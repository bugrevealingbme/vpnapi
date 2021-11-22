import csv
import json
from requests import Session

def get_proxy(data,key):
    liste = []
    for i in data:
        try:
            if int(int(i['Speed'])/int(i['NumVpnSessions'])) == int(key):
                liste.append(i)
        except:
            pass
    return liste



def best_proxy_finder(data):
    speed_list = []
    best_list = []
    normal_list = []
    for proxies in data:
        try:
            speed_list.append(int(int(proxies['Speed'])/int(proxies['NumVpnSessions'])))
        except:
            pass
    speed_list.sort(reverse=True)
    for i in speed_list[1:]:
        for b in get_proxy(data,i):
            if b not in best_list:
                if len(best_list) != 5:
                    best_list.append(b)
                else:
                    normal_list.append(b)
    return [best_list,normal_list]



def get_csv_data_from_api():
    session = Session()
    with open('data.csv','w',encoding='utf-8', newline='') as f:
        f.write(session.get('http://www.vpngate.net/api/iphone/').text[15:-5])
    return csv_to_json()


def csv_to_json():
    liste = []
    with open('data.csv','r') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            liste.append(row)
    return best_proxy_finder(liste)


data = get_csv_data_from_api()
best = data[0]
normal = data[1]

print(json.dumps({'best':best, 'normal':normal},indent=2))
