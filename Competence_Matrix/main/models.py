# -------------------------------------------------------------------
# Модель компетенций, индикаторов и ЗУВов (Знания, умения, владения)
#-------------------------------------------------------------------
class Model:
    def __init__(self, name, type, description, children):
        self.name = name
        self.type = type
        self.description = description
        self.children = children