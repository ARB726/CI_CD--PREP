import subprocess
import sys


result=subprocess.run(["python","--version"],capture_output=True,text=True)
print(result.stdout)
if result.stdout=="Python 3.9.25\n":
        print("TEST PASSED")
        sys.exit(1)
print("TEST FAILED PLAYING WITH PYTHON VERSIONS")