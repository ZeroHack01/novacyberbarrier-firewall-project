<div align="center">
  
# 🛡️ NovaCyberBarrier Firewall Project 🔥

<img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT" />
<img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Platform-Linux-green?logo=linux&logoColor=white" alt="Platform" />
<img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status" />

<p align="center">
  <img src="https://img.shields.io/badge/iptables-Powered-orange?style=for-the-badge&logo=linux&logoColor=white" alt="iptables" />
  <img src="https://img.shields.io/badge/CLI-Tool-yellow?style=for-the-badge&logo=gnometerminal&logoColor=white" alt="CLI" />
</p>

<p>
  <b>NovaCyberBarrier</b> is a powerful Linux-based CLI firewall management tool written in Python. It leverages <b>iptables</b> to help you easily manage IP access, apply rate limits, and persist your firewall rules with simple commands.
</p>

<p align="center">
  <a href="#-installation">Quick Install</a> •
  <a href="#-feature-details">Features</a> •
  <a href="#-quick-command-reference">Commands</a> •
  <a href="#-requirements">Requirements</a>
</p>

</div>

---

## ✨ Features Overview

<table>
  <tr>
    <td width="50%">
      <h3>🔒 Network Protection</h3>
      <ul>
        <li>Block malicious IP addresses</li>
        <li>Control port access</li>
        <li>Apply traffic rate limiting</li>
      </ul>
    </td>
    <td width="50%">
      <h3>⚙️ Management</h3>
      <ul>
        <li>Persist rules across reboots</li>
        <li>Comprehensive logging</li>
        <li>Easy rule listing and monitoring</li>
      </ul>
    </td>
  </tr>
</table>

---

## 📋 Feature Details

### 🔐 Add and Remove Rules

<details open>
<summary><b>Control TCP traffic on specified ports</b></summary>
<br>

Allow or block TCP traffic on any port with simple commands:

```bash
# Add a rule allowing traffic on a port
sudo python3 novacyberbarrier.py add [port]

# Remove a rule blocking traffic on a port
sudo python3 novacyberbarrier.py remove [port]
```

</details>

### 🚫 IP Address Management

<details open>
<summary><b>Control access for specific IP addresses</b></summary>
<br>

Keep your network secure by managing IP access:

```bash
# Block an IP address
sudo python3 novacyberbarrier.py block [ip]

# Allow a previously blocked IP address
sudo python3 novacyberbarrier.py allow [ip]
```

</details>

### ⏱️ Rate Limiting

<details open>
<summary><b>Prevent abuse and control traffic</b></summary>
<br>

Apply rate limits to prevent DoS attacks and control bandwidth usage:

```bash
# Apply rate limiting to an IP address
sudo python3 novacyberbarrier.py limit [ip]
```

This helps manage excessive traffic from specific sources and prevents abuse.

</details>

### 📋 List Current Rules

<details open>
<summary><b>View your firewall configuration</b></summary>
<br>

Easily check what rules are currently active:

```bash
# Display all active rules
sudo python3 novacyberbarrier.py list
```

</details>

### 📝 Log Actions

<details open>
<summary><b>Track all firewall activities</b></summary>
<br>

All actions are logged for auditing and troubleshooting:

```bash
# Check the log file
cat novacyberbarrier.log
```

</details>

### 💾 Save Rules

<details open>
<summary><b>Persist your firewall configuration</b></summary>
<br>

Make sure your rules survive system reboots:

```bash
# Save current rules
sudo python3 novacyberbarrier.py save
```

</details>

---

## 🔧 Requirements

<div align="center">

| Requirement | Description |
|-------------|-------------|
| <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python" /> | Python 3.x |
| <img src="https://img.shields.io/badge/iptables-Required-red?logo=linux&logoColor=white" alt="iptables" /> | Usually pre-installed on Linux |
| <img src="https://img.shields.io/badge/Root-Permissions-critical?logo=linux&logoColor=white" alt="Root" /> | Sufficient permissions to modify firewall settings |

</div>

---

## 📥 Installation

<div align="left">

```bash
# Clone the Repository
git clone https://github.com/ZeroHack01/novacyberbarrier-firewall-project.git
cd novacyberbarrier-firewall-project

# Make the script executable
chmod +x novacyberbarrier.py

# Run with root privileges
sudo ./novacyberbarrier.py [command] [arguments]
```

</div>

#### One-Line Quick Install (Copy & Paste):

```bash
git clone https://github.com/ZeroHack01/novacyberbarrier-firewall-project.git && cd novacyberbarrier-firewall-project && chmod +x novacyberbarrier.py && sudo ./novacyberbarrier.py list
```



---

<div align="center">

## 🔄 Quick Command Reference

| Command | Description | Example |
|---------|-------------|---------|
| `add` | Allow traffic on a port | `sudo python3 novacyberbarrier.py add 80` |
| `remove` | Block traffic on a port | `sudo python3 novacyberbarrier.py remove 8080` |
| `block` | Block an IP address | `sudo python3 novacyberbarrier.py block 192.168.1.100` |
| `allow` | Allow an IP address | `sudo python3 novacyberbarrier.py allow 192.168.1.100` |
| `limit` | Rate limit an IP | `sudo python3 novacyberbarrier.py limit 192.168.1.100` |
| `list` | Show all rules | `sudo python3 novacyberbarrier.py list` |
| `save` | Persist rules | `sudo python3 novacyberbarrier.py save` |

</div>

---

<div align="center">
  
### 📊 Project Status
  
<img src="https://img.shields.io/maintenance/yes/2025" alt="Maintenance" />
<img src="https://img.shields.io/github/last-commit/ZeroHack01/novacyberbarrier-firewall-project" alt="Last Commit" />

### 👨‍💻 Contribute
  
<a href="https://github.com/ZeroHack01/novacyberbarrier-firewall-project/issues">
  <img src="https://img.shields.io/github/issues/ZeroHack01/novacyberbarrier-firewall-project?style=for-the-badge" alt="Issues" />
</a>
<a href="https://github.com/ZeroHack01/novacyberbarrier-firewall-project/pulls">
  <img src="https://img.shields.io/github/issues-pr/ZeroHack01/novacyberbarrier-firewall-project?style=for-the-badge" alt="Pull Requests" />
</a>

</div>

---

<div align="center">
  
### 📜 License
  
This project is licensed under the MIT License - see the LICENSE file for details.

</div>
