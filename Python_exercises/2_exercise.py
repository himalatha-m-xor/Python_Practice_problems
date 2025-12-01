import re

f=open("feature.log","r")
data=f.readlines()
f.close()

dbg=open("debug.log","w")
err=open("error.log","w")
crt=open("critical.log","w")

for line in data:
    if re.search(r"(DEBUG)",line):
        dbg.write(line)
    elif re.search(r"(ERROR)",line):
        err.write(line)
    elif re.search(r"(CRITICAL)",line):
        crt.write(line)

dbg.close()
err.close()
crt.close()