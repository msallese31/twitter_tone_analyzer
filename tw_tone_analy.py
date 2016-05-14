import twitter
import json
import sys
from watson_developer_cloud import ToneAnalyzerV3Beta

CONSUMER_KEY = 'xcgIGah9GQmug62fCupl8f8Vk'
CONSUMER_SECRET = sys.argv[1]
OAUTH_TOKEN = '727524942972096512-2yAlnSq3tSIeK0J63TM1vTGECmNzQc3'
OAUTH_TOKEN_SECRET = sys.argv[2]

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

tone_analyzer = ToneAnalyzerV3Beta(
    username='e6ac8a83-d333-4002-b9db-3208fc9189d7',
    password=sys.argv[3],
    version='2016-02-11'
)

print(json.dumps(tone_analyzer.tone(text='I am very happy'), indent=2))

US_WOE_ID = 23424977
us_trends = twitter_api.trends.place(_id=US_WOE_ID)
#print json.dumps(us_trends, indent=1)

tw = json.dumps(us_trends)
tw_json = json.loads(tw)
# print tw_json[0]['trends'][0]['name']
#for et in tw_json:
 #   for cat in et:
  #      if cat == "trends":
   #         for trends in et[cat]:
    #            print trends['name']

#print "**********************************"
i = 0
trends_list = []
for et in tw_json:
    for trends in et["trends"]:
        if(i > 4):
            break
        else:
            i += 1
            trends_list.append(trends["name"])
print trends_list
for trend in trends_list:
    print trend
