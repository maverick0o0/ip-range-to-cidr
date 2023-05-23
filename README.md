This tool converts an IP range to its corresponding CIDR.

Usage:

1. Clone the repository using the command: git clone `https://github.com/maverick0o0/ip-range-to-cidr.git`
2. Install the required packages using the command: `pip3 install -r requirements.txt`
3. Provide the start IP and end IP as arguments to the script using the command: `python3 ip-range-to-cidr.py 185.18.45.0 185.18.45.255` -> 185.18.45.0/24
4. Alternatively, provide a list of IP ranges as input using the command: python3 `ip-range-to-cidr.py -list list-of-ip-range.txt`

*For convenient use add this to .bashrc :
`alias ip-range-convertor="python3 ~/path/to/convert-ip-range-to-cidr.py"`
