import pathlib
from os import getenv


class Folder():
    def __init__(self):
        self.files: dict[str, int] = {}  # {"filename":filesize}
        self.directories: dict[str, Folder] = {}  # {"foldername": Folder}

    def add_file(self, filesize: int, filename: str):
        while filename in self.files:
            filename += " (copy)"
        self.files[filename] = filesize

    def add_folder(self, folder_name: str):
        if not folder_name in self.directories:
            self.directories[folder_name] = Folder()

    def get_size(self) -> int:
        total = sum(self.files.values())

        for child_dir in self.directories.values():
            total += child_dir.get_size()

        return total

    def __str__(self, level=1):
        output = f"- / (dir, size={self.get_size()})\n" if level == 1 else ""
        for name, directory in self.directories.items():
            output += ("  " * level) + \
                f"- {name} (dir, size={directory.get_size()}) \n"
            output += directory.__str__(level + 1)
        for filename, filesize in self.files.items():
            output += ("  " * level) + \
                f"- {filename} (file, size={filesize})\n"
        return output


# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process


def traverse_tree(tree: Folder, directories: list[str]) -> Folder:
    if len(directories) == 0:
        return tree
    next_directory = directories.pop()
    return traverse_tree(tree.directories[next_directory], directories)


def _format_dataset(dataset: "list[str]"):
    tree = Folder()
    current_location: list[str] = []
    for line in dataset[1:]:
        branch = traverse_tree(tree, [*current_location[::-1]])
        if line.startswith("$"):
            cmd = line[2:]

            # cd something
            if " " in cmd:
                folder_target = cmd[3:]
                if folder_target == "..":
                    current_location.pop()
                else:
                    current_location.append(folder_target)
                    branch.add_folder(folder_target)

        # parse ls line
        else:
            cmd, name = line.split()
            if cmd == "dir":
                branch.add_folder(name)
            else:
                branch.add_file(int(cmd), name)
    return tree


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)


if __name__ == "__main__":
    get_dataset()

