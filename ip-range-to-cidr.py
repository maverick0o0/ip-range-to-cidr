import sys
import ipaddress


def convert_ip_range_to_cidr(start_ip, end_ip):
    start_ip_obj = ipaddress.ip_address(start_ip)
    end_ip_obj = ipaddress.ip_address(end_ip)

    cidr_list = list(ipaddress.summarize_address_range(start_ip_obj, end_ip_obj))
    cidr_notation = [str(cidr) for cidr in cidr_list]

    return cidr_notation


def convert_ip_list_to_cidr(ip_list):
    cidr_notation = []

    with open(ip_list, 'r') as file:
        ips = file.read().splitlines()

    for ip_range in ips:
        start_ip, end_ip = ip_range.split('-')
        cidr_notation.extend(convert_ip_range_to_cidr(start_ip.strip(), end_ip.strip()))

    return cidr_notation


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Invalid number of arguments!')
        print('Usage: python3 convert_to_cidr.py startIp endIp')
        print('       python3 convert_to_cidr.py -list listIps.txt')
        sys.exit(1)

    if sys.argv[1] == '-list':
        ip_list_file = sys.argv[2]
        cidr_results = convert_ip_list_to_cidr(ip_list_file)
    else:
        start_ip = sys.argv[1]
        end_ip = sys.argv[2]
        cidr_results = convert_ip_range_to_cidr(start_ip, end_ip)

    if not cidr_results:
        print('No CIDR notation found.')
    else:
        for cidr in cidr_results:
            print(cidr)
