# ------------------------------------------------
# Show Tenant
#
# Cisco Systems Denmark
# ------------------------------------------------

# Import ACI Toolkit
import acitoolkit.acitoolkit as ACI

# Suppress HTTPS certificate validation warning message
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

# Define static value for Tenant name
Tenant_Name = 'Test'

# Login to the APIC
session = ACI.Session('https://10.54.61.56', 'admin', 'Cisco123')
resp = session.login()
if not resp.ok:
    print '%% Could not login to APIC'
    sys.exit(0)

# Create the Tenant
tenant = ACI.Tenant(Tenant_Name)

# Display JSON code being sent to the APIC
print "\n %s \n" % tenant.get_json()

# Push it all to the APIC
resp = session.push_to_apic(tenant.get_url(),
                            tenant.get_json())
if not resp.ok:
    print '%% Error: Could not push configuration to APIC'
    print resp.text
