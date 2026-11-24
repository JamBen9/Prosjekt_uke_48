import subprocess

result = subprocess.run(
    ["ping", "-c", "1", "-W", "2", "1.1.1.1"],
    capture_output=True,
    text=True,
    timeout=5,
)

if result.returncode == 0:
    print(result.stdout)
else:
    print("Ping failed:")
    print(result.stderr or result.stdout)