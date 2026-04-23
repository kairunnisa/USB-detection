# USB Security Monitoring System

## Description
This project detects unauthorized USB device usage in Windows systems.

## Technologies
- Python
- WMI
- SQLite
- Windows Event Logs

## Features
- Real-time monitoring
- Whitelist checking
- Alert generation
- Database logging

## Run

```bash
python main.py
---

# How It Works

```text
USB Inserted
↓
System Detects Device
↓
Checks Authorized List
↓
Authorized → Allow
Unauthorized → Log + Alert
