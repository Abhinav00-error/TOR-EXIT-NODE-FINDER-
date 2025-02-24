# TOR-EXIT-NODE-FINDER-
TOR EXIT NODE FINDER is a powerful penetration testing tool designed to check whether a given IP address belongs to a Tor exit node. It also provides detailed IP information to help cybersecurity professionals analyze network traffic and potential anonymity risks
.Features

.Tor Exit Node Detection: Verifies if an IP address is part of the Tor exit node list.
.IP Information Lookup: Fetches geolocation, ISP, region, and other details of the provided IP.
.Real-Time Data: Uses the Tor Project’s exit node list for the most accurate results.
.User-Agent Spoofing: Avoids API blocks while fetching IP details.
.Fully CLI-Based: Designed for penetration testers and cybersecurity professionals.
🛠️ Technologies Used

    Language: Python
    Libraries: requests, sys, socket, json
    APIs Used:
        Tor Project Exit Nodes
        IP Information API:

🔧 How It Works
.The tool fetches the latest Tor exit nodes from the Tor Project.
.It checks if the provided IP is in the exit node list.
.If the IP matches an exit node, an alert is displayed.
.If not, it fetches IP details (country, city, ISP, etc.).

USAGE
git clone tool link

chmod +x tof.py

python3 tof.py <ip>



