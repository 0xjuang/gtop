#!/usr/bin/env python3

import psutil

def get_mem_info():
    v_mem = psutil.virtual_memory()
    return {
        "Total": v_mem.total,
        "Available": v_mem.available,
        "Used": v_mem.used,
        "Free": v_mem.free,
        "Percent": v_mem.percent,
    }

print(get_mem_info())