# Pynmap

A Python script that wraps Nmap to perform network scans on IP ranges or CIDR notations, with options for scanning specific ports and additional Nmap options. The results are saved to individual files named after each IP address.

## Features

- Scan single IP addresses or IP ranges in CIDR notation.
- Scan specific ports or all ports (`-p-`).
- Pass additional Nmap options to customize the scan.
- Save scan results to files named after each IP address.

## Prerequisites

- **Nmap**: Ensure Nmap is installed on your system. You can check if it's installed by running `nmap --version` in your terminal.
- **Python 3.12**: This script is compatible with Python 3.12.

## Installation

1. **Install Nmap**: Follow instructions from the [Nmap official website](https://nmap.org/download.html) to install Nmap on your system.
2. **Install Python Dependencies**: The script uses Python's `subprocess` module, which is part of the standard library, so no additional Python packages are required.

## Usage

### Command-Line Arguments
- `ip_range`: The IP address range or CIDR notation to scan (e.g., `192.168.1.1-192.168.1.10` or `192.168.1.0/24`).
- `--port_range`: The port range to scan (e.g., `22-80`). Default is `-p-` for scanning all ports.
- `--options`: Additional Nmap options (e.g., `-sS -T4`).

### Examples

- **Scan a specific IP range with a custom port range and Nmap options**:
```bash
python pynmap.py 192.168.1.0/24 --port_range 22-80 --options "-sS -T4"
```

- **Scan an IP range with default port range (all ports) and custom Nmap options:**:
```bash
python pynmap.py 192.168.1.0/24 --options "-sS -T4"
```

- **Scan a single IP address with default port range and no additional options:**:
```bash
python pynmap.py 192.168.1.1
```

### Files
```
pynmap.py: The Python script for running Nmap scans.
nmap_results/: Directory where scan results are saved. Each file is named after the IP address.
```

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.