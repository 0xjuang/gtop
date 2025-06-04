#!/usr/bin/env python3

import psutil

def get_io_info():
    disk_partitions_raw = psutil.disk_partitions()
    disk_partitions= []
    disk_usage= {}

    for part in disk_partitions_raw:
        partition_info = {
            "Device": part.device,
            "Mountpoint": part.mountpoint,
            "FSType": part.fstype,
            "Opts": part.opts,
        }
        disk_partitions.append(partition_info)
        try:
            usage = psutil.disk_usage(part.mountpoint)
            disk_usage[part.mountpoint] = {
                "Total": usage.total,
                "Used": usage.used,
                "Free": usage.free,
                "Percent": usage.percent,
            }
        except PermissionError:
            continue
    
    disk_counter = psutil.disk_io_counters(perdisk=True)
    return {
        "Disk_Partitions": disk_partitions,
        "Disk_Usage": disk_usage,
        "Disk_Counter": disk_counter,
    }

def main():
    from pprint import pprint
    pprint(get_io_info())

if __name__ == "__main__":
    main()