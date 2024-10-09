import os
import socket
import configparser

def send_wol(mac_address, ipv6_address):
    mac_bytes = bytes.fromhex(mac_address.replace(':', ''))
    magic_packet = b'\xff' * 6 + mac_bytes * 16
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.settimeout(5)
    sock.sendto(magic_packet, (ipv6_address, 9))
    print(f'WOL packet sent to {ipv6_address}.')

def create_default_config(filename):
    config = configparser.ConfigParser()
    config['WOL'] = {
        'mac_address': 'MAC地址',
        'ipv6_address': 'IPV6地址或链接(必须有对应IPV6地址)'
    }
    with open(filename, 'w') as configfile:
        config.write(configfile)
    print(f'Default config file {filename} created.')

if __name__ == "__main__":
    config_file = 'config.ini'
    
    # 检查配置文件是否存在
    if not os.path.exists(config_file):
        create_default_config(config_file)

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(config_file)

    mac = config.get('WOL', 'mac_address')
    ipv6 = config.get('WOL', 'ipv6_address')

    send_wol(mac, ipv6)
