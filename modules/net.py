#!/usr/bin/env python3

import psutil
import socket

def get_net_info():
    nic_data = {}
    net_addr = psutil.net_if_addrs()
    for nic_name, nic_info in net_addr.items():
        for addr in nic_info:
            if (
                addr.family == socket.AF_INET
                and addr.address
                and addr.address != "127.0.0.1"
            ):
                nic_data[nic_name] = addr.address
        
    net_stats = psutil.net_if_stats()
    net_io = psutil.net_io_counters()
    return {
        "Addresses": nic_data,
        "Stats": net_stats,
        "I/O": net_io,
    }


def main():
    from pprint import pprint
    pprint(get_net_info())

if __name__ == "__main__":
    main()