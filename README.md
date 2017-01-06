# terminal-vkmessenger
VK Messenger on python helps you to chat with your friends secretly in your termianl or command prompt

vkmessenger is executable python file(to run - print in linux\osx terminal ./vkmessengeer; For windows -- compile with python)

HOW IT WORKS:
  With vk_auth.py it connects to oauth.vk.com(with GET Request) and sends printed data(login and password). On success it gets cookies and acces_token to authorize
  Then you can write commands
    - command "help" provides you to list all aviable commands
    - command "d" provides you to list your last 10 dialogs
      - to open a dialog print id from brackets ("Username [status] (id)")
      - then everything you print except "r" and "d" will be send to id-helder
      - to refresh use "r" command
      - to return to dialog list use "d" command
    - command "r" provides to refresh current activity
    - command "exit" exits :D
		
