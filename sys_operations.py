import platform
import socket
import os

print("Machine type:", platform.machine())
print("Processor:", platform.processor())

socket.setdefaulttimeout(50)
print("Default socket timeout:", socket.getdefaulttimeout())

print("Operating System:", os.name)
print("Current Process ID:", os.getpid())

print("\n--- Fork Process ---")

if hasattr(os, "fork"):
    pid = os.fork()

    if pid == 0:
        print("Child Process ID:", os.getpid())
    else:
        print("Parent Process ID:", os.getpid())
else:
    print("Fork not supported on this system")


print("\n--- File Descriptor Practice ---")

fd = os.open("fdpractice.txt", os.O_CREAT | os.O_RDWR)

os.write(fd, b"Some string to write to the file")

if hasattr(os, "fork"):
    pid = os.fork()

    if pid == 0:
        print("Child PID:", os.getpid())
        os.lseek(fd, 0, 0)
        data = os.read(fd, 100)
        print("Child read:", data.decode())
        os.close(fd)
        os._exit(0)
    else:
        print("Parent PID:", os.getpid())
        os.wait()
        os.close(fd)