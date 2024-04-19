#!/bin/python

from pwn import *

r = remote("localhost", 1337)
r.sendline(b"niteCTF{good_for_health_bad_for_education}")
output = r.recvall(timeout=0.1)
r.close()

if b"nite{Te" in output:
    print("works")
    exit(0)
exit(1)
