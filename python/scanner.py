import nmap

scanner = nmap.PortScanner()

print('\nWelcome!')

ip_addr = input('\nEnter ip adress: ')

print('Your Ip you entered is: ', ip_addr)

resp = input(
    '\nEnter type of scan you want: \n\t1) SYN ACK scan\n\t2) UDP Scan\n\t3) Comprehensive scan\n\t')

print('\nYou selected: ', resp)

if resp == '1':
    print('\nNmap version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print('Ip Status: ,', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print('\nNmap version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print('Ip Status: ,', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print('\nNmap version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print('Ip Status: ,', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
else:
    print('Please choose a valid value!')