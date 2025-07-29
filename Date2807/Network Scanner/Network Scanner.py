from scapy.all import ICMP, IP, sr1
import time
import socket

def speed_test(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"\n⏱️ Scan completed in {duration:.2f} seconds")
        return result
    return wrapper

class Scanner:
    def __init__(self, subnet):
        self.subnet = subnet
        self.results = {}

    def _ping_host(self, ip):
        try:
            pkt = IP(dst=ip)/ICMP()
            reply = sr1(pkt, timeout=1, verbose=0)
            return reply is not None
        except Exception as e:
            print(f"[Error] Ping failed for {ip}: {e}")
            return False

    def _generate_ips(self):
        base = ".".join(self.subnet.split(".")[:3])
        for i in range(1, 255):
            yield f"{base}.{i}"

    @speed_test
    def scan(self):
        print(f"🔍 Scanning subnet: {self.subnet}.0/24...\n")
        for ip in self._generate_ips():
            if self._ping_host(ip):
                try:
                    hostname = socket.gethostbyaddr(ip)[0]
                except:
                    hostname = "Unknown"
                self.results[ip] = hostname
                print(f"✅ {ip} - {hostname}")
            else:
                self.results[ip] = "Offline"
        return self.results

if __name__ == "__main__":
    subnet_input = input("Enter subnet (e.g., 192.168.1): ").strip()
    scanner = Scanner(subnet_input)
    scanner.scan()
