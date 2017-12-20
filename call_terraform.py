import subprocess
import os

os.chdir("/home/hems-repo/terrform")

current_directory = os.getcwd()
print ('current_directory')
subprocess.call(["terraform", "apply"])