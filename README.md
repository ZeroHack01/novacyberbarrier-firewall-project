# 🔥 NovaCyberBarrier Firewall Project

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg) 
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Linux-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

NovaCyberBarrier is a Linux-based CLI firewall management tool written in Python. It uses **iptables** to allow you to easily manage IP access, apply rate limits, and persist your firewall rules.

## Features

### 1. Add and Remove Rules
- **Description**: Allow or block TCP traffic on specified ports.
- **How to Use**:
  - To add a rule allowing traffic on a port:
    ```bash
    sudo python3 novacyberbarrier.py add [port]
    ```
  - To remove a rule blocking traffic on a port:
    ```bash
    sudo python3 novacyberbarrier.py remove [port]
    ```

### 2. IP Address Management
- **Description**: Manage access for specific IP addresses.
  - Block specific IP addresses from accessing your server.
  - Allow previously blocked IP addresses back into your network.
- **How to Use**:
  - To block an IP address:
    ```bash
    sudo python3 novacyberbarrier.py block [ip]
    ```
  - To allow an IP address:
    ```bash
    sudo python3 novacyberbarrier.py allow [ip]
    ```

### 3. Rate Limiting
- **Description**: Apply rate limits to specific IP addresses to prevent abuse and control traffic.
- **How to Use**:
  - To apply rate limiting to an IP address:
    ```bash
    sudo python3 novacyberbarrier.py limit [ip]
    ```
  - This helps manage excessive traffic from specific sources.

### 4. List Current Rules
- **Description**: View currently configured `iptables` rules.
- **How to Use**:
  - To display all active rules:
    ```bash
    sudo python3 novacyberbarrier.py list
    ```
  - This command will show you the current state of your firewall configuration.

### 5. Log Actions
- **Description**: All actions are logged in a dedicated log file for auditing and troubleshooting.
- **How to Use**:
  - To check the log file for a history of actions:
    ```bash
    cat novacyberbarrier.log
    ```
  - This is useful for tracking changes and debugging issues.

### 6. Save Rules
- **Description**: Persist `iptables` rules to a configuration file, ensuring they remain after a reboot.
- **How to Use**:
  - To save the current rules:
    ```bash
    sudo python3 novacyberbarrier.py save
    ```
  - This ensures that your firewall settings are preserved even when the system is restarted.

## Requirements

- Python 3.x
- `iptables` (usually pre-installed on Linux)
- Sufficient permissions (root) to modify firewall settings

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/novacyberbarrier.git
   cd novacyberbarrier
