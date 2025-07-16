visitors = set()
blacklist = {'192.168.1.1', '10.0.0.1'}

def log_ip(ip):
    if {ip}.isdisjoint(blacklist):
        visitors.add(ip)
    else:
        print(f"Blocked blacklisted IP: {ip}")

log_ip('192.168.1.2')
log_ip('192.168.1.1')  