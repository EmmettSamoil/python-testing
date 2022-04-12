
class Backpack:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.open = False
        # method to open bag
    def openBag(self):
        self.open = True
        print("Bag Opened...")
        # method to add item to the items list
    def putIn(self, item):
        if self.open:
            item = item.lower()
            self.items.append(item)
            print(f"Added {item} to bag.")
        else:
            print("Error: bag not open.")
    # method to close bag
    def closeBag(self):
        self.open = False
        print("Bag Closed...")
    # method to take item out of bag
    def takeout(self, item):
        if self.open:
            item = item.lower()
            try:
                self.items.remove(item)
                print(f"The item, {item}, was removed.")
            except ValueError:
                print(f"Error: {item} not in bag.")
        else:
            print("Error: bag not open.")
# end class Backpack


# main function
def main():
    # task 2
    smallBlue = Backpack("Blue", "Small")
    mediumRed = Backpack("Red", "Medium")
    largeGreen = Backpack("Green", "Large")
    # task 3
    mediumRed.openBag()
    mediumRed.putIn("Lunch")
    mediumRed.putIn("Jacket")
    mediumRed.closeBag()
    mediumRed.openBag()
    mediumRed.takeout("Jacket")
    mediumRed.closeBag()
# end main()


if __name__ == "__main__":
    main()