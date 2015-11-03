# ------------------------------------------------
# Create Tenant with App, BD, Context and EPGs
# Attach EPGs to vlans on interfaces
#
# Cisco Systems Denmark
# ------------------------------------------------

# Import ACI Toolkit
import acitoolkit.acitoolkit as ACI

# Suppress HTTPS certificate validation warning message
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

# Define static values
Tenant_Name = 'Test-DevOps-Tenant'
AP_Name = 'Demo-App'
EPG1_Name = 'web-frontend'
EPG2_Name = 'app-layer'
EPG3_Name = 'database-backend'
Context_Name = 'VRF1'
BD_Name = 'BD1'

# Create the Tenant
tenant = ACI.Tenant(Tenant_Name)

# Create the Application Profile
app = ACI.AppProfile(AP_Name, tenant)

# Create the EPGs
web_epg = ACI.EPG(EPG1_Name, app)
app_epg = ACI.EPG(EPG2_Name, app)
db_epg = ACI.EPG(EPG3_Name, app)

# Create a Context and BridgeDomain
# Place all EPGs in the Context and in the same BD
context = ACI.Context(Context_Name, tenant)
bd = ACI.BridgeDomain(BD_Name, tenant)

# Define a subnet in the BridgeDomain
subnet1 = ACI.Subnet('Subnet1', bd)
subnet2 = ACI.Subnet('Subnet2', bd)
subnet1.set_addr('10.20.30.1/24')
subnet2.set_addr('192.168.1.1/24')

# Add Context and Subnets to BridgeDomain
bd.add_context(context)
bd.add_subnet(subnet1)
bd.add_subnet(subnet2)

# Define three EPGs
web_epg.add_bd(bd)
app_epg.add_bd(bd)
db_epg.add_bd(bd)

# Define a contract with a single entry
contract1 = ACI.Contract('SQL-Contract', tenant)
contract1_entry1 = ACI.FilterEntry('entry1',
                     applyToFrag='no',
                     arpOpc='unspecified',
                     dFromPort='3306',
                     dToPort='3306',
                     etherT='ip',
                     prot='tcp',
                     sFromPort='1',
                     sToPort='65535',
                     tcpRules='unspecified',
                     parent=contract1)

# Provide the contract from one EPG and consume from the other
db_epg.provide(contract1)
app_epg.consume(contract1)

# Define a contract with a single entry
contract2 = ACI.Contract('App-Contract', tenant)
contract2_entry1 = ACI.FilterEntry('entry1',
                     applyToFrag='no',
                     arpOpc='unspecified',
                     dFromPort='443',
                     dToPort='443',
                     etherT='ip',
                     prot='tcp',
                     sFromPort='1',
                     sToPort='65535',
                     tcpRules='unspecified',
                     parent=contract2)

# Provide the contract from one EPG and consume from the other
app_epg.provide(contract2)
web_epg.consume(contract2)


# Physical Interfaces
# web_if = ACI.Interface('eth', '1', '101', '1', '10', None)
# app_if = ACI.Interface('eth', '1', '101', '1', '11', None)
# db_if = ACI.Interface('eth', '1', '101', '1', '12', None)

# Create vlans on physical interfaces
# vlan10_webif = ACI.L2Interface('vlan10_webif', 'vlan', '10')
# vlan10_webif.attach(web_if)
# vlan20_appif = ACI.L2Interface('vlan20_appif', 'vlan', '20')
# vlan20_appif.attach(app_if)
# vlan30_dbif = ACI.L2Interface('vlan30_dbif', 'vlan', '30')
# vlan30_dbif.attach(db_if)

# Attach EPGs to vlan_if
# web_epg.attach(vlan10_webif)
# app_epg.attach(vlan20_appif)
# db_epg.attach(vlan30_dbif)


# Login to the APIC
session = ACI.Session('https://10.54.61.56', 'admin', 'Cisco123')
resp = session.login()
if not resp.ok:
    print '%% Could not login to APIC'
    sys.exit(0)

print "\n %s \n" % tenant.get_json()

# Push it all to the APIC
resp = session.push_to_apic(tenant.get_url(),
                            tenant.get_json())
if not resp.ok:
    print '%% Error: Could not push configuration to APIC'
    print resp.text
