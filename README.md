# terminal-vkmessenger
VK Messenger on python helps you to chat with your friends secretly in your termianl or command prompt

vkmessenger is executable python file(to run - print in linux\osx terminal ./vkmessengeer; For windows -- compile with python)

HOW IT WORKS:
  With vk_auth.py it connects to oauth.vk.com(with GET Request) and sends printed data(login and password). On success it gets cookies and acces_token to authorize
  Then you can write commands
  </br>
   &nbsp;&nbsp;&nbsp;&nbsp; - command "help" provides you to list all aviable commands</br>
    &nbsp;&nbsp;&nbsp;&nbsp; - command "d" provides you to list your last 10 dialogs</br>
     &nbsp;&nbsp;&nbsp;&nbsp; - to open a dialog print id from round brackets</br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- then everything you print except "r" and "d" will be send to id-helder</br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - to refresh use "r" command</br>
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - to return to dialog list use "d" command</br>
    &nbsp;&nbsp;&nbsp;&nbsp; - command "r" provides to refresh current activity</br>
   &nbsp;&nbsp;&nbsp;&nbsp; - command "exit" exits :D</br>
		
