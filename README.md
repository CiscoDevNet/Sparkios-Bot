# Sparkios-Bot

###Simple CiscoSpark Nagios / Cmd Line Bot Messenger for alerts or other cmd line functionality.

This is a very simple commandline tool for passing messages to a Cisco Spark bot to send your message to a Spark Chat room.
I primarily use this tool as a Nagios plugin to allow Nagios to send alerts to a Spark room, but this could be used for any commandline messaging.

###Get-Started

* Modify the code to include the token from your Cisco Sparkbot
``` python
bearer = "Bearer <Your Bot Token Here>"
```
* From the Command Line run NagiosPlugin-CmdLine_Bot.py like the following (infoArg1 will be message passed to the Spark room):
``` shell
python /your/location/ChatOps_CmdLineBot.py -r <Spark Room ID> -m <infoArg1>
```
* You can also run the command with more than one informational argument passed to Spark
``` shell
python /your/location/ChatOps_CmdLineBot.py -r <Spark Room ID> -m <infoArg1> <infoArg2> <infoArg3> <infoArgXX>
```

Please let me know if you have any questions.

