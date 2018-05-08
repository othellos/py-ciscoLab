import netmiko
from netmiko import ConnectHandler
import paramiko
import socket

platform = 'cisco_ios'
hosts = open("testhosts.csv")
# hosts = ['10.100.1.50', '10.100.1.51', '10.100.1.252', '10.100.1.253']
# username = input("Username:")
username = 'TestLab'
# password = input("Password:")
password = 'Pa55w0rd'

def get_uptime():
    getuptime = device.send_command("sh hardware | inc uptime")
    print(getuptime)

def get_bootfile():
    getbootfile = device.send_command("sh ver | inc image")
    print(host + " " + getbootfile)

def set_user():
    setusername = ['username TestLab priv 15 password Pa55w0rd']
    output = device.send_config_set(setusername)
    print(output)

def write_mem():
    writemem = ['wr mem']
    output = device.send_command("wr mem")
    print("Config has been written for " + host)

def set_snmp():
    snmpsvr_add = '10.100.20.65'
    buildsnmp = ['no snmp-server',
                 'no access-list 13',
                 'access-list 13 permit ' + snmpsvr_add,
                 'logging host ' + snmpsvr_add,
                 'logging trap notifications',
                 'ip flow-export ver 9',
                 'ip flow-export dest ' + snmpsvr_add + ' 2055',
                 'snmp-server community TESTLAB RO 13',
                 'snmp-server location JacDC',
                 'snmp-server contact regret',
                 'snmp-server enable traps snmp authentication linkdown linkup coldstart warmstart',
                 'snmp-server enable traps tty',
                 'snmp-server enable traps eigrp',
                 'snmp-server enable traps bgp',
                 'snmp-server enable traps syslog',
                 'snmp-server host ' + snmpsvr_add + ' version 2c TESTLAB']
    output = device.send_config_set(buildsnmp)
    print(output)

for host in hosts:
    device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
    try:
        # get_uptime()
        # get_bootfile()
        # set_user()
        write_mem()
        # set_snmp()

    except:
        print("There was an error on " + host)
        pass