#!/usr/bin/env python3

import psutil
import os

def get_cpu_info():
    cpu_count = os.cpu_count()
    cpu_percentage = psutil.cpu_percent(interval=1)
    cpu_stats = psutil.cpu_stats()
    cpu_freq = psutil.cpu_freq()
    cpu_load = os.getloadavg()
    
    return {
        "CPU_Count": cpu_count,
        "CPU_Percent": cpu_percentage,
        "CPU_Stats": cpu_stats,
        "CPU_Freq": cpu_freq,
        "CPU_Load": cpu_load,
    }

def main():
    from pprint import pprint
    pprint(get_cpu_info())

if __name__ == "__main__":
    main()