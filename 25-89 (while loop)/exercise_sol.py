# 1
# while True:
#     name = input('enter a golden name :')
#     if len(name) > 4 and name.count('o') == 2:
#         break
#     print('not a golden name ')
#
# print('golden name')

ip1_address = input('please enter ip in this forman ip/mask')
ip2_address = input('please enter ip in this forman ip/mask')

# 1  two ip's in the same network
# mask == mask
# 16 //8 =2   199.177.1.55/16  199.177.1.55/24
# 000.000.000.000/00
ip1 = ip1_address[:ip1_address.find('/')]
mask1 = int(ip1_address[ip1_address.find('/') + 1:])

ip2 = ip2_address[:ip2_address.find('/')]
mask2 = int(ip2_address[ip2_address.find('/') + 1:])

print(f'ip1 {ip1} ip2 {ip2}')
print(f'mask1 {mask1} mask2 {mask2}')

if mask2 == mask1:
    byte = mask2 // 8
    ip1 = ip1.split('.')
    ip2 = ip2.split('.')
    print(f'ip1 {ip1} ip2{ip2}')
    for i in range(byte):
        if ip1[i] != ip2[i]:
            break
    else:
        print('same network')
        if byte == 2:  # a.b.c.d
            host = [ip1[0], ip1[1], 0, 0]
            while host[2] <= 255:
                if host[3] <= 255:
                    print(f'{host[0]}.{host[1]}.{host[2]}.{host[3]}')
                    host[3] += 1
                else:
                    host[2] += 1
                    host[3] = 0
