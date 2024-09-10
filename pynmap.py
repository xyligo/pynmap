#!/usr/bin/env python3

import subprocess
import argparse
import os
import ipaddress


def run_nmap_scan(ip, port_range, nmap_options):
    """Run Nmap scan for a specific IP address and port range with additional options."""
    output_file = f"{ip}.txt"
    command = ["nmap", port_range] + nmap_options + [ip]

    with open(output_file, "w") as file:
        subprocess.run(command, stdout=file, stderr=subprocess.STDOUT, text=True)


def parse_ip_range(ip_range):
    """Generate a list of IP addresses from a given range or CIDR notation."""
    ips = []
    try:
        # Check if the IP range is in CIDR notation
        network = ipaddress.ip_network(ip_range, strict=False)
        ips = [str(ip) for ip in network]
    except ValueError:
        # If not in CIDR notation, assume it's a simple IP range
        start_ip, end_ip = ip_range.split("-")
        start_ip = ipaddress.ip_address(start_ip)
        end_ip = ipaddress.ip_address(end_ip)
        ips = [str(ip) for ip in ipaddress.summarize_address_range(start_ip, end_ip)]

    return ips


def main():
    parser = argparse.ArgumentParser(description="Nmap Scanner Wrapper")
    parser.add_argument(
        "ip_range",
        type=str,
        help="The IP address range or CIDR notation to scan (e.g., 192.168.1.1-192.168.1.10 or 192.168.1.0/24)",
    )
    parser.add_argument(
        "--port_range",
        type=str,
        default="-p-",
        help="The port range to scan (e.g., 22-80). Default is '-p-' for all ports.",
    )
    parser.add_argument(
        "--options",
        type=str,
        default="",
        help="Additional Nmap options (e.g., '-sS -T4')",
    )

    args = parser.parse_args()

    ip_range = args.ip_range
    port_range = args.port_range
    nmap_options = args.options.split()

    # Create a directory to store the results if it doesn't exist
    if not os.path.exists("nmap_results"):
        os.makedirs("nmap_results")

    os.chdir("nmap_results")

    ips = parse_ip_range(ip_range)
    for ip in ips:
        print(f"Scanning {ip} on ports {port_range}...")
        run_nmap_scan(ip, port_range, nmap_options)
        print(f"Output saved to {ip}.txt")


if __name__ == "__main__":
    main()
