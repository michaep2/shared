#!/usr/bin/python

import requests
import json

apic = 'cphlab-apic01.cisco.com'
vcenter_ip = '10.54.60.110'
vCenter_Datacenter = 'cphlab'
vmm_controller = 'cphlab-vcenter2.cisco.com'
vmm_credentials = 'vcenter-credentials-sedk'

user = 'admin'
password = 'Cisco123'
vcenter_user = 'devops'
vcenter_password = 'Cisco123'

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

auth = {'aaaUser': {'attributes': {'name': user, 'pwd': password } } }

sesh = requests.Session()
resp = sesh.post('https://{0}/api/mo/aaaLogin.json'.format(apic), data=json.dumps(auth), verify=False)
status = resp.status_code
cookies = resp.cookies
print status



# This one creates the Link level Interface Policy for '1GE auto"
jsondata = {"fabricHIfPol":{"attributes":{"speed":"1G","descr":"","dn":"uni/infra/hintfpol-IntPol_1G_Auto","name":"IntPol_1G_Auto","ownerKey":"","ownerTag":""}}}
resp = sesh.post('https://{0}/api/node/mo/uni/infra/lacplagp-IntPol_1G_Auto.json'.format(apic), cookies = cookies, data = json.dumps(jsondata), verify = False)
print resp
