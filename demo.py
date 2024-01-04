import time
from termcolor import colored
from time import sleep
import random

colours = ['red','green','yellow','blue','magenta','cyan','white']
position = 0
position1 = 0
index = 0
index1 = 0

race_track1 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
race_track2 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
race_track3 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
race_track4 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

class Car:
  def __init__(self, name, maxspeed, logo, colour):
    self.name = name
    self.maxspeed = maxspeed
    self.logo = logo
    self.colour = colour

  def __str__(self):
    return('Name: %s\nMax speed: %s\nLogo: %s\nColour %s')%(self.name, int(self.maxpeed), self.logo, self.colour)

class YourCar(Car):
  def __init__(self, name, maxspeed, logo, colour):
    self.name = name
    self.maxspeed = maxspeed
    self.logo = logo
    self.colour = colour

def progress(percent=0, width=30):
    hashes = width * percent // 100
    blanks = width - hashes

    print('\r[', hashes*'#', blanks*' ', ']', f' {percent:.0f}%', sep='',
        end='', flush=True)
  
def move():
  global position
  global position1
  while True:
    move1 = random.randint(0,2)
    if position + move1 <= 100:
      for i in range(0, move1):
        position += 1
        race_track1[position] = 'ㅤ'
        race_track2[position] = '#'
      break
      
  while True:
    move2 = random.randint(0,2)
    if position1 + move2 <= 100:
      for i in range(0, move2):
        position1 += 1
        race_track3[position1] = 'ㅤ'
        race_track4[position1] = '#'
      break

def printFirstTrack():
  global index
  print('KM passed:', position,'\n\n')
  for i in race_track1:
    print(race_track1[index], end = '')
    index +=1
  index = 0
  
def printBottomFirstTrack():
  global index
  for i in race_track1:
    print(race_track2[index], end = '')
    index +=1
  print('\n____________________________________________________________________________________________________')
  index = 0

def printSecondTrack():
  global index1
  print('KM passed:', position1,'\n\n')
  for i in race_track3:
    print(race_track3[index1], end = '')
    index1 +=1
  index1 = 0
  
def printBottomSecondTrack():
  global index1
  for i in race_track3:
    print(race_track4[index1], end = '')
    index1 +=1
  print('\n____________________________________________________________________________________________________')
  index1 = 0

random_colour1 = random.choice(colours)
car1 = colored(".-'--`-._", random_colour1)
car2 = colored("'-O---O--'", random_colour1)
colours.remove(random_colour1)
random_colour2 = random.choice(colours)
car3 = colored(".-'--`-._", random_colour2)
car4 = colored("'-O---O--'", random_colour2)

print('CARS RACING')
print('-------------')
print('Car1:', random_colour1)
print('Car2:', random_colour2)
print()
print('The first car to reach 50 km wins!')

while True:
  print()
  bet = input('Which car do you bet will win? (Car1 or Car2) ')
  print()
  bet = bet.title()
  if bet == 'Car1' or bet == 'Car2':
    break
  else:
    print('Please choose a valid car!')

logo = input('What do you want to say on your car? ')
if bet == 'Car1':
  car1 = colored(".-'--`-." + logo + "_", random_colour1)
  car2 = colored("'-O---O---'", random_colour1)
if bet == 'Car2':
  car3 = colored(".-'--`-." + logo + "_", random_colour2)
  car4 = colored("'-O---O---'", random_colour2)

print('Loading race...')
for i in range(101):
    progress(i)
    sleep(0.01)
print('\n')

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
  if position == position1 == 100:
    print('It was a tie')
    break
  if bet == 'Car1':
    if position == 100:
      print('The', random_colour1, 'car won so your bet was correct!')
      break
    if position1 == 100:
      print('The', random_colour1, 'car lost so your bet was incorrect!')
      break
  if bet == 'Car2':
    if position == 100:
      print('The', random_colour2, 'car lost so your bet was incorrect!')
      break
    if position1 == 100:
      print('The', random_colour2, 'car won so your bet was correct!')
      break
  race_track1[position] = 'ㅤ'
  race_track2[position] = '#'
  race_track3[position1] = 'ㅤ'
  race_track4[position1] = '#'
  move()
  for i in range(0,20):
    print()
  