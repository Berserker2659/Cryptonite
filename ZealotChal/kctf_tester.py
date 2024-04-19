import os
import subprocess
from pwn import *
from time import sleep

CHAL_FOLDER_NAME = "rev_zealot"

RESTART = True
# RESTART = False

MAX_TRIES = 200

root = f"{os.getenv('HOME')}/Desktop/KCTF"

input_data = b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY!"


def start(port):
    try:
        r = remote("localhost", port)
        r.sendline(b"niteCTF{good_for_health_bad_for_education}")
        output = r.recvall(timeout=0.1)
        r.close()

        if b"nite{Te" in output:
            print("works")
        else:
            print("FAILED")

    except Exception:
        print("FAILED")


if RESTART:
    subprocess.call(
        f"source {root}/kctf/activate && cd {root}/{CHAL_FOLDER_NAME} && kctf chal stop && sleep 2",
        shell=True,
    )
    subprocess.call(
        f"source {root}/kctf/activate && cd {root}/{CHAL_FOLDER_NAME} && kctf chal start && sleep 5",
        shell=True,
    )

with subprocess.Popen(
    f"source {root}/kctf/activate && cd {root}/{CHAL_FOLDER_NAME} && kctf chal debug port-forward &",
    stdout=subprocess.PIPE,
    bufsize=1,
    universal_newlines=True,
    shell=True,
) as p:
    for line in p.stdout:
        if "Forwarding" in line:
            port = line.replace("Forwarding from 127.0.0.1:", "").split()[0]

            if RESTART:
                for i in range(10):
                    print(".", end="")
                    sleep(1)

            start(port)

            print(f"Listening at port: {port}")

            break
