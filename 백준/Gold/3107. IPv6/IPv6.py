import sys
input = sys.stdin.readline

ipv6 = input().strip()

if ipv6.count(":") == 8:
  ipv6 = ipv6.replace("::", ":")

ipv6 = ipv6.replace("::", (7-ipv6.count(":"))*":" + "::")
ipv6 = ipv6.split(":")

for i in range(len(ipv6)):
  if len(ipv6[i]) < 4:
    ipv6[i] = (4-len(ipv6[i]))*'0' + ipv6[i]
    
print(":".join(ipv6))