import json
import datetime



f = open('R1_data.json', 'r', encoding="utf-16")
raw_data = json.load(f)

blap = raw_data['sessionResult']['leaderBoardLines'][0]['timing']['totalTime']
# blap = raw_data['sessionResult']['leaderBoardLines'][1]['currentDriver'].key()
# print(blap)


def get_time(ms):
    mils = ms % 1000
    x = ms // 1000
    seconds = x % 60
    x = x // 60
    minutes = x % 60
    x = x // 60
    hours = x // 24
    return str(hours).zfill(2)+':'+str(minutes).zfill(2)+':'+str(seconds).zfill(2)+'.'+str(mils)



# import datetime
# time_in_millis = blap
# dt = datetime.datetime.fromtimestamp(time_in_millis / 1000.0, tz=datetime.timezone.utc)

# l = datetime.date(197)
fu = 36181560000
# print(dt)
for i in range(len(raw_data['sessionResult']['leaderBoardLines'])):
    # if raw_data['sessionResult']['leaderBoardLines'][i]['currentDriver']['firstName'] == 'Joseph':
    #     print('you suck!')
    # else:
    if i < 1:
        j = raw_data['sessionResult']['leaderBoardLines'][i]['timing']['totalTime']
        # print('j',j)
        print(get_time(raw_data['sessionResult']['leaderBoardLines'][i]['timing']['totalTime']))
    else:
        # print('j',j)
        # print(raw_data['sessionResult']['leaderBoardLines'][i]['timing']['totalTime'])
        h = raw_data['sessionResult']['leaderBoardLines'][i]['timing']['totalTime'] - j
        # print('h',h)
        j = raw_data['sessionResult']['leaderBoardLines'][i]['timing']['totalTime']
        print(get_time(h))
    


