#! /usr/bin/env python3

times = 10
place = "world"
try:
  for x in range(0,times):
    if (x < (times - 1)):
      print("Hello " + place + "!")
    else:
      print("Goodbye " + place + "!")
except:
  print("Done!")
