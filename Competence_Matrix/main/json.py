import json
import os
import codecs

def loadJSON():
    file = codecs.open(os.path.dirname(os.path.abspath(__file__)) + "\DB.json", 'r', "utf_8_sig")
    data = json.load(file)
    return data
def saveJSON(data):
    file = codecs.open(os.path.dirname(os.path.abspath(__file__)) + "\DB.json", 'w', encoding='utf8')
    json.dump(data, file, indent=3, ensure_ascii=False)