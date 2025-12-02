import paramiko,time,re

HOST="10.81.1.116"
USER="interns"
PASS="123123"

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST,username=USER,password=PASS)

sh=ssh.invoke_shell()

def send(cmd):
    sh.send(cmd+"\n")
    time.sleep(1)
    return sh.recv(10000).decode()

print("Monitoring Started...\n")

while True:
    cpu=send("top -bn1 | head -5")
    mem=send("free -m")
    disk=send("df -h | tail -1")

    cpu_val=re.search(r"(\d+\.\d+)\s*id",cpu)
    cpu_used=100-float(cpu_val.group(1)) if cpu_val else 0

    disk_val=re.search(r"(\d+)%",disk)
    disk_used=int(disk_val.group(1)) if disk_val else 0

    print("CPU:",cpu_used,"%  Disk:",disk_used,"%")

    if cpu_used>80 or disk_used>90:
        with open("alerts.log","a") as f:
            f.write(f"ALERT CPU={cpu_used}% DISK={disk_used}%\n")

    time.sleep(5)
