#!/usr/bin/env python3
"""
Day 1: Cross-platform system information collector
Works on Windows, Mac, and Linux
"""

import platform
import os
import json
from datetime import datetime

def get_system_info():
    """Collect system information"""
    info = {
        "timestamp": datetime.now().isoformat(),
        "platform": platform.system(),
        "platform_release": platform.release(),
        "platform_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "hostname": platform.node(),
        "python_version": platform.python_version(),
        "user": os.environ.get('USER', os.environ.get('USERNAME', 'unknown')),
        "home_directory": os.path.expanduser('~')
    }
    
    # Platform-specific info
    if platform.system() == 'Darwin':  # macOS
        info['platform_detail'] = 'macOS (M1)' if 'arm64' in platform.machine() else 'macOS (Intel)'
    elif platform.system() == 'Linux':
        info['platform_detail'] = 'Linux (WSL2)' if 'microsoft' in platform.release().lower() else 'Linux'
    elif platform.system() == 'Windows':
        info['platform_detail'] = 'Windows'
    
    return info

def main():
    """Main function"""
    print("=== Infrastructure Journey: Day 1 ===")
    print("System Information Collector\n")
    
    info = get_system_info()
    
    # Display info
    for key, value in info.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    # Save to file
    filename = f"system_info_{info['platform']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(info, f, indent=2)
    
    print(f"\nInfo saved to: {filename}")

if __name__ == "__main__":
    main()
