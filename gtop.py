#!/usr/bin/env python3
"""
gtop.py - Lightweight System Snapshot Tool
==========================================

gTOP provides a one-glance summary of system health by aggregating and printing
vital metrics from CPU, memory, disk, and network subsystems. It is designed
for terminal use and modular enough to be extended into a full monitoring suite.

Author: Juan J. Garcia (@0xjuang) <juan@gg3.dev>

Dependencies:
-------------
- Python 3.6+
- `psutil` for hardware/system metrics
- `platform`, `socket`, `time` from stdlib
- `modules/` directory containing:
    - cpu.py with get_cpu_info()
    - mem.py with get_mem_info()
    - io.py  with get_io_info()
    - net.py with get_net_info()

Sample Usage:
-------------
$ ./gtop.py
"""

__version__ = "0.1.0"

# ──[ Standard Library Imports ]─────────────────────────────────────────────
from pprint import pprint  # Optional for debugging
import socket
import time
import platform
import psutil
import prettytable  # Optional for future tabular output

# ──[ Internal Module Imports ]──────────────────────────────────────────────
from modules import cpu, io, mem, net


def basic_snap() -> str:
    """
    Collect and format a real-time system snapshot.

    This function gathers data from internal modules and standard libraries to
    display an overview of system status, including:
    - Host and kernel details
    - Memory usage
    - CPU load and core count
    - Disk usage of the root partition
    - Network I/O and IP information

    Returns:
        str: A preformatted string ready for printing to console.
    """

    # ──[ Fetch Subsystem Data ]──────────────────────────────────────────────
    cpu_data = cpu.get_cpu_info()
    mem_data = mem.get_mem_info()
    disk_data = io.get_io_info()
    net_data = net.get_net_info()

    # ──[ System Metadata ]───────────────────────────────────────────────────
    hostname = socket.gethostname()
    os_name = platform.system()
    kernel = platform.release()
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time

    # ──[ Format Uptime ]─────────────────────────────────────────────────────
    uptime_days = int(uptime_seconds // 86400)
    uptime_hours = int((uptime_seconds % 86400) // 3600)
    uptime_minutes = int((uptime_seconds % 3600) // 60)
    uptime = f"{uptime_days}d {uptime_hours}h {uptime_minutes}m"

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # ──[ Memory Stats (in GB) ]──────────────────────────────────────────────
    mem_total = mem_data["Total"] / (1024**3)
    mem_used = mem_data["Used"] / (1024**3)
    mem_free = mem_data["Free"] / (1024**3)
    mem_available = mem_data["Available"] / (1024**3)
    mem_percent = mem_data["Percent"]

    # ──[ CPU Stats ]─────────────────────────────────────────────────────────
    cpu_logical = cpu_data["CPU_Count"]
    cpu_physical = cpu_data["CPU_Physical"]
    cpu_usage = cpu_data["CPU_Percent"]
    cpu_load = ", ".join(f"{x:.2f}" for x in cpu_data["CPU_Load"])

    # ──[ Disk Stats (root partition) ]───────────────────────────────────────
    disk_mount = disk_data["Disk_Partitions"][0]["Mountpoint"]
    disk_type = disk_data["Disk_Partitions"][0]["FSType"]
    disk_total = disk_data["Disk_Usage"]["/"]["Total"] / (1024**3)
    disk_used = disk_data["Disk_Usage"]["/"]["Used"] / (1024**3)
    disk_free = disk_data["Disk_Usage"]["/"]["Free"] / (1024**3)
    disk_percent = disk_data["Disk_Usage"]["/"]["Percent"]

    # ──[ Network Stats ]─────────────────────────────────────────────────────
    net_iface = list(net_data["Addresses"].keys())[0]
    net_ip = list(net_data["Addresses"].values())[0]
    net_sent = net_data["I/O"][0] / (1024**2)
    net_received = net_data["I/O"][1] / (1024**2)

    # ──[ Output Formatting ]─────────────────────────────────────────────────
    output = f"""
========== gTOP SYSTEM SNAPSHOT ==========
Hostname    : {hostname}
Uptime      : {uptime}
OS          : {os_name}
Kernel      : {kernel}
------------------------------------------

[ Memory ]
Total       : {mem_total:.2f} GB
Used        : {mem_used:.2f} GB
Free        : {mem_free:.2f} GB
Available   : {mem_available:.2f} GB
Usage       : {mem_percent}%
------------------------------------------

[ CPU ]
Logical     : {cpu_logical}
Physical    : {cpu_physical}
Usage       : {cpu_usage}%
Load Avg    : {cpu_load}
------------------------------------------

[ Disk ]
Mount       : {disk_mount}
Type        : {disk_type}
Total       : {disk_total:.2f} GB
Used        : {disk_used:.2f} GB
Free        : {disk_free:.2f} GB
Usage       : {disk_percent}%
------------------------------------------

[ Network ]
Interface   : {net_iface}
IP Address  : {net_ip}
Sent        : {net_sent:.2f} MB
Received    : {net_received:.2f} MB
------------------------------------------

Snapshot Timestamp : {timestamp}
==========================================
"""
    return output


# ──[ Entry Point ]───────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(basic_snap())
