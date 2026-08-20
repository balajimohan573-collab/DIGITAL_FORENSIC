import socket

domain = input("Enter domain name: ").strip()

print("\n===== BASIC WHOIS INFORMATION =====")

try:
    print("Domain:", domain)
    print("IP Address:", socket.gethostbyname(domain))
    print("Hostname:", socket.getfqdn(domain))
    print("Note: This is basic DNS information, not full WHOIS registration data.")

except socket.gaierror:
    print("Could not resolve the domain.")
