from netmiko import ConnectHandler # Import the ConnectHandler method from the Netmiko library
from credentials import * # Import device account credentials
# Import sys, csv, os, and datetime libraries for basic file handling and getting the date
import sys
import os
import csv
import datetime

# Assign the current date and time into a variable called rawTime, then use the strftime() method to
# parse a formatted string (dd-mm-yy) into a variable called today
rawTime = datetime.datetime.now()
today = rawTime.strftime("%d-%m-%Y")

# Open the file deviceList.csv and put each row into a list called deviceList, each row
# contains a tuple that is the (hostname, ip, role)
with open("deviceList.csv") as csv_file:
    deviceList = [tuple(line) for line in csv.reader(csv_file)]

# Print the list that was imported from the CSV file.  This can be commented out if it's not needed
for entry in deviceList:
    print(*entry)

# Create a new directory on a network share with the current date
directory = "//localhost/c$/Projects/netConBackup/SCRIPTS/Python/netConBackup/" + today + "/"
os.mkdir(directory)

# For loop to iterate over each key:value pair in the deviceList dictionary 
for hostname, IP, role in deviceList:
    # Initialize a dictionary called device and populate key:value pairs that are needed for Netmiko
    # to establish the SSH connection.  Credentials are imported above
    device = {
        'device_type': role,
        'ip': IP,
        'username': username,
        'password': password,
        'secret': secret,   
    }
    try:
        print("\nConnecting to Device",IP)
        # Create a variable called net_connect and pass the device dictionary into it
        net_connect = ConnectHandler(**device)
        # Enter priveleged exec (enable) mode on the device
        net_connect.enable()
        print("Reading the running config ")
        # Store the output of the "show run" command into a variable named output
        output = net_connect.send_command('show run')
        # Set the filename to be used for this device using the hostname and today's date
        filename = hostname + '_' + today + ".txt"
        # Create a file and open it in the location (directory variable above), w+ overwrites existing files
        saveconfig = open(directory + filename,'w+')
        print("Writing configuration to file")
        # Write the output from the "show run" command to the file variable "saveconfig" we opened in the previous line
        saveconfig.write(output)
        # Close the "saveconfig" file
        saveconfig.close()
        # Disconnect the netmiko SSH session
        net_connect.disconnect()
        print("Configuration saved to file",filename)
    except:
        # If the connection fails, catch the exception and print an error message
        print("Access to " + IP + " failed, no backup created.")

print("\nAll device backups complete")