import docker
import subprocess
import time

client = docker.from_env()

def publish_mdns(name, ip):
    print(f"📣 Publishing {name}.local → {ip}")
    subprocess.Popen(["avahi-publish", "-a", name, ip])

def handle_container(container):
    try:
        name = container.name
        networks = container.attrs["NetworkSettings"]["Networks"]
        for net in networks.values():
            ip = net["IPAddress"]
            if ip:
                publish_mdns(name, ip)
    except Exception as e:
        print(f"[!] Error handling {container.name}: {e}")

# Başlarken tüm çalışanları yay
print("🚀 Publishing existing containers...")
for c in client.containers.list():
    handle_container(c)

# Docker event'lerini dinle
print("👂 Listening for new containers...")
for event in client.events(decode=True):
    if event["Type"] == "container" and event["Action"] == "start":
        try:
            container = client.containers.get(event["id"])
            handle_container(container)
        except Exception as e:
            print(f"[!] Event error: {e}")
