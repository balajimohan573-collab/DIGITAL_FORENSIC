from collections import defaultdict

# Simulated network traffic log
traffic_log = [
    "10.0.0.5 192.168.1.10 21",
    "10.0.0.5 192.168.1.10 22",
    "10.0.0.5 192.168.1.10 23",
    "10.0.0.5 192.168.1.10 25",
    "10.0.0.5 192.168.1.10 53",
    "10.0.0.5 192.168.1.10 80",
    "10.0.0.5 192.168.1.10 110",
    "10.0.0.5 192.168.1.10 135",
    "10.0.0.5 192.168.1.10 139",
    "10.0.0.5 192.168.1.10 443",

    "192.168.1.20 192.168.1.10 80",
    "192.168.1.20 192.168.1.10 443",
    "192.168.1.20 192.168.1.10 80"
]

# Store ports contacted by each source IP
port_activity = defaultdict(lambda: defaultdict(set))

# Analyze each traffic entry
for line in traffic_log:
    source_ip, destination_ip, destination_port = line.split()

    port_activity[source_ip][destination_ip].add(
        int(destination_port)
    )

# Number of different ports considered suspicious
PORT_SCAN_THRESHOLD = 5

print("=" * 55)
print("        NETWORK PORT-SCAN DETECTION")
print("=" * 55)

scan_detected = False

for source_ip, destinations in port_activity.items():

    for destination_ip, ports in destinations.items():

        print("\nSource IP      :", source_ip)
        print("Destination IP :", destination_ip)
        print("Ports Contacted:", sorted(ports))

        if len(ports) >= PORT_SCAN_THRESHOLD:
            scan_detected = True

            print("STATUS         : POSSIBLE PORT SCAN")
            print("Different Ports:", len(ports))
        else:
            print("STATUS         : Normal traffic")

        print("-" * 55)

print("\nFinal Result")

if scan_detected:
    print("WARNING: Port-scanning behaviour detected.")
else:
    print("No obvious port-scanning behaviour detected.")
