visitors = set()
blacklist = {'192.168.1.100', '10.0.0.15'}

def track_visitor(ip):
    if ip not in blacklist:
        visitors.add(ip)
    else:
        print(f"Blocked blacklisted IP: {ip}")

def get_stats():
    print(f"Unique visitors: {len(visitors)}")
    print(f"Blacklisted visitors blocked: {len(blacklist)}")

track_visitor('192.168.1.1')
track_visitor('192.168.1.1') 
track_visitor('192.168.1.100')  
backup = visitors.copy()
get_stats()