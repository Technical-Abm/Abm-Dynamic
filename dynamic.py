# -*- coding: utf-8 -*-

import re
import time
import os
import sys
import platform
import subprocess

try:
    import requests
except (KeyError,IOError,OSError):
    os.system("pip install requests")

try:
    import mechanize
except (KeyError,IOError,OSError):
    os.system("pip install mechanize")

try:
    import bs4
except (KeyError,IOError,OSError):
    os.system("pip install bs4")

try:
    import progress
except (KeyError,IOError,OSError):
    os.system("pip install progress")

try:
    import tqdm
except (KeyError,IOError,OSError):
    os.system("pip install tqdm")

try:
    import click
except (KeyError,IOError,OSError):
    os.system("pip install click")

from functools import lru_cache
from sys import maxsize

@lru_cache(maxsize=1)
class User_Main(object):
    def __init__(self) -> None:
        os.system("clear")
        try:
            if hasattr(sys,'getandroidapilevel'):
                User()
            else:
                print()
                print("\tInvalid, you are use another platform")
                time.sleep(3)
                exit()
        except ConnectionError:
            print()
            exit("Internet connection failed please fast it first")

@lru_cache(maxsize=1)
class User(object):
    def __init__(self) -> None:
        os.system("clear")
        try:
            os.system("termux-setup-storage")
            if "y":
                try:
                    Main()
                except (KeyError,IOError):
                    print()
                    print("\tSomething wrong please try again")
                    time.sleep(3)
                    User()
            elif "n":
                try:
                    NotFound()
                except (KeyError,IOError):
                    print()
                    print("\tSomething wrong please try again")
                    time.sleep(3)
                    User()
        except ConnectionError:
            print()
            print("\tYour internet connection failed")
            time.sleep(3)
            exit()

@lru_cache(maxsize=1)
class NotFound(object):
    def __init__(self) -> None:
        """
        Maybe not working Bro :)
        """
        exit("        Exit Right Now :)        ")

@lru_cache(maxsize=1)
class Main(object):
    def __init__(self) -> None:
        os.system("clear")
        try:
            aarch = "uname -om"
            subprocess.Popen(aarch,shell=True)
            time.sleep(3)
        except (KeyError):
            print()
            print("   The subprocess does not check your termux platform   ")
            print("               Please try again               ")
            Main()
            try:
                with open('abm.txt', 'a+') as f:
                    f.write('Welcomet to abm graphing project')
            except FileNotFoundError:
                os.system("termux-setup-storage")
                os.system("rm -rf abm.txt")
                Main()
                try:
                    with open('abm.txt', 'r') as f:
                        print(f.read())
                except FileNotFoundError:
                    os.system("termux-setup-storage")
                    os.system("rm -rf abm.txt")
                    Main()
        platform_reverse()

@lru_cache(maxsize=1)
class platform_reverse(object):
    def __init__(self) -> None:
        os.system("clear")
        try:
            __abm__ = platform.architecture()[0]
            if "64bit" in __abm__:
                os.system("cd abm64 && python main.py")
            elif "32bit" in __abm__:
                os.system("cd abm32 && python main.py")
            else:
                print()
                exit("    Invalid aarch device maybe your android is too old    ")
        except ConnectionError:
            print()
            exit(" Your internet connection failed ")

if __name__ == '__main__':
    User_Main()
