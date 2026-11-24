import subprocess

result = subprocess.run(
    ["ping", "-c", "1", "-W", "2", "1.1.1.1"],
    capture_output=True,
    text=True,
)

if result.returncode == 0 and "time=" in result.stdout:
    after_time = result.stdout.split("time=", 1)[1]
    ping_ms = float(after_time.split()[0])
    print(f"Ping: {ping_ms:.2f} ms")
else:
    print("No ping time available.")