import requests
import json
import datetime as dt
import sys
import getopt


#Simple Bot Function for passing messages to a room
def SparkIt(Acheron, CharonsObol, Spark):

        StartUrl = "https://api.ciscospark.com"

        token = CharonsObol

        header = {"Authorization": "%s" % token, "Content-Type": "application/json"}

        api_url = "/v1/messages/"
        data = {"roomId": Spark,
                "text": Acheron}

        SparkUrl = StartUrl + api_url

        try:
                SparkMessage = requests.post(SparkUrl, headers=header, data=json.dumps(data), verify=True)
        except BaseException as e:
                SparkReqErrLog = open("SparkReqErrLog.log", 'w+')
                shores = str(now) + " " + str(e)
                SparkReqErrLog.write(shores)
                SparkReqErrLog.close()


def main():
        now = dt.datetime.now()
        obolus = "Bearer <Your Bot Token Here>"
        ferry = ''
        cmdMessage = 'SparkAPI_NagiosTest.py -r <roomID_Here> -m <PassErrorMessageHere and pass as many arguments after -m as you like>'

        #Command line Argument Parsing Section
        try:
                opts, args = getopt.getopt(sys.argv[1:], 'hr:m:', ["errMess="])
                print args
        except getopt.GetoptError:
                print cmdMessage
                sys.exit(2)
        if len(opts) == 0:
                print cmdMessage
                sys.exit(2)
        for opt, arg in opts:
                if opt == '-h':
                        print cmdMessage
                        sys.exit(2)
                elif opt == '-r':
                        SparkRoom = arg
                elif opt == '-m':
                        ferry = arg + '\n' + '\n'.join(args)

        fire = str(now) + "\n" + ferry

        SparkIt(fire, obolus, SparkRoom)


if __name__ == '__main__':
        main()
