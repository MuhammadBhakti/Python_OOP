print("Latihan object Oriented Programming (OOP)")
print("     <Multiple Inheritance>")

class Team:
    def setTeam(self,team):
        self.team = team

    def showTeam(self):
        print(self.team)

class Type_Hero:
    def setType(self,type):
        self.type = type

    def showType(self):
        print(self.type)

#Multiple Inheritance
class Hero(Team,Type_Hero):

    def __init__(self,name,health):
        self.name = name
        self.health = health

#Set object name

Agung = Hero('Agung',100)
Agung.setTeam("Merah")
Agung.setType("Striker")

Agung.showType()
Agung.showTeam()

