# ------------------------------------------------
# Show Tenant
#
# Cisco Systems Denmark
# ------------------------------------------------

# Import ACI Toolkit
import acitoolkit.acitoolkit as ACI
import acitoolkit.aciphysobject as PHYS
import requests.packages.urllib3

#---------------------------
# Tenant Exists (no-case)
#---------------------------
def TenantExists_CaseInsensitive(tenant_name, tenants):
	for tenant in tenants:
		if tenant.name.lower() == tenant_name.lower():
			return True
	return False

#---------------------------
# Tenant Exists (case)
#---------------------------
def TenantExists_CaseSensitive(tenant_name, tenants):
	for tenant in tenants:
		if tenant.name == tenant_name:
			return True
	return False

#---------------------------
# Create Tenant
#---------------------------
def CreateTenant(tenant_name):
	tenants = ACI.Tenant.get(session)
	if TenantExists_CaseInsensitive(tenant_name, tenants):
		print '\nTenant already exists. Skipping'
	else:
		print '\nCreating tenant...'
		tenant = ACI.Tenant(tenant_name)
		# Push it all to the APIC
		resp = session.push_to_apic(tenant.get_url(),tenant.get_json())
		if not resp.ok:
			print '%% Error: Could not push configuration to APIC'
			print resp.text

#---------------------------
# Delete Tenant
#---------------------------
def DeleteTenant(tenant_name):
	if tenant_name.lower() in ['infra','common','mgmt']:
		print '\nInfrastructure tenants cannot be deleted.'
	else:
		tenants = ACI.Tenant.get(session)
		if TenantExists_CaseSensitive(tenant_name, tenants):
			print '\nDeleting tenant.'
			tenant = ACI.Tenant(tenant_name)
			tenant.mark_as_deleted()
			# Push it all to the APIC
			resp = session.push_to_apic(tenant.get_url(),tenant.get_json())
			if not resp.ok:
				print '%% Error: Could not push configuration to APIC'
				print resp.text
		else:
			print '\nTenant does not exist. Skipping'

#---------------------------
# Main
#---------------------------

# Suppress HTTPS certificate validation warning message
requests.packages.urllib3.disable_warnings()

# Login to the APIC
session = ACI.Session('https://10.54.61.56', 'admin', 'Cisco123')
resp = session.login()
if not resp.ok:
	print '%% Could not login to APIC'
	sys.exit(0)

choice = ''
while choice != 'q':
	print '\n1. Show Tenants'
	print '2. Create Tenant'
	print '3. Delete Tenant'
	print '4. Show nodes'
	print '5. Show interfaces'
	print 'Q. Quit'
	choice = raw_input('\nPlease choose: ').lower()
	print ''

	if choice == '1':
		print 'Tenants'
		print '------------------------'
		tenants = ACI.Tenant.get(session)
		for tenant in tenants:
			print tenant.name
	elif choice == '2':
		tenant_name = raw_input('Type name of tenant you want to create: ')
		CreateTenant(tenant_name)
	elif choice == '3':
		tenant_name = raw_input('Type name of tenant you want to delete: ')
		DeleteTenant(tenant_name)
	elif choice == '4':
		nodes = PHYS.Node.get(session)
		print 'Spine and Leaf nodes'
		print '--------------------'
		for node in nodes:
			if node.role in ['spine','leaf']:
				print node.name
	elif choice == '5':
		interfaces = ACI.Interface.get(session)
		for interface in interfaces:
			print interface.name
