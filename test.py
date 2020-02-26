import glob
import sys
import re
import os

# data = glob.glob(r"D:\120event\txt_test/*.txt")
data = glob.glob(r"D:\120event\export\txt_readable/*.txt")
savePath = r'D:\\Coding\KaoCleansing\txt_edited'

# fw = open("gyou.txt", "w")

#ファイル名を職員番号にする
def numberNS(n):
    number_regex = re.compile(r'\d{5}')
    mo = number_regex.search(n)
    nn = mo.group()
    return nn

def saveedittext(n, r, count):
    kaoFile = open( savePath + "\\" + str(n) +'.txt', 'w')
    for j in range(count + 1, len(r)):
        kaoFile.write(r[j])
    kaoFile.close()

noGenzaiList = []
# ファイルの数だけ処理を実行
for file in data:
    # ファイル名から職員番号を抽出
    syokuinNumber = numberNS(file)
    print("----------職員番号は「{0}」です----------".format(syokuinNumber))

    # 一行ずつ読み込む処理
    f = open(file, "r")
    lines = f.readlines()
    count = 0
    gyou = []
    for i in range(len(lines)):
        gen_regex = re.compile(r'\現在|\現 在|\現  在|\現　在')
        findText = gen_regex.findall(lines[i])
        if findText:
            # print(findText)
            count += 1
            gyou.append(i)
   
    # 現在のカウント数の判定
    if count == 0:
        print("この文には現在という単語が含まれていません")
        noGenzaiList.append(syokuinNumber)
    elif count == 1:
        # print("正常")
        saveedittext(syokuinNumber, lines, gyou[0])
    else:
        # pc = ("この文章には現在という単語が「{0}」個含まれています。").format(len(gyou))
        saveedittext(syokuinNumber, lines, gyou[0])
        # print(pc)
        # print(gyou)
    f.close()

print(noGenzaiList)
# print("---終了。現在が異常検出された職員番号の総数は{0}個です---".format(count))

# fw.close()