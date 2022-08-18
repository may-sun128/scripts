#!/usr/bin/python

import datetime
from termcolor import colored
import sys

class Ascii_Numbers:
   def __init__(self):

      self.zero = ''' 
 0000
00  00
00  00
00  00
 0000'''

      self.one = '''
1111
  11
  11
  11
111111'''

      self.two = '''
 2222
22  22
   22
  22
222222'''

      self.three = '''
 3333
33  33
   333
33  33
 3333'''

      self.four = '''
44  44
44  44
444444
    44
    44'''

      self.five = '''
555555
55
55555
    55
55555'''

      self.six = ''' 
 6666
66
66666
66  66
 6666'''

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
 8888'''

      self.nine = '''
 9999
99  99  
 99999
    99  
 9999'''

      self.colon = '''
##
      
##'''

      self.fuck = 'fuck'

def get_colored_time() -> str:
   time = datetime.datetime.now().strftime("%X")
   i = 0
   letters = Ascii_Numbers()
   ascii_time = ''


   for char in time:
      try:
         if str(char) == '1':
            ascii_time += join_art("", one, "")
         elif str(char) == '0':
            ascii_time += join_art("", zero, "")
         elif str(char) == '2':
            colored_time += colored(letters.two, colors[i])
         elif str(char) == '3':
            colored_time += colored(letters.three, colors[i])
         elif str(char) == '4':
            colored_time += colored(letters.four, colors[i])
         elif str(char) == '5':
            colored_time += colored(letters.five, colors[i])
         elif str(char) == '6':
            colored_time += colored(letters.six, colors[i])
         elif str(char) == '7':
            colored_time += colored(letters.seven, colors[i])
         elif str(char) == '8':
            colored_time += colored(letters.eight, colors[i])
         elif str(char) == '9':
            colored_time += colored(letters.nine, colors[i])
         elif str(char) == ':':
            colored_time += colored(letters.colon, colors[i])
      except:
         print('off by one')
      if i < 5:
         i += 1
      else:
         i = 0

   return colored_time

# Working, but only with two string
# Also, not changing color
def join_art(s1, s2, str_between=''):
   lines1 = s1.split('\n')
   lines2 = s2.split('\n')
   max_dist = max([len(s) for s in lines1])
   f_str = '{:<' + str(max_dist) + '}{}{}'
   s3 = "\n".join([f_str.format(str1, str_between, str2) for str1, str2 in zip(lines1, lines2)])
   return s3

def debug():
   colored_time = get_colored_time()
   l_colored_time = colored_time.split('x')

   ac = Ascii_Numbers()
   one = ac.one
   two = ac.two

   one_and_two = join_art(one, two, " ")

   print(one_and_two)
   print('Built')

def main():
   colored_time = get_colored_time()
   # Added x to the ascii art class so it could be easily made into a list
   # If a list ends up not being needed, TODO remove the x
   l_colored_time: list[str] = colored_time.split('x')

   print(colored_time)

def debug_or_main():
   i = input("Debug or Main")
   if i == 'd':
      debug()
   elif i == 'm':
      main()
   else:
      print('debug main error')

debug_or_main()
