import os, threading, hashlib

FILE = "10mb-examplefile-com.txt"
OUT = "parts"
MERGED = "final.txt"
SIZE = 1024 * 1024

os.makedirs(OUT, exist_ok=True)

i = 0
with open(FILE, "rb") as f:
    while True:
        chunk = f.read(SIZE)
        if not chunk:
            break
        open(f"{OUT}/p{i}", "wb").write(chunk)
        i += 1

print("Split done:", i, "parts")

lock = threading.Lock()

def join(p):
    data = open(f"{OUT}/{p}", "rb").read()
    lock.acquire()
    open(MERGED, "ab").write(data)
    lock.release()

threads = []
for p in sorted(os.listdir(OUT)):
    t = threading.Thread(target=join, args=(p,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Merge done")

def md5(f):
    return hashlib.md5(open(f, "rb").read()).hexdigest()

print("Match" if md5(FILE) == md5(MERGED) else "Mismatch")
