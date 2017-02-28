#!/usr/bin/python
import os
import sys

os.system('ls /tmp')

count=0
while count < 10:
    print(count)
    count = count + 1

def demo():
    count=0
    while count < 10:
      count = count + 1
      print(count)

demo()

class Admin():
  def __init__(self,a,b):
    self.admin=a
    self.data=b
  def new(self):
    print(self.admin, self.data)
    
inst1=Admin("Kamil","Babayev")
inst1.new()
