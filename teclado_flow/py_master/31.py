with open('show_airports.txt', 'r') as f:
    content = f.read().splitlines()
    content = content[1:]
    ip_mac = list()
    for line in content:
        ip = line.split()[1]
        mac = line.split()[3]
        ip_mac.append((ip, mac))

print(ip_mac)

# print(content)