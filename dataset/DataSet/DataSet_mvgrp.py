#encoding=utf8
import re, os, sys
for reldirx, _lidir in (
        (os.path.split(os.path.abspath(__file__))[0]+"/", []), # 这个先，规避加载漏洞。
        (os.path.split(os.path.abspath("."))[0]+"/", [])):
    while not _lidir and len(reldirx) > 3: # 3 应该所有平台都问题不大。
        reldirx = os.path.split(reldirx)[0] # 只尝试 funclib.py，funclib.pyc 存在版本。
        _checkfunc = lambda idir: os.path.exists(reldirx+idir+"/pythonx/funclib.py")
        _lidir = [reldirx+idir for idir in os.listdir(reldirx) if _checkfunc(idir)]
        assert len(_lidir) in (0, 1), _lidir
        if _lidir: reldirx = os.path.abspath(_lidir[0])
        del _checkfunc
    if _lidir: break
if not reldirx in sys.path: sys.path.append(reldirx) # 放到最后，避免 sys.path.insert
del _lidir # reldirx 可以继续使用

from pythonx.funclib import *

import shutil

def mysplit(rootdir, count):
    for i in range(count):
        tdir = "{}-{}".format(rootdir, i)
        if not os.path.exists(tdir):
            os.makedirs(tdir)
            
        destination = os.path.join("{}-{}".format(rootdir, i))
        tmp = os.path.relpath(destination, ".")
        print([tmp, tmp], ",")
            
    for ifile in os.listdir(rootdir):
        source = os.path.join(rootdir, ifile)
        i = int("".join(re.findall("[0-9]+", ifile)), 10) % count
        destination = os.path.join("{}-{}".format(rootdir, i), ifile)
        print(ifile, "{}-{}".format(rootdir, i))
        shutil.move(source, destination)

@CUR_DIR_RUN(r"G:\BaiduNetdiskDownload\所有数据集一起压缩\merge\merge~")
def main():
    rootdir = r"G:\BaiduNetdiskDownload\所有数据集一起压缩\merge\merge~\dataset\DataSet\Chinese_dataset\images"
    mysplit(rootdir, 10) # 每个大概 10 万。
    
    rootdir = r"G:\BaiduNetdiskDownload\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images"
    mysplit(rootdir, 36) # 每个大概 10 万。

if __name__ == "__main__":
    main()
    