from netmiko import ConnectHandler

ip_list = ["192.168.1.101", "192.1.1.2"]
#ip_list = ["192.168.1.101", "192.1.1.2"]

send_config_commands = ["ip ssh password-auth"]
send_write_memory = "conf t"


def ssh_begin():

    for devices in ip_list:
        print(devices)
        device = ConnectHandler(
            ip=devices, username="admin", password="aBH8PUPtGr8AEjxYTMarqg59CTQB", device_type="cisco_s300"
        )
        print(device.find_prompt())
        print(device.send_command(send_write_memory))
        print(device.send_config_set(send_config_commands))

if __name__ == "__main__":
    ssh_begin()