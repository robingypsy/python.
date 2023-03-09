class Chelsea:
    def points(self):
        print("I have 43 points")

class Liverpool:
    def position(self):
        print("My position is 5")

class Premier(Chelsea,Liverpool):
    def league(self):
        print("This is the premier league")

p=Premier()
p.points()
p.position()
p.league()