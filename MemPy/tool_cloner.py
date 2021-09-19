import os
import subprocess
import requests
from subprocess import PIPE


f = open("ToolsClone.txt", "r")
for linea in f:
    proceso= subprocess.run("ls", stdout=PIPE,stderr=PIPE)
    print(proceso.stdout)

f.close()