import csv
import paramiko

# Set the IP address and credentials for the switch
switch_ip = '10.0.0.1'
username = 'admin'
password = 'password'

# Establish an SSH connection to the switch
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(switch_ip, username=username, password=password)

# Run the "show cdp neighbors" command and store the output
stdin, stdout, stderr = ssh.exec_command('show cdp neighbors')
output = stdout.read().decode('utf-8')

# Close the SSH connection
ssh.close()

# Split the output into a list of rows
rows = output.split('\n')

# Use the csv.DictReader to parse the rows
reader = csv.DictReader(rows)

# Iterate over each row in the output
for row in reader:
  # Print out the hostname and IP address for the neighbor
  print(f'Hostname: {row["Device ID"]}')
  print(f'IP Address: {row["IP address"]}')
