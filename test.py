import glob
import sys
# data = glob.glob("./txt_test/*.txt")
data = glob.glob("./txt_honban/*.txt")

fw = open("gyou.txt", "w")

#ファイル名を職員番号にする
def numberNS(n):
    converter = n.replace("./txt_test\\","").replace(".txt","")
    return converter


for file in data:
    f = open(file, "r")
    fnumber = str(file)

    syokuinNumber = numberNS(fnumber)
    fw.write(syokuinNumber + ",")
    
    # print("----------職員番号は「{0}」です----------".format(syokuinNumber))
    fdata = f.read() #ファイル終端まで読んだデータを返す
    lines = fdata.split("\n")
    f.close()


    #print("----------改行数は{0}です----------".format(len(lines1)))
    noGenzai = []
    for i in range(len(lines)):
        editText = lines[i].replace("　", "")
        if (("現 在") in editText) or (("現在") in editText) or (("現  在") in editText):
            noGenzai.append(i)
            break

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
    try:
        if noGenzai[-1] == 0:
            print("現在がない職員番号は「{0}」です".format(syokuinNumber))
    except IndexError:
        print("現在がない職員番号は「{0}」です".format(syokuinNumber))
    fw.write("\n")

fw.close()