from django.db import models
import json

#--------------------------------------------------------
# Компетенции, индикаторы и ЗУВ (Знания, умения, владения)
#--------------------------------------------------------
class Model:
    def __init__(self, type, name, description, children):
        self.type = type
        self.name = name
        self.description = description
        self.children = children
    def ChangeModel(self, newName, newDescription):
        self.name = newName
        self.description = newDescription

def loadJSON():
    with open('DB.json', 'r') as file:
        data = json.load(file)
    return data
def saveJSON(data):
    with open('DB.json', 'w') as file:
        json.dump(data, file, indent=3)