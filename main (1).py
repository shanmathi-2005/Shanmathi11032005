'''Implement a class called player that represents a cricket player.The player class should have a
method called play() which printss "The players is playing cricket. Derive a two classes,Batsman and
Bowler, from the player class. Override the play() method in each derived class to print "The batsman
is batting" and "The bowler is blowing", respectively. Write a program to create subject or both the
Batsman and Blower classes and call the play() method for each object.'''


# Define the base class Player
class Player:
      def play(self):
        print("The  player is playing cricket.") 

# Define the derived class Batsman
class Batsman(Player):
      def play(self):
          print("The batsman is batting.")

# Define the derived class Bowler
class Blower(Player):
      def play(self):
          print ("The blower is blowing.")

# create object of Batsman and Bowler classes
batsman=Batsman()
bowler=Blower()

# call the play() method for each object
batsman.play()
bowler.play()