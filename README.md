# netConBackup Script

This script is written in Python and automates the backup of all switches, routers, and firewalls in our environment.  The **netConBackup.py** script checks to see what role the device is designated as in the **deviceList.csv** file and backs it up appropriately.  Details about each device are stored in **deviceList.csv** in the format *Hostname, IP, Role*.

## Basic Script Functionality
The script connects via SSH to each device, runs the *"show run"* command, then saves the output to a file.  This is repeated for each entry in the **deviceList.csv** file.  

## Netmiko
The script uses a library called **Netmiko** created by **[Kirk Byers](http://github.com/ktbyers/)** that simplifies **[Paramiko](http://www.paramiko.org/)** SSH connections to network devices.  The Github repository for **[Netmiko](http://github.com/ktbyers/netmiko)** contains all the documentation required to implement it yourself.