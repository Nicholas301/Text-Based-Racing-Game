import time
from termcolor import colored
from time import sleep
import random

#Global variables
car_names = ['Fredson\'s car', 'Speed racer', 'Flash', 'Nick\'s car']
car_logos = ['V8', 'HI', '$$', '99', '30']
colours = ['red','green','yellow','blue','magenta','cyan','white']
bank = 100
position = 0
position1 = 0
index = 0
index1 = 0
you_won = ''
bet = ''

race_track1 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
race_track2 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
race_track3 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
race_track4 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

#The parent class that returns the values of name, maxspeed, logo, and colour
class Car:
  def __init__(self, name, maxspeed, logo, colour):
    self.name = name
    self.maxspeed = maxspeed
    self.logo = logo
    self.colour = colour

  def __str__(self):
    return('Name: %s\nMax speed: %s\nLogo: %s\nColour: %s')%(self.name, int(self.maxspeed), self.logo, self.colour)

#The child class that is called to create a car with the following attributes
class MakeCar(Car):
  def __init__(self, name, maxspeed, logo, colour):
    self.name = name
    self.maxspeed = maxspeed
    self.logo = logo
    self.colour = colour
    
#progress bar loading animation - The number of hashes to show is based on the percent passed in. Number of blanks is whatever space is left after.
def progress(percent=0, width=30):
    hashes = width * percent // 100
    blanks = width - hashes

    print('\r[', hashes*'#', blanks*' ', ']', f' {percent:.0f}%', sep='',
        end='', flush=True)

#This function will randomly decide how many spaces each car will moves. It will return a value from 0 to max_speed
def move():
  global position
  global position1
  while True:
    move1 = random.randint(0, max_speed)
    if position + move1 <= 50:
      for i in range(0, move1):
        position += 1
        race_track1[position] = 'ㅤ'
        race_track2[position] = '##'
      break
      
  while True:
    move2 = random.randint(0, speed)
    if position1 + move2 <= 50:
      for i in range(0, move2):
        position1 += 1
        race_track3[position1] = 'ㅤ'
        race_track4[position1] = '##'
      break
#Prints the top of the first track
def printFirstTrack():
  global index
  print('KM passed:', position,'\nName:',name, '\n')
  for i in race_track1:
    print(race_track1[index], end = '')
    index +=1
  index = 0

#Prints the bottom of the first track
def printBottomFirstTrack():
  global index
  for i in race_track1:
    print(race_track2[index], end = '')
    index +=1
  print('\n____________________________________________________________________________________________________')
  index = 0

#Prints the top of the second track
def printSecondTrack():
  global index1
  print('KM passed:', position1,'\nName:',name1, '\n')
  for i in race_track3:
    print(race_track3[index1], end = '')
    index1 +=1
  index1 = 0

#Prints the bottom of the second track
def printBottomSecondTrack():
  global index1
  for i in race_track3:
    print(race_track4[index1], end = '')
    index1 +=1
  print('\n____________________________________________________________________________________________________')
  index1 = 0

#Prints the description of the program
print('In this program, you will be designing and racing in your very own car.\nThe first car to reach 50 km wins the game!\nYour goal is to make bets on the races and reach $500.\nYou will start with $100\n')

#User input that is used to create the players car
name = input('Enter the name of your car: ')
print()
while True:
  max_speed = int(input('Enter the max speed of your car (Maximum 4): '))
  if max_speed >= 1 and max_speed <= 4:
    break
  else:
    print('\nPlease choose a valid speed\n')
print()
logo = input('Enter the logo of your car: ')
print()
print('Colours:\n-----------------')
for i in colours:
  print('-', i)
print()
while True:
  colour = input('Enter the colour of your car: ')
  if colour in colours:
    colours.remove(colour)
    break
  else:
    print('\nPlease pick a valid colour\n')
print()

#Creates the players car and then prints the details of it
your_car = MakeCar(name, max_speed, logo, colour)
print('Details of your car:\n---------------------')
print(your_car)

car1 = colored(".-'--`-." + logo + "_", colour)
car2 = colored("'-O---O---'", colour)

#Will check if the player has won the game or lost the game, if the player won or lost the bet, and will create the car of the opposing player (computer)
while True:
  if you_won == True:
    bet *= 2
    bank += bet
    print('You won the bet! You made', '$'+ str(bet),'and now have', '$' + str(bank) + '!')
  if you_won == False:
    bank -= bet
    print('You lost the bet! You lost', '$' + str(bet),'and now have', '$' + str(bank) + '!')
  if bank >= 500:
    print('\nYou have reached 500 dollars and beaten the game!')
    break
  if bank <= 0:
    print('\n You are now broke! You have lost!!!')
    break
  random_colour = random.choice(colours)
  logo1 = random.choice(car_logos)
  name1 = random.choice(car_names)
  speed = random.randint(1,6)
  car3 = colored(".-'--`-." + logo1 + "_", random_colour)
  car4 = colored("'-O---O--'", random_colour)
  opposing_car = MakeCar(name1, speed, logo1, random_colour)
  print('\nDetails of the opposing car:\n----------------------------------')
  print(opposing_car)
  print()
  print('Here is a preview of your car:\n')
  print(car1)
  print(car2)
  
  #betting system - max. bet is $75 / cannot bet more than what is in bank acc.
  while True:
    print()
    bet = int(input('How much would you like to bet? [Max $75]: '))
    if bank < bet:
      print('You cannot bet more than what is in your bank account!')
    if bet > 75:
      print('You cannot bet over the maximum!')
    else:
      break
  print()
  time.sleep(5)
  print('3')
  time.sleep(1)
  print('2')
  time.sleep(1)
  print('1')
  
  print('Loading race...')
  for i in range(101):
      progress(i)
      sleep(0.01)
  print('\n')

  #The main part of the code that runs the race. It will set the car to how far it it has reached in the race. Then it will print both tracks and check if the player won or lost the race. If the race is finished, it will load up the next race
  while True:
    race_track1[position] = car1
    race_track2[position] = car2
    race_track3[position1] = car3
    race_track4[position1] = car4
    time.sleep(0.75)
    printFirstTrack()
    print('\n')
    printBottomFirstTrack()
    print('\n')
    printSecondTrack()
    print('\n')
    printBottomSecondTrack()
    if position == position1 == 50:
      print('It was a tie')
      you_won = 'Tie'
      break
    if position == 50:
      print()
      print(name, 'beat', name1, '\nYOU WON!!!')
      you_won = True
      print()
      print('Loading next race...')
      position = 0
      position1 = 0
      index = 0
      index1 = 0
      spot = 0
      for i in race_track1:
        race_track1[spot] = ''
        race_track2[spot] = ''
        race_track3[spot] = ''
        race_track4[spot] = ''
        spot += 1
      break
    if position1 == 50:
      print()
      print(name1, 'beat', name, '\nYOU LOST!!!')
      you_won = False
      print()
      print('Loading next race...')
      position = 0
      position1 = 0
      index = 0
      index1 = 0
      spot = 0
      for i in race_track1:
        race_track1[spot] = ''
        race_track2[spot] = ''
        race_track3[spot] = ''
        race_track4[spot] = ''
        spot += 1
      break
    race_track1[position] = 'ㅤ'
    race_track2[position] = '##'
    race_track3[position1] = 'ㅤ'
    race_track4[position1] = '##'
    move()
    for i in range(0,20):
      print()



