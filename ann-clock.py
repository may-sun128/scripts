#!/usr/bin/python

import datetime 
from termcolor import colored

class Ascii_Numbers:
   def __init__(self):

      self.zero = '''
       0000
      00  00
      00  00
      00  00
       0000
      '''

      self.one = '''
      1111
        11
        11
        11
      111111
      '''

      self.two = '''
       2222
      22  22
         22
        22
      222222
      '''

      self.three = '''
       3333
      33  33
         333
      33  33
       3333
      '''

      self.four = '''
      44  44
      44  44
      444444
          44
          44
      '''

      self.five = '''
      555555
      55
      55555
          55
      55555
      '''

      self.six = '''
       6666
      66
      66666
      66  66
       6666
      '''

      self.seven = '''
      777777
         77
        77
       77
      77'''

      self.eight = '''
       8888
      88  88
       8888
      88  88
       8888
      '''

      self.nine = '''
       9999
      99  99  
       99999
          99  
       9999
      '''

      self.colon = '''
      ##
      
      ##
      '''

      # self.one.rstrip()
      # self.two.rstrip()
      # self.three.rstrip()
      # self.four.rstrip()
      # self.five.rstrip()
      # self.six.rstrip()
      # self.seven.rstrip()

def get_colored_time():
   time = datetime.datetime.now().strftime("%X")

   colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
   colored_time = []
   i = 0
   letters = Ascii_Numbers()

   for char in time:
      try:
         if str(char) == '1':
            colored_time.insert(0, colored(letters.one.strip('n'), colors[i]))
         elif str(char) == '0':
            colored_time.insert(0, colored(letters.one.strip('n'), colors[i]))
         elif str(char) == '2':
            colored_time.insert(0, colored(letters.one.strip('n'), colors[i]))
         elif str(char) == '3':
            colored_time.insert(0, colored(letters.one.strip('n'), colors[i]))
         elif str(char) == '4':
            colored_time.insert(0, colored(letters.one.strip('n'), colors[i]))
         elif str(char) == '5':
            colored_time.insert(0, colored(letters.one.strip('n'), colors[i]))
         elif str(char) == '6':
            colored_time.insert(0, colored(letters.one.strip('n'), colors[i]))
         elif str(char) == '7':
            colored_time.insert(0, colored(letters.one.strip('n'), colors[i]))
         elif str(char) == '8':
            colored_time.insert(0, colored(letters.one.strip('n'), colors[i]))
         elif str(char) == '9':
            colored_time.insert(0, colored(letters.one.strip('n'), colors[i]))
         elif str(char) == ':':
            colored_time.insert(0, colored(letters.one.strip('n'), colors[i]))
      except:
         debug_print('off by one')
      if i < 5:
         i += 1
      else:
         i = 0

   return colored_time



def debug():
   colored_time = get_colored_time()
   print(colored_time)
   print('Built')

def main():
   colored_time = get_colored_time()
   print(colored_time)

#main()
debug()