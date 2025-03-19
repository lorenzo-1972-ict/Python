# class & functions

class Character:
    
    def __init__(self, type):
        self.type=type
        print("\nCharacter's type: ", type)

    def profile(self, name):
        self.name=name
        print("\nFellowship's character's name: ",name)
        
    def weapons(self, weapons):
        print("\nFellowship's character's weapon: ", weapons,"\n")

    def artefacts(self):
        print("...")

# instantiations

wizard1 = Character("Wizard")
wizard1.profile("Gandalf")
wizard1.weapons("staff")

archer1 = Character("Archer")
archer1.profile("Legolas")
archer1.weapons("long bow")