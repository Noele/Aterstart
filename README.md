# IMPORTANT NOTICE
## Theres a good chance this program will get you suspended from Aternos, Please don't use it.

# Aterstart
A discord bot for starting an Aternos server

## Commands
  ```_checkonline``` returns the current status of the server (Online, Offline & Loading)
  
  ```_startserver``` & ```_stopserver``` Starts and Stops the server
  
  ```_getip``` Returns the servers address in the format ```ip:port```
  
## Notes
  Requires [discord.py](https://github.com/Rapptz/discord.py) & [python-aternos](https://pypi.org/project/python-aternos/)
  
  On startup, A file called ```data.json``` will be created, You will then need to add your Aternos username, password and discord bot token into this file, please leave ```hashed``` set to False, this is updated on first login to hash your password so it's not saved as plaintext in the file.
