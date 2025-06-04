

# gTOP

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/status-alpha-lightgrey.svg)]()

Originally designed for use in automation and orchestration pipelines, **gTOP** enables lightweight system snapshots during provisioning or monitoring of orchestrated systems.

---

### Overview

**gTOP** is a modular Python tool that provides a real-time snapshot of system metrics in a structured and readable format. It reports information on:

- Hostname, OS, and kernel  
- CPU load, frequency, and utilization  
- Memory usage and availability  
- Disk partitions and usage  
- Network interface data and I/O

---

### Features

`[POSIX-friendly]` Designed to work seamlessly in Unix-like environments, including headless servers.  
`[Modular Design]` Each subsystem is decoupled into a module (CPU, Mem, I/O, Net) for easy extension.  
`[Automation Ready]` Originally designed for use in orchestration and provisioning pipelines.  
`[DevOps Compatible]` Built with clean stdout output for chaining, logging, or integration.  
`[Extensible Output]` Easy to extend for JSON formatting, CLI flag parsing, and logging.

---

### Usage

```bash
$ ./gtop.py
```

This prints a formatted snapshot of your system’s current state to stdout. All metrics are collected at runtime using `psutil` and the Python standard library.

---

### Project Structure

```text
gtop/
├── gtop.py           # Main entry script
├── modules/
│   ├── cpu.py        # CPU metrics
│   ├── mem.py        # Memory metrics
│   ├── io.py         # Disk I/O and partition info
│   └── net.py        # Network stats
└── README.md         # Project documentation
```

Each module exposes a `get_<subsystem>_info()` function that returns a dictionary of structured metrics.

---

### Example Output

```text
========== gTOP SYSTEM SNAPSHOT ==========
Hostname    : dev-vm
Uptime      : 1d 3h 42m
OS          : Linux
Kernel      : 6.6.12-arch1-1
------------------------------------------

[ Memory ]
Total       : 7.67 GB
Used        : 4.12 GB
Free        : 2.21 GB
Available   : 3.45 GB
Usage       : 53.7%
------------------------------------------

[ CPU ]
Logical     : 4
Physical    : 2
Usage       : 12.8%
Load Avg    : 0.57, 0.89, 1.22
------------------------------------------

[ Disk ]
Mount       : /
Type        : ext4
Total       : 50.00 GB
Used        : 20.42 GB
Free        : 27.89 GB
Usage       : 42.0%
------------------------------------------

[ Network ]
Interface   : eth0
IP Address  : 192.168.0.100
Sent        : 85.23 MB
Received    : 124.67 MB
------------------------------------------

Snapshot Timestamp : 2025-06-04 18:14:32
==========================================
```

---

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/0xjuang/gtop.git
   cd gtop
   ```

2. Install dependencies:
   ```bash
   pip install psutil
   ```

3. Run the snapshot tool:
   ```bash
   ./gtop.py
   ```

---

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.

---

### Author

**Juan J Garcia**  
GitHub: [@0xjuang](https://github.com/0xjuang)  
Email: juan@gg3.dev