import csv
from netmiko import ConnectHandler

def get_cdp_neighbors(device):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show cdp neighbors")
    return output

def parse_cdp_neighbors(output):
    neighbors = []
    for line in output.splitlines():
        if '.' in line:
            fields = line.split()
            hostname = fields[0]
            ip_address = fields[1]
            neighbors.append((hostname, ip_address))
    return neighbors

def save_to_csv(neighbors):
    with open('cdp_neighbors.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["hostname", "ip_address"])
        writer.writerows(neighbors)

def main():
    device = {
        "device_type": "cisco_ios",
        "host": "ipaddress of your device",
        "username": "pick your name",       # Not recommended to hard code username and password.
        "password": "pick your password",
    }
    output = get_cdp_neighbors(device)
    neighbors = parse_cdp_neighbors(output)
    save_to_csv(neighbors)

if __name__ == "__main__":
    main()
