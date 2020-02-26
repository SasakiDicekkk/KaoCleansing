import re

moji = '私の番号は042-555-0341です1.3440じつは345-222-4536'

phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phone_num_regex.findall(moji)
print('番号が見つかりました' + str(mo))
