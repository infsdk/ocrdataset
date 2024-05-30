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

@CUR_DIR_RUN(r"G:\BaiduNetdiskDownload\所有数据集一起压缩\merge\merge~")
def main():
    rootdir = r"dataset\mjsynth\imgs"
    for dir in os.listdir(rootdir):
        if os.path.isdir(os.path.join(rootdir, dir)):
            print([os.path.join(rootdir, dir), os.path.join(rootdir, dir)], ",")

    rootdir = r"dataset"
    for dir in os.listdir(rootdir):
        if os.path.isdir(os.path.join(rootdir, dir)):
            print([os.path.join(rootdir, dir), os.path.join(rootdir, dir)], ",")

def main2():
    rootdir = r"G:\BaiduNetdiskDownload\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs"
    
    for dir in os.listdir(rootdir):
        #print(dir)
        if re.findall("^[0-9]+$", dir):
            num = int(dir)
            #print(num)
            idx = (num - 1) // 50
            todir = "%d~%d" % (idx * 50 + 1, idx * 50 + 50)
            
            oldpos = os.path.join(rootdir, dir)
            newpos = os.path.join(rootdir, todir, dir)
            print(dir, os.path.join(todir, dir))
            shutil.move(oldpos, newpos)

        else:
            subdir = os.path.join(rootdir, dir)
            print(subdir, len(os.listdir(subdir)))
            assert len(os.listdir(subdir)) == 50

if __name__ == "__main__":
    main()
    