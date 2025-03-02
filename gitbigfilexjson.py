#encoding=utf8
import re, os, sys
from pathlib import Path
for reldirx, _lidir in (
        (os.path.dirname(os.path.abspath(__file__)), []), # 这个先，规避加载漏洞。
        (os.path.dirname(os.path.abspath(".")), [])):
    while not _lidir and len(reldirx) > 3: # 3 应该所有平台都问题不大。
        reldirx = os.path.dirname(reldirx) # 只尝试 funclib.py，funclib.pyc 存在版本。
        _checkfunc = lambda idir: os.path.exists(os.path.join(reldirx, idir, "pythonx", "funclib.py"))
        _lidir = [os.path.join(str(Path(os.path.join(reldirx, idir, "pythonx")).resolve()), "..")
                    for idir in os.listdir(reldirx) if _checkfunc(idir)]
        assert len(set(_lidir)) in (0, 1), _lidir
        if _lidir: reldirx = os.path.abspath(_lidir[0])
        del _checkfunc
    if _lidir: break
for _lidir in [r"E:\kSource", r"D:\kSource", r"C:\kSource"]:
    if not os.path.exists(os.path.join(reldirx, "pythonx", "funclib.py")):
        reldirx = _lidir
if not reldirx in sys.path: sys.path.append(reldirx) # 放到最后，避免 sys.path.insert
del _lidir # reldirx 可以继续使用
from pythonx.funclib import *


page = r"""
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\Art\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\BdCnScene\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\COCO_Text\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Chinese_dataset\images-0\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Chinese_dataset\images-1\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Chinese_dataset\images-2\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Chinese_dataset\images-3\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Chinese_dataset\images-4\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Chinese_dataset\images-5\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Chinese_dataset\images-6\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Chinese_dataset\images-7\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Chinese_dataset\images-8\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Chinese_dataset\images-9\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\config\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-0\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-1\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-10\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-11\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-12\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-13\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-14\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-15\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-16\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-17\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-18\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-19\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-2\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-20\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-21\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-22\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-23\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-24\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-25\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-26\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-27\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-28\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-29\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-3\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-30\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-31\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-32\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-33\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-34\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-35\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-4\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-5\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-6\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-7\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-8\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\DataSet\Synthetic_Chinese_String_Dataset\images-9\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\icdar2015\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\icdar2017rctw\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\LSVT\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1001~1050\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\101~150\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1051~1100\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1101~1150\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1151~1200\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1201~1250\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1251~1300\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1301~1350\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1351~1400\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1401~1450\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1451~1500\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1501~1550\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\151~200\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1551~1600\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1601~1650\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1651~1700\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1701~1750\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1751~1800\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1801~1850\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1851~1900\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1901~1950\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1951~2000\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\1~50\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2001~2050\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\201~250\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2051~2100\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2101~2150\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2151~2200\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2201~2250\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2251~2300\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2301~2350\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2351~2400\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2401~2450\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2451~2500\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2501~2550\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\251~300\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2551~2600\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2601~2650\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2651~2700\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2701~2750\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2751~2800\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2801~2850\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2851~2900\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2901~2950\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\2951~3000\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\301~350\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\351~400\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\401~450\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\451~500\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\501~550\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\51~100\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\551~600\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\601~650\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\651~700\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\701~750\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\751~800\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\801~850\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\851~900\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\901~950\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth\imgs\951~1000\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mjsynth_cfg\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\mlt2019\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\MTWI2018\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\ReCTS\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\SROIE2019\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\SynthText800k\datamap.txt
I:\ocr_data\所有数据集一起压缩\merge\merge~\dataset\Art\datamap.txt.md5.txt"""

def mainidx(idxfile):
    idxdir = os.path.dirname(idxfile)
    gitroot = r"I:\ocr_data\所有数据集一起压缩\merge\merge~"
    reldir = os.path.relpath(idxdir, gitroot)
    submit_dir = reldir.replace("\\", "_")
    reldirb = os.path.relpath(gitroot, idxdir)
    #print("reldir", reldir)
    #print("reldirb", reldirb)
    
    true = True
    fjson = {
      "autopinyin": true,
      "copylist": [],
      "copylist_note": "上传前，须要拷贝的文件列表，每个的格式是：['fromfile', 'tofile']。",
      "datamaplist": [
        f"{reldir}\\datamap.txt"
      ],
      "ftpconfig": {
        "host": "10.12.172.128",
        "pass": "35218764",
        "pypass_upload": "OCRDATA_FTP_PASS_KEY",
        "user": "ftp_readonly",
        "user_upload": "ftp_readwrite"
      },
      "generate_listfile": true,
      "generate_versionfile": true,
      "gitremote": "data_for_ai",
      "gitremote_note": "远程根目录 'data_for_ai'。",
      "mainfile": f"{reldir}\\datamap.txt",
      "mainroot": "..\\..",
      "mynote": f"I: & cd {gitroot} & python3 E:/kSource/pythonx/gitbigfileftp.py /UploadLocal /NoTipInfo /NoCheckFile {reldir}",
      "others": [],
      "submit_dir": submit_dir,
      "timeout": 365,
      "timeout_note": "自动清理 365 天前的文件。",
      "timeout_reserved": 10000,
      "timeout_reserved_note": "不会清理最新的 10000 个文件夹（保底保留文件夹个数）。",
      "upload": {
        "comment": "这个节点是程序自动维护的，不要修改。上面的 'others' 字段支持配置文件夹。",
        "count": 55636,
        "others": []
      }
    }
    writefileJson(os.path.join(idxdir, "gitbigfilex.json"), fjson)
    print(fjson["mynote"])
        
def main():
    idxlist = page.strip().split("\n")
    for idxfile in idxlist:
        mainidx(idxfile)

if __name__ == "__main__":
    main()
    print("ok")