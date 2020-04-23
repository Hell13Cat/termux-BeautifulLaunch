













import os
import shutil
import platform

def dels(text):
 for num in range(len(text)):
  char = text[num]
  if char == " ":
   pass
  else:
   break
 readytext = text[num:(len(text))]
 return readytext


try:
 import configparser
except ImportError:
 import ConfigParser as configparser
config = configparser.ConfigParser()
config.read(os.getcwd() + "/termux-br.cfg")
phoneroot = config.get("Setting", "phone")
flashroot = config.get("Setting", "flash")


os.system("clear")
stats = ["+------------------------------+", "|      Welcome to termux!      |", "+------------------------------+"]
stats.append("+++    System Information    +++")
systeminfo = platform.system() + " " + platform.release() + " / " + platform.architecture()[0]
stats.append(systeminfo)
res = os.popen("vmstat -s").read()
pars = res.split("\n")
stats.append("+++      RAM statistics      +++")
counta = 0
for one in pars:
 if "K" in one:
  if "memory" in one:
   if ("total" in one) or ("free" in one):
    gg = (dels(one).split(" "))[0]
    counta += 1
    if counta == 1:
     adds = "> " + str(int(gg) // 1024) + " mb - Total"
     ggh = int(gg)
     stats.append(adds)
    if counta == 2:
     adds = "> " + str((ggh - int(gg)) // 1024) + " mb - Used"
     stats.append(adds)
     adds = "> " + str(int(gg) // 1024) + " mb - Free"
     stats.append(adds)
stats.append("+++ Phone memory statistics +++")
total, used, free = shutil.disk_usage(phoneroot)
stats.append("> " + str(total // (2**20)) + " mb - Total")
stats.append("> " + str(used // (2**20)) + " mb - Used")
stats.append("> " + str(free // (2**20)) + " mb - Free")
stats.append("+++ Flash memory statistics +++")
total, used, free = shutil.disk_usage(flashroot)
stats.append("> " + str(total // (2**20)) + " mb - Total")
stats.append("> " + str(used // (2**20)) + " mb - Used")
stats.append("> " + str(free // (2**20)) + " mb - Free")
stats.append("+++       Enjoy using       +++")

width = shutil.get_terminal_size().columns 
position = (width - max(map(len, stats))) // 2
for line in stats: # left justtified
 if ("+" in line) or ("|" in line) or ("/" in line):
  print(line.center(width))
 else:
  print(' '*position + line)

#for line in stats: # right justified
# print(line.rjust(width // 2))
#for line in stats: # center
# print(line.center(width))









