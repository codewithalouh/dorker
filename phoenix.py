#!/usr/bin/python3
#coded by Alouh Sperk (ph.phoenix)
#github: codewithalouh

import time #to delay response
import argparse #for commandline input
from googlesearch import search #for dorking


#user input
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--Output", help = "Output dk into file")
parser.add_argument("-d", "--dk", help = "Input dk")
parser.add_argument("-a", "--Amount", help = "Input dk")
args = parser.parse_args()


out = args.Output

#function to write result to file 
#sf - savefile | wf - writefile
def output(sf):
  wf = open(out, 'a')
  wf.write(sf)
  wf.write('\n')
  wf.close()
  

#function to initiate dorking
#dk - dork | a - amount
def scan():
  dk = args.dk
  need = args.Amount
  x = 0
  
  for results in search(dk, tld="com", lang="en", num=int(need), start=0, stop=None, pause=2):
            print (f"\033[31m[{x}] \033[36m{results}")
            time.sleep(0.1)
            x += 1
            if x >= int(need):
                break
            
            output(results)


scan()
