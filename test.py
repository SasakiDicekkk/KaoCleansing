import glob
import sys
import re

# data = glob.glob(r"D:\ceremony\txt_test/*.txt")
data = glob.glob(r"D:\ceremony\txt_honban/*.txt")

fw = open("gyou.txt", "w")

#ファイル名を職員番号にする
def numberNS(n):
    number_regex = re.compile(r'\d{5}')
    mo = number_regex.search(n)
    nn = mo.group()
    return nn

def containedgenzai(f):
    gen_regex = re.compile(r'\現在|\現 在|\現  在|\現　在')
    # gen_regex = re.compile(r'\現.*在')
    mo = gen_regex.search(f)
    mo == True
    if mo:
        print(len(mo.group()))
    return mo
    # delSpace = f.replace(("　"), "")
    # if ('現在' in delSpace) or ('現 在' in delSpace):
    #     return True

count = 0
for file in data:

    f = open(file, "r")

    #ファイル名から職員番号を抽出
    syokuinNumber = numberNS(file)

    fw.write(syokuinNumber)
    
    print("----------職員番号は「{0}」です----------".format(syokuinNumber))

    fdata = f.read()  #ファイル終端まで読んだデータを返す
    boolGenzai = containedgenzai(fdata)
    #print(boolGenzai)
    if not boolGenzai:
        print("---{0}は現在が含まれていません---".format(syokuinNumber))
        count += 1

    # lines = fdata.split("\n")
    # f.close()


    #print("----------改行数は{0}です----------".format(len(lines1)))
    # noGenzai = []
    # for i in range(len(lines)):
    #     editText = lines[i].replace("　", "")
    #     if (("現 在") in editText) or (("現在") in editText) or (("現  在") in editText):
    #         noGenzai.append(i)
    #         break

        #     print(editText)
        # else:
        #     print("aru")
        # print("---区切り---")
        # print(line)
        # if (len(line) > 2):  #文字列が数値より大きいとき
        #     countLength = len(editText)
        #     scountLength = str(countLength)
        #     #print(countLength)
        #     fw.write(scountLength + ",")
        #     #print(editText)
        #     if (line.find("現在") == True):
        #         print(line)
        #         # print(line)

    # try:
    #     if noGenzai[-1] == 0:
    #         print("現在がない職員番号は「{0}」です".format(syokuinNumber))
    # except IndexError:
    #     print("現在がない職員番号は「{0}」です".format(syokuinNumber))
    fw.write("\n")

print("---現在が含まれていない職員番号の総数は{0}個です---".format(count))

fw.close()