"""
nrwjb 143562
qqvdcclf 78449
tvrms 116085
qqvdcclf 5693
tprth.gjn 235620
vrdrsj.fbl 82743
crswqlvd.nsj 94188
lbsfsspm 60078
nrwjb 74624
tjhcqw.wrq 247709
tvrms 267693
nrwjb 109072
qqvdcclf 31512
nrwjb 237917
vrdrsj.ntw 45489
smfzmmhc.zzd 185533
qqvdcclf 83589
hrvlgmjb.wrv 232123
rlf 137190
tghvbj.mfr 21785
vrdrsj.swp 25344
lgt 36125
lggpfj.gnr 128272
lrdq.zgm 146745
mwmlf.wnp 266383
pcdtdblc.znj 175784
wmstvdt.lhn 185424
ljslzhjl 141743
rlf 169015
fqtrpm.mqr 81450
jtbr 146399
qqvdcclf 288302
zmn.fjz 121112
czvpvwz 7858
tprth.gjn 150816
spbjrlv.spt 184385
zzhz 201578
nrwjb 47747
mwmlf 136682
lscdth.lbj 282363
qbpmcqs 273281
qdffbp 7547
tprth.gjn 223960
nrwjb 12361
pfvtwr.pbf 150218
sfhsszcq.tzv 158227
smfzmmhc.drh 183244
ldpfs.qhr 194008
nfqmvqcm.ftd 11099
zrtsd.jwg 153379
rlf.nlc 62076
smfzmmhc 102930
tjhcqw.wrq 185079
jzbvmc 61556
sgh 237487
tvrms 136126
tjhcqw.wrq 86537
smfzmmhc.shv 263122
tvrms 73772
zwdbh 220800
rlf 38282
rlf.blz 93306
nrwjb 21587
zvq.lvr 184621
zdmnm.wlc 82901
vrdrsj.zwc 75558
qqvdcclf 128171
rlf.hgt 245942
mwmlf 7382
zltjmn 285714
gttgwfgf.cpd 43731
jdhb.ssj 112018
rlf.gvd 195239
spsstb 200476
vrdrsj 116544
qqvdcclf 55892
fnrhmbbm.rnp 144766
tjhcqw.wrq 2622
tprth.gjn 219884
dhjv.pfn 153434
mcb.djg 26553
qqvdcclf 37741
mwmlf.vhs 13218
rggt 102602
rlnf.qrt 228549
mwmlf.lsv 17957
lfgh.jwg 40821
zmrpm.pqn 301639
tprth.gjn 294779
qst.zgc 37853
tjhcqw.wrq 230725
tvrms 2872
bph 214328
tjhcqw.wrq 138045
sllvfsf 62568
tjhcqw.wrq 286839
zvqrg.bsg 241004
tprth.gjn 116677
vtbt 151347
hrvlgmjb.wzz 97786
nrwjb 70534
qqvdcclf 292701
sjqvgh.nvt 153174
hrvlgmjb 63451
nrwjb 246754
gwcrpgc 283020
ltmzzz 36180
nscwcztf.wlh 51208
smfzmmhc 121548
mwmlf.fqd 263186
nrwjb 204801
rdrmctwg.nqc 116293
tjhcqw.wrq 36548
ctllrm 231615
jsm 135330
qqvdcclf 279734
tvrms 220762
vrdrsj.jqj 35964
frn.ccd 300636
jwvjslwp.vsp 267669
tvrms 180586
cgzmwg.rgr 169064
qgmmc.sqq 270729
shcpdlm.nwz 92811
qqvdcclf 301584
mwmlf.rvg 264911
svhwhw.fdp 32109
tjhcqw.wrq 155713
tvrms 32357
nrwjb 93501
mgrvcbjc.rqb 241812
nvrssljz 273819
tvrms 156873
wdfvctwp 133649
smfzmmhc 67552
dnbvw.zwd 132663
hrvlgmjb.fwh 293463
nrwjb 194357
tprth.gjn 56668
tvrms 303099
nrwjb 84952
rlf 192566
srzz 78478
tprth.gjn 250044
tvrms 97100
nrwjb 203375
qqvdcclf 39137
rtphln.pgc 1747
tjhcqw.wrq 163505
tprth.gjn 76891
hhtdhzgn 6853
pmsflvrn.hnh 158303
vrdrsj 263568
hqggp.lrq 12435
ntbcht.zbw 292141
qqvdcclf 118913
tjhcqw.wrq 291087
tjhcqw.wrq 263233
mwmlf.zss 3390
dbwsmwnb.svt 298839
tprth.gjn 170672
tld 193212
tprth.gjn 257122
lnrwrpjj 274740
ptzmfsmr.pwc 35217
qpdj.pfc 67549
jgstzhw.cbq 40279
mqfl.flt 126237
bngqncqn 53423
nrwjb 178935
tprth.gjn 188826
vrdrsj.svn 286449
jjvcgb.nwc 215281
tvrms 300004
mwmlf 19667
rbhz.plr 263985
smfzmmhc 254206
hrvlgmjb.bbf 250310
mwmlf.lbq 130543
hcnsgjhj 107472
rlf 303694
nrwjb 299875
mzhgbj.zvv 114118
tprth.gjn 273343
wgrp 28259
bvlv.npm 218927
hrf.czg 64283
qtb.fnb 103691
zjlgc.sfg 252712
hrvlgmjb.mtq 231583
nrwjb 264128
tvrms 257359
zzgr 237116
qqvdcclf 230613
smfzmmhc 91615
mwmlf.qtq 98708
fgh.djg 131293
lcwjtdf.sbl 125876
tvrms 263022
vrdrsj 276134
dndbj.gww 194315
lspnmhml.fdb 115061
tjhcqw.wrq 239758
wjcbcvfd 124732
tvrms 127542
lcl 33684
npvgs.qdw 203352
tvrms 6985
wmnrjw.chn 102991
wrcjmll.rlb 162852
mwmlf.vdw 84338
nrwjb 147349
chlgpdsp.hrv 265563
rlf 100762
sjvgwmdg.qhg 300872
tzqmh 164004
zhgmdcl.bfq 300736
rtt.qps 284520
smfzmmhc 263890
mcdjsms.zss 295429
tmf.ctw 41526
svdm 17063
tvrms 216391
hrvlgmjb 1835
mwmlf.sng 43155
ngjg.zmc 238089
bgfnqf 178768
qrrc.bbc 255854
smfzmmhc 178991
hrvlgmjb 70585
rmjzzgrs 43606
wthtcg.wgd 35098
qqvdcclf 19740
mwmlf 100360
fgthp.qmg 279143
gnclhrw.mwt 247595
pcdnbq.zbs 303125
tprth.gjn 38092
brcbr 37395
tjhcqw.wrq 94639
dnplntn.mwr 108141
lmfsgd 31100
lpbdq.vdp 263849
smfzmmhc.wsr 109813
nwszgpm.qqr 31933
rjqvhccg 106249
vgzqz 16766
mwmlf 19593
rggqjp.pnt 220657
tdgd.ppw 48210
tjhcqw.wrq 232603
grstm.ltj 202702
tvrms 258253
fwfzsc.pls 131860
thp 42452
vdjh.dct 284648
jdbdb 108335
ctwllbmc 237419
qqvdcclf 36570
smfzmmhc 92173
dtg.bvl 89469
mqrr 88361
fftpd 47472
qqvdcclf 53118
hnvqtbcn 98255
hgwh.tnl 29828
rdj.wrv 240042
clnbddrh.lbq 45192
ndzjnttr 105827
nmnr.lct 140925
tprth.gjn 238998
mnnr.smj 115973
zld.hzv 75630
phmvhpvb.fwh 302512
hrvlgmjb 13802
hrvlgmjb.nhn 228515
mwmlf 246019
mwmlf.nvm 9535
mwmlf 279877
zwwtflb 278221
cpzj 270197
tprth.gjn 197398
"""
