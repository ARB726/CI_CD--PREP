import subprocess
import sys


result=subprocess.run(["python","--version"],capture_output=True,text=True)
print(result.stdout)
if result.returncode!=0:
    print("TEST FAILED")
    sys.exit(1)
print("TEST PASSED")