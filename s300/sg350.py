#!/usr/bin/python3

from netmiko import Netmiko, ConnectHandler, NetmikoTimeoutException
from getpass import getpass
from discord import Webhook, RequestsWebhookAdapter
import fastapi
import requests
import emoji
import pprint

webhook_url = "https://discord.com/api/webhooks/628541226047504384/PUG68jxKCo56kJ3O2LIIbskz1hWI2t4-6KvKgmDyeaqVeRfQlERmA8VQfGhmFAVWFeUt"

webhook = Webhook.from_url(webhook_url, adapter=RequestsWebhookAdapter())

cisco_switch = {
    "host": "192.168.1.101",
    "username": "",
    "password": "",
    "device_type": "cisco_s300"
}
connection = Netmiko(**cisco_switch)

with ConnectHandler(**cisco_switch) as net_connect:
    output = net_connect.send_command("show ip interface brief", use_genie=True)
print()
pprint(output)
print()

def add_vlans():
    connection = Netmiko(**cisco_switch)
    add_vlans = connection.send_config_set(['vlan 10,20,30,40,50,60'])
    webhook.send(add_vlans)

def show_vlan():
    connection = Netmiko(**cisco_switch)
    show_vlan = connection.send_command("show vlan")
    webhook.send(show_vlan)

def show_sntp_server():
    show_sntp_server = connection.send_command("show sntp status")
    webhook.send(show_sntp_server)

def show_ip_route():
    show_ip_route = connection.send_command("show ip route")
    webhook.send(show_ip_route)

def show_arp():
    show_arp = connection.send_command("show arp")
    webhook.send(show_arp)

def show_version():
    show_version = connection.send_command("show version")
    webhook.send(show_version)

def show_system():
    show_system = connection.send_command("show system")
    webhook.send(show_system)

def show_inventory():
    show_inventory = connection.send_command("show inventory")
    webhook.send(show_inventory)

def show_hosts():
    show_hosts = connection.send_command("show hosts")
    webhook.send(show_hosts)

def show_interfaces():
    show_interfaces = connection.send_command("show interfaces")
    webhook.send(show_interfaces)

# def enable_ospf():
#     commands = ['router ospf 1',
#             'network 10.0.0.0 0.255.255.255 area 0',
#             'network 192.168.1.0 255.255.255.0 area 1']

#     enable_ospf = connection.send_config_set(commands)
#     webhook.send(enable_ospf)

def show_internal_bridge():
    show_internal_bridge = connection.send_command('show ip int br')
    webhook.send(show_internal_bridge)

def save_switch_config():
    #todo hostname & ip_address regex from 
    save_switch_config = connection.send_command("show running-config")
    config = open("hostname.txt","w")
    config.write(save_switch_config)
    config.close()

def show_ip_interface_summary():
    show_interface_brief = connection.send_command("show ip interface summary")
    webhook.send(show_interface_brief)

# def allow_ssh_password_auth():
#     allow_ssh_password_auth = connnection.send_config_set(['ip ssh password-auth'])
#     webhook.send(allow_ssh_password_auth)
    webhook.send(emoji.emojize(':thumbs_up:'))

    connection.disconnect()

if __name__ == "__main__":
    connection = Netmiko(**cisco_switch)
    show_vlan()
    show_internal_bridge()
    show_sntp_server()
    show_ip_route()
    show_arp()
    show_version()
    show_inventory()
    show_hosts()
    show_interfaces()
    save_switch_config()