import socket
import dns.resolver

def get_dns_info(url):
    try:
        # Resolve IP address
        ip_address = socket.gethostbyname(url)
        print(f"IP Address: {ip_address}")

        # Resolve DNS records (e.g., A, MX, NS)
        for record_type in ['A', 'MX', 'NS']:
            try:
                answers = dns.resolver.resolve(url, record_type)
                print(f"{record_type} Records:")
                for answer in answers:
                    print(f" - {answer}")
            except dns.resolver.NoAnswer:
                print(f"No {record_type} records found.")

    except socket.gaierror:
        print("Error: Invalid URL or DNS resolution failed.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    user_url = input("Enter a URL (e.g., example.com): ").strip()
    get_dns_info(user_url)
