import subprocess
import re
from jinja2 import Environment, FileSystemLoader
def ping():
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "2", "1.1.1.1"],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0 and "time=" in result.stdout:
        after_time = result.stdout.split("time=", 1)[1]
        ping_ms = float(after_time.split()[0])
        return f"Ping: {ping_ms:.2f} ms"
    else:
        return "Ping: no reply"
ping()

def get_wifi_signal():
    result = subprocess.run(
        ["iw", "dev", "wlan0", "link"],
        capture_output=True,
        text=True,
    )

    match = re.search(r"signal:\s*(-?\d+)\s*dBm", result.stdout)
    if match:
        return int(match.group(1))

    return None