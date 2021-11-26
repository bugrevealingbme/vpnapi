import json
from aiohttp import ClientSession
import asyncio

async def vpngate():
    best_list = []
    normal_list = []
    async with ClientSession() as session:
        async with session.get('http://www.vpngate.net/api/iphone/',ssl=False) as response:
            _vpn_data = await response.text()
            vpn_data = _vpn_data.replace('\r','')
            servers = [line.split(',') for line in vpn_data.split('\n')]
            labels = servers[1]
            labels[0] = labels[0][1:]
            servers = [s for s in servers[2:] if len(s) > 1]
            for i in servers:
                a = {
                    labels[0]:i[0],
                    labels[1]:i[1],
                    labels[2]:i[2],
                    labels[3]:i[3],
                    labels[4]:i[4],
                    labels[5]:i[5],
                    labels[6]:i[6],
                    labels[7]:i[7],
                    labels[8]:i[8],
                    labels[9]:i[9],
                    labels[10]:i[10],
                    labels[11]:i[11],
                    labels[12]:i[12],
                    labels[13]:i[13],
                    labels[14]:i[14]
                    }
                if len(best_list) !=5:
                    best_list.append(a)
                else:
                    normal_list.append(a)
    return [best_list, normal_list]

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
data = loop.run_until_complete(vpngate())
print(json.dumps({'best':data[0],'normal':data[1]},indent=2))
