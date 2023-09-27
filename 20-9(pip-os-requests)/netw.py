import ipaddress

# ip
# network
# ipv6

ip1 = ipaddress.ip_address('192.168.0.255')
ip2 = ip1+1
print(ip2)
# print(ip1.is_global)  # is private or public ip
# print(ip1.is_private)

network1 = ipaddress.ip_network('192.168.0.0/24')
print(network1)
if ip1 in network1:
    print('yes')

print(ip2 in network1 )

#
# for ip in network1:
#     print(ip)