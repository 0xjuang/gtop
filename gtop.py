#!/usr/bin/env python3

from modules import cpu, io, mem, net
from pprint import pprint
import prettytable
import socket
import time
import psutil
import platform


cpu_data = cpu.get_cpu_info()
mem_data = mem.get_mem_info()
disk_data = io.get_io_info()
net_data = net.get_net_info()


# pprint(cpu_data)
# pprint(mem_data)
# pprint(disk_data)
# pprint(net_data)


hostname = socket.gethostname()
os_name = platform.system()
kernel = platform.release()
boot_time = psutil.boot_time()
uptime_seconds = time.time() - boot_time

# Convert to days, hours, minutes
uptime_days = int(uptime_seconds // 86400)
uptime_hours = int((uptime_seconds % 86400) // 3600)
uptime_minutes = int((uptime_seconds % 3600) // 60)
uptime = f"{uptime_days}d {uptime_hours}h {uptime_minutes}m"

timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


print(f"""
========== gTOP SYSTEM SNAPSHOT ==========
Hostname    : {hostname}
Uptime      : {uptime}
OS          : {os_name}
Kernel      : {kernel}
------------------------------------------

[ Memory ]
Total       : 
Used        : 
Free        : 
Available   : 
Usage       : 
------------------------------------------

[ CPU ]
Logical     : 
Physical    : 
Usage       : 
Load Avg    : 
------------------------------------------

[ Disk ]
Mount       : 
Used        : 
Free        : 
Usage       : 
------------------------------------------

[ Network ]
Interface   : 
IP Address  : 
Sent        : 
Received    : 
------------------------------------------

Snapshot Timestamp : {timestamp}
==========================================
""")