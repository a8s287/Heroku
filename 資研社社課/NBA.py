

import requests as re
import json 



request_url = "http://data.nba.net/prod/v2/2019/teams.json"

r = re.request("GET",request_url)

j = json.loads( r.text )

cnt = 0
for i in j['league']['standard']:
    cnt += 1
    if cnt == 5:
        print (i)
        break
    
    
list = []
list2 = []
cnt2 = 0
cnt3 = 0
for i in j['league']:
    for x in j['league'][i]:
        if x['isNBAFranchise'] == True:
            cnt2 += 1
            list.append(x['fullName'])
        if x['divName'] == "Pacific":
            cnt3 += 1
            list2.append(x['fullName'])

print( cnt2 )
for i in list:
    print(i)
print( cnt3 )
for i in list2:
    print(i)