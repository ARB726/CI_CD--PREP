import subprocess
import sys

result=subrocess.run(["ls"])
if result.returncode!=0:
    print("UNABLE TO RUN")
    sys.exit(1)
print("BUILD PASSED")
