import csv
import telnetlib

# Set the IP address, username, and password for the switch
switch_ip = '10.0.0.1'
username = 'admin'
password = 'password'

# Connect to the switch using Telnet
tn = telnetlib.Telnet(switch_ip)

# Wait for the login prompt, then enter the username and password
tn.read_until(b'Username: ')
tn.write(username.encode('ascii') + b'\n')

tn.read_until(b'Password: ')
tn.write(password.encode('ascii') + b'\n')

# Run the "show cdp neighbors" command and store the output
tn.write(b'show cdp neighbors\n')
output = tn.read_until(b'#').decode('utf-8')

# Close the Telnet connection
tn.close()

# Split the output into a list of rows
rows = output.split('\n')

# Use the csv.DictReader to parse the rows
reader = csv.DictReader(rows)

# Iterate over each row in the output
for row in reader:
  # Print out the hostname and IP address for the neighbor
  print(f'Hostname: {row["Device ID"]}')
  print(f'IP Address: {row["IP address"]}')
