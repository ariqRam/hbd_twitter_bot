# hbd.py
This is a Python script that uses Selenium library to send messages to another Twitter user.

The idea behind this script was to open a way to send an early birthday wish without having to stay up till midnight. The script takes in several inputs: 
  1. Browser of choice (supports Firefox and Chrome)
  2. The sending time (hour and minute)
  3. Target Twitter account
  4. The birthday wish (as a .txt file)
  5. Sender's Twitter email address and password

# Requirements
  1. The machine on which the script runs should have the path to chromedriver.exe or geckodriver.exe (for Firefox) saved in the environment PATH.
  2. If the drivers' path are not put in the environment PATH, the file should be in the same directory as the hbd.py script
  3. The birthday wish file has to be in the same directory as the hbd.py script.
  
