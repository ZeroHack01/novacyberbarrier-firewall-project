+ #!/usr/bin/env python3
# Novacyberbarrier firewall project

import subprocess
import sys
import logging

# Configure logging
logging.basicConfig(filename='nova_cyber_barrier.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class NovaCyberBarrier:
    def __init__(self):
        self.rules_file = "/etc/iptables/rules.v4"
        self.log_file = "nova_cyber_barrier.log"

    def log_action(self, action, port=None, ip=None):
        if port:
            logging.info(f"{action} - Port: {port}")
        if ip:
            logging.info(f"{action} - IP: {ip}")

    def add_rule(self, port):
        try:
            subprocess.run(["iptables", "-A", "INPUT", "-p", "tcp", "--dport", str(port), "-j", "ACCEPT"], check=True)
            self.log_action("Rule added", port=port)
            print(f"[NovaCyberBarrier] Rule added: Allow TCP traffic on port {port}")
        except subprocess.CalledProcessError:
            print(f"[NovaCyberBarrier] Failed to add rule for port {port}")

    def remove_rule(self, port):
        try:
            subprocess.run(["iptables", "-D", "INPUT", "-p", "tcp", "--dport", str(port), "-j", "ACCEPT"], check=True)
            self.log_action("Rule removed", port=port)
            print(f"[NovaCyberBarrier] Rule removed: Block TCP traffic on port {port}")
        except subprocess.CalledProcessError:
            print(f"[NovaCyberBarrier] Failed to remove rule for port {port}")

    def block_ip(self, ip):
        try:
            subprocess.run(["iptables", "-A", "INPUT", "-s", str(ip), "-j", "DROP"], check=True)
            self.log_action("IP blocked", ip=ip)
            print(f"[NovaCyberBarrier] IP blocked: {ip}")
        except subprocess.CalledProcessError:
            print(f"[NovaCyberBarrier] Failed to block IP {ip}")

    def allow_ip(self, ip):
        try:
            subprocess.run(["iptables", "-D", "INPUT", "-s", str(ip), "-j", "DROP"], check=True)
            self.log_action("IP allowed", ip=ip)
            print(f"[NovaCyberBarrier] IP allowed: {ip}")
        except subprocess.CalledProcessError:
            print(f"[NovaCyberBarrier] Failed to allow IP {ip}")

    def rate_limit_ip(self, ip):
        try:
            subprocess.run(["iptables", "-A", "INPUT", "-s", str(ip), "-m", "limit", "--limit", "5/min", "-j", "ACCEPT"], check=True)
            self.log_action("Rate limiting applied", ip=ip)
            print(f"[NovaCyberBarrier] Rate limiting applied to IP: {ip}")
        except subprocess.CalledProcessError:
            print(f"[NovaCyberBarrier] Failed to apply rate limiting to IP {ip}")

    def list_rules(self):
        try:
            rules = subprocess.run(["iptables", "-L"], capture_output=True, text=True, check=True)
            print(rules.stdout)
        except subprocess.CalledProcessError:
            print("[NovaCyberBarrier] Failed to list rules")

    def save_rules(self):
        try:
            subprocess.run(["iptables-save"], stdout=open(self.rules_file, 'w'), check=True)
            print(f"[NovaCyberBarrier] Rules saved to {self.rules_file}")
        except subprocess.CalledProcessError:
            print("[NovaCyberBarrier] Failed to save rules")

def main():
    firewall = NovaCyberBarrier()
    
    if len(sys.argv) < 2:
        print("[NovaCyberBarrier] Usage: nova_cyber_barrier.py [add|remove|block|allow|limit|list|save] [port|ip]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add" and len(sys.argv) == 3:
        port = sys.argv[2]
        firewall.add_rule(port)
    elif command == "remove" and len(sys.argv) == 3:
        port = sys.argv[2]
        firewall.remove_rule(port)
    elif command == "block" and len(sys.argv) == 3:
        ip = sys.argv[2]
        firewall.block_ip(ip)
    elif command == "allow" and len(sys.argv) == 3:
        ip = sys.argv[2]
        firewall.allow_ip(ip)
    elif command == "limit" and len(sys.argv) == 3:
        ip = sys.argv[2]
        firewall.rate_limit_ip(ip)
    elif command == "list":
        firewall.list_rules()
    elif command == "save":
        firewall.save_rules()
    else:
        print("[NovaCyberBarrier] Invalid command or arguments")

if __name__ == "__main__":
    main()


