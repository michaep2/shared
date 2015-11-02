# ------------------------------------------------
# Show Tenant
#
# Cisco Systems Denmark
# ------------------------------------------------

# Login to the APIC
session = ACI.Session('https://10.54.61.56', 'admin', 'Cisco123')
resp = session.login()
if not resp.ok:
	print '%% Could not login to APIC'
	sys.exit(0)

print '\nTenants'
print '------------------------'
tenants = ACI.Tenant.get(session)
for tenant in tenants:
	print tenant.name

pause = raw_input()