import subprocess
import os

os.chdir("/home/hems-repo/terraform/")

current_directory = os.getcwd()
print ('current_directory')
subprocess.call(["terraform", "apply"])