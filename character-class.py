class character:
    #initialize class
    def __init__(self, name, phrase1, phrase2):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = 0
    # Speak method
    def speak(self, phraseNum):
        if phraseNum == 1:
            print(self.phrase1)
        elif phraseNum == 2:
            print(self.phrase2)
        else:
            print("bleh")
    # setLevel Method
    def setLevel(self, newLevel):
        self.level = newLevel
        print(f"New level: {self.level}")

# main function
def main():
    # task 2
    Matt = character("I am Matt", "I go bowling", "I am good at Wii Sports")
    Guts = character("I'd rather fight for my life than live it", "Hmph", "But if you disturb me ill kill you")
    # task 3
    Matt.speak(1)
    Guts.setLevel(2)
    Guts.speak(2)
# end main()

main()