import requests
import json
import datetime as dt
import sys
import getopt


#Simple Bot Function for passing messages to a room
def spark_it(message, bot_token, roomid):

        start_url = "https://api.ciscospark.com"

        token = bot_token

        header = {"Authorization": "%s" % token,
                  "Content-Type": "application/json"}

        api_url = "/v1/messages/"
        data = {"roomId": roomid,
                "text": message}

        spark_url = start_url + api_url

        spark_message = requests.post(spark_url, headers=header, data=json.dumps(data), verify=True)

        return spark_message


def main():
        now = dt.datetime.now()
        bearer = "Bearer <Your Bot Token Here>"
        alerts = ''
        cmd_message = 'SparkAPI_NagiosTest.py -r <roomID_Here> -m <PassErrorMessageHere and pass as many arguments after -m as you like>'

        #Command line Argument Parsing Section
        try:
                opts, args = getopt.getopt(sys.argv[1:], 'hr:m:', ["errMess="])
                print(args)
        except getopt.GetoptError:
                print(cmd_message)
                sys.exit(2)
        if len(opts) == 0:
                print(cmd_message)
                sys.exit(2)
        for opt, arg in opts:
                if opt == '-h':
                        print(cmd_message)
                        sys.exit(2)
                elif opt == '-r':
                        spark_room = arg
                elif opt == '-m':
                        alerts = arg + '\n' + '\n'.join(args)

        messages = str(now) + "\n" + alerts

        spark_it(messages, bearer, spark_room)


if __name__ == '__main__':
        main()
