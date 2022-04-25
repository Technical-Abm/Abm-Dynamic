# -*- coding: utf-8 -*-

try:
    import os
    import platform
    import requests
    import mechanize
    import bs4
    import subprocess
    import time
except (OSError):
    os.system("pip install requests && pip install mechanize")
    os.system("pip install requests bs4 && pip install bs4")
    
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

class NotFound(object):
    def __init__(self) -> None:
        """
        Maybe not working Bro :)
        """
        exit("        Exit Right Now :)        ")

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
    User()
