import zipfile
import datetime
import time

fp = "/tmp/a.zip"
s = 1865689000
zf = zipfile.ZipFile(fp, "r")
data = {}
for ff in zf.filelist:
    k = ff.filename.lstrip("flag/").rstrip(".txt")
    dt = datetime.datetime(*ff.date_time[0:])
    ts = dt.timestamp()
    print(ts)
    v = ts - s
    data[str(k)] = v
for i in range(27):
    v = data.get(str(i))
    print(chr(int(v)+1), end="")