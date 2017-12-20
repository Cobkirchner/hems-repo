import subprocess
import os

os.chdir("/terrform/")

current_directory = os.getcwd()
print ('current_directory')
subprocess.call(["terraform", "apply"])