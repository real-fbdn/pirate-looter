import os
from time import sleep

print("""
 ________  ___  ________  ________  _________  _______           ___       ________  ________  _________  _______   ________     
|\   __  \|\  \|\   __  \|\   __  \|\___   ___\\  ___ \         |\  \     |\   __  \|\   __  \|\___   ___\\  ___ \ |\   __  \    
\ \  \|\  \ \  \ \  \|\  \ \  \|\  \|___ \  \_\ \   __/|        \ \  \    \ \  \|\  \ \  \|\  \|___ \  \_\ \   __/|\ \  \|\  \   
 \ \   ____\ \  \ \   _  _\ \   __  \   \ \  \ \ \  \_|/__       \ \  \    \ \  \\\  \ \  \\\  \   \ \  \ \ \  \_|/_\ \   _  _\  
  \ \  \___|\ \  \ \  \\  \\ \  \ \  \   \ \  \ \ \  \_|\ \       \ \  \____\ \  \\\  \ \  \\\  \   \ \  \ \ \  \_|\ \ \  \\  \| 
   \ \__\    \ \__\ \__\\ _\\ \__\ \__\   \ \__\ \ \_______\       \ \_______\ \_______\ \_______\   \ \__\ \ \_______\ \__\\ _\ 
    \|__|     \|__|\|__|\|__|\|__|\|__|    \|__|  \|_______|        \|_______|\|_______|\|_______|    \|__|  \|_______|\|__|\|__|
""")
print("\n[- Builder version 2.1 -]\n")
print("You need to follow instructions in readme.md or it will not work!")
sleep(2)
os.system('pyarmor pack -e"--onefile --noconsole --icon NONE" setup.py')
