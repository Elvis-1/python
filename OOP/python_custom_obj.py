class MyFirstClass:
    index = "Author-Book"
    print("Who wrote this?")

    def handList(self, philosopher,book):
        print(self.index, philosopher + " wrote the book: "+book)


# whodunnit = MyFirstClass()
# whodunnit.handList("Sun Tzu","The Art of War")


#   THIER SOLUTION
# Sample Solution code
class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)

whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")