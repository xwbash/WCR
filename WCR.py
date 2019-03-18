#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
def finish():
    print("""
  ▄████████  ▄█  ███▄▄▄▄    ▄█     ▄████████    ▄█    █▄    
  ███    ███ ███  ███▀▀▀██▄ ███    ███    ███   ███    ███   
  ███    █▀  ███▌ ███   ███ ███▌   ███    █▀    ███    ███   
 ▄███▄▄▄     ███▌ ███   ███ ███▌   ███         ▄███▄▄▄▄███▄▄ 
▀▀███▀▀▀     ███▌ ███   ███ ███▌ ▀███████████ ▀▀███▀▀▀▀███▀  
  ███        ███  ███   ███ ███           ███   ███    ███   
  ███        ███  ███   ███ ███     ▄█    ███   ███    ███   
  ███        █▀    ▀█   █▀  █▀    ▄████████▀    ███    █▀   
~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--~~
                     instagram: yigitaydn.py                                                           
    """)
def logo():
    print("""
   ▄█     █▄   ▄████████    ▄████████ 
  ███     ███ ███    ███   ███    ███ 
  ███     ███ ███    █▀    ███    ███ 
  ███     ███ ███         ▄███▄▄▄▄██▀ 
  ███     ███ ███        ▀▀███▀▀▀▀▀   
  ███     ███ ███    █▄  ▀███████████ 
  ███ ▄█▄ ███ ███    ███   ███    ███ 
   ▀███▀███▀  ████████▀    ███    ███
~~--~~--~~--~~--~~--~~--~~--~~--~~--~~--
           wordlist combiner
                by $bash
""")
def program():
    os.system("clear")
    logo()
    wordlist = input(">> Please Enter the main file name.: ")
    os.system("clear")
    logo()
    wordlist2 = input(">> PLease Enter the other file name.: ")
    os.system("clear")
    a = open(wordlist, "r+",encoding = "utf-8")
    f = open(wordlist2, "r+",encoding = "utf-8")
    for k in f:
        for c in a:
            a.write(c)
        a.write(k)
    f.close()
    a.close
    finish()
program()
