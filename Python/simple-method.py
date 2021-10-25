class PlayerCharacter:
    def __init__(self,name):
        self.name = name;

    def run(self):
        return "Running";

player1 = PlayerCharacter("Larry")
print(player1.run())
print(player1.name)
