import socket

# Get domain name from the user
domain = input("Enter the domain name (e.g., example.com): ")

try:
    # Perform DNS lookup
    ip_address = socket.gethostbyname(domain)

    print("\n=== DNS Lookup Result ===")
    print("Domain Name :", domain)
    print("IP Address  :", ip_address)

except socket.gaierror:
    print("Error: Unable to resolve the domain name.")