!/bin/bash

echo Starting the Endpoit Tracker tools.

exec python /home/sedk/acitoolkit/applications/endpointtracker/aci-endpoint-tracker.py -u https://cphlab-apic01.cisco.com -l admin -p Cisco123 -i 127.0.0.1 -a root -s Cisco123 &
exec python /home/sedk/acitoolkit/applications/endpointtracker/aci-endpoint-tracker-gui.py -i 127.0.0.1 -a root -s Cisco123 --ip 10.54.60.58 &

