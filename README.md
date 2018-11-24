# Discord Bot starter code

## Running
Copy the Client Id and Client Secret into the bot.yml file. A sample configuration file can be found in config/.

Using a virtual environment is highly recommended. Python version should be 3.7+.
To install the dependencies, do the following:
1. python -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip#egg=discord.py
2. python -m pip install -r requirements.txt

To run the bot, from the src directory, call:  
```python run.py```

A sample systemd unit file can be used to have the bot run at startup. Put the unit file in the /etc/systemd/system directory and do:  
```sudo systemctl daemon-reload
sudo systemctl start [name of your service]
sudo systemctl status [name of your service]```
