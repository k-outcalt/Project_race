'''
race_project.py
by Katherine Outcalt
6.6.19
'''
import turtle
import random
import math


class Frog(object):
    """Keeps track of a frog instance with frog name, color, and bib number.
       Class Frog has methods to move and place the frog via the Turtle class.
    """
    bib_num = 0
    def __init__(self, name, color):
        self.name = name
        Frog.bib_num += 1
        self.bib_num = Frog.bib_num
        self.color = color
        self.turtle = turtle.Turtle()
        self.turtle.color(self.color, 'black')
        
    def __str__(self):
        return "#%d, %s's %s frog" % (self.bib_num, self.name, self.color)
    
    def position(self):
        return self.turtle.position()
        
    def place(self, x, y, heading):
        """Set turtle to the x and y and heading parameter."""
        self.turtle.setposition(x, y)
        self.turtle.setheading(heading)
                
    def doSomething(self):
        """Randomly jumps the frog or spins
           the frog or does nothing."""
        move = random.choice(['jump', 'spin', 'do nothing'])
        if move == 'jump':
            distance = random.choice([2, 5, 10, 12, 15, 20, 30])
            x, y = self.turtle.position()
            angle = math.radians(self.turtle.heading())
            x += distance * math.cos(angle)
            y += distance * math.sin(angle)
            self.turtle.setposition(x, y)
        elif move == 'spin':     
            randomAngle = random.choice([5,7,10,15,25,45,75,90])
            spin = random.choice(['right','left'])
            if spin == 'right':
                self.turtle.right(randomAngle)
            else:
                self.turtle.left(randomAngle)
        else:
            pass

class RaceCourse(object):
    """Sets up the race course for the frogs by its methods
       to add, place, and course correct frogs. It also announces
       the winner.
    """
    def __init__(self):
        self.frogs = []
        self.paths = {}
        self.width = 600
        self.height = 400
        self.x_bound = self.width // 2 #for x boundary
        self.y_bound = self.height // 2 #for y boundary
        
    def addFrog(self, frog):
        """adds frog and sets up dictionary key for frog"""
        self.frogs.append(frog)
        self.paths[frog.bib_num] = []
        
    def placeFrogs(self):
        """gets frogs into starting spots, draws boundary, and prints titles"""
        # draw boundary #
        turtle.penup()
        turtle.goto(-self.x_bound, self.y_bound)
        turtle.setheading(0)
        turtle.pendown()
        turtle.fd(self.width)
        turtle.right(90)
        turtle.fd(self.height)
        turtle.right(90)
        turtle.fd(self.width)
        turtle.right(90)
        turtle.fd(self.height)
        turtle.hideturtle()
        turtle.write("The Great Frog Race!", font=("Arial", 24, "normal"))
        
        # frogs to starting spots w/ title #
        num_frogs = len(self.frogs)
        y_val = -self.y_bound + self.height / (2 * num_frogs)
        for frog in self.frogs:
            frog.turtle.penup()
            frog.place(-self.x_bound, y_val, 0)
            frog.turtle.write(str(frog), font=("Arial", 15, "normal"))
            frog.turtle.pendown()
            y_val += self.height // num_frogs 

    def offCourse(self, frog):
        """returns True if frog is off course"""
        x, y = frog.position()
        if x < -self.x_bound: 
            return True
        elif y > self.y_bound:
            return True
        elif y < -self.y_bound:
            return True 
        else:
            return False
        
    def correct(self, frog):
        """puts frog back to the closest boundary w/ heading 0"""
        x, y = frog.position()
        if x < -self.x_bound:  
            frog.place(-self.x_bound, y, 0)
        if y > self.y_bound:
            frog.place(x, self.y_bound, 0)
        elif y < -self.y_bound:
            frog.place(x, -self.y_bound, 0)
            
        
    def moveFrogs(self):
        """calls doSomething and moves frogs if necessary"""
        for frog in self.frogs:
            self.paths[frog.bib_num].append(frog.position())
            frog.doSomething()
            if self.offCourse(frog):
                self.correct(frog)

    def winner(self):
        """returns the frog that crosses the finish first (the x boundary).
           If no frogs have won yet, returns None."""
        for frog in self.frogs:
            x, y = frog.position()
            if x > self.x_bound:
                return frog
        return None
    
    def announceWinner(self):
        """announces the winner in the center of the screen"""
        turtle.penup()
        turtle.goto(0,0)
        turtle.write("Winner is: " + str(self.winner()), align="center", font=("Arial", 20, "bold"))

    def go(self):
        """ Run the race! This includes placing the frogs on the
            starting line, printing the titles and boundaries and keeps
            calling doSomething for each frog until there is a winner.
            Then the winner is displayed and the race is finished.
        """
        self.placeFrogs()
        while self.winner() is None:
            self.moveFrogs()
        self.announceWinner()
                    
        
def race():
    """ Create a race course, load it up with three frogs and go! Then also
        look at the data collected for the frogs' paths and display a
        selection from it.
    """
    course = RaceCourse()
    course.addFrog(Frog('Amy', 'green'))
    course.addFrog(Frog('Gil', 'blue'))
    course.addFrog(Frog('Lou', 'red'))
    course.go()
  
    for bib in course.paths:
        print('for frog', bib, 'number of moves:', len(course.paths[bib]))
        print('printing every 20th:')
        for i in range(0, len(course.paths[bib]), 20):
            print(course.paths[bib][i])

if __name__ == "__main__":
    race()
        

    
