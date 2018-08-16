import json
from websocket import create_connection
import time


ws1 = create_connection('wss://api.bitfinex.com/ws/2')
ws2 = create_connection('wss://api.bitfinex.com/ws/2')


demand = {'event': 'subscribe', 'channel': 'trades', 'pair': 'BTCUSD'}
demand2 = {'event': 'subscribe', 'channel': 'trades', 'pair': 'ETHBTC'}
demand3 = {'event': 'subscribe', 'channel': 'trades', 'pair': 'ETHUSD'}
demand4 = {'event': 'subscribe', 'channel': 'trades', 'pair': 'LTCUSD'}
demand5 = {'event': 'subscribe', 'channel': 'trades', 'pair': 'LTCBTC'}
demand6 = {'event': 'subscribe', 'channel': 'trades', 'pair': 'XRPUSD'}
demand7 = {'event': 'subscribe', 'channel': 'trades', 'pair': 'XRPBTC'}
demand8 = {'event': 'subscribe', 'channel': 'trades', 'pair': 'BCHUSD'}
demand9 = {'event': 'subscribe', 'channel': 'trades', 'pair': 'EOSBTC'}
demand10 = {'event': 'subscribe', 'channel': 'trades', 'pair': 'EOSUSD'}
demand11 = {'event': 'subscribe', 'channel': 'trades', 'pair': 'IOTBTC'}



ws1.send(json.dumps(demand1))
ws2.send(json.dumps(demand2))
ws2.send(json.dumps(demand6))


store_btc_p = []
store_btc_v = []

store_eth_p = []
store_eth_v = []

btc_p_c = []

i = 0
while True:
    i += 1
    result = ws1.recv()
    result2 = ws2.recv()
    result = json.loads(result)
    result2 = json.loads(result2)
    if type(result) == list:
        if len(result) == 3:
            if result[1] == 'te':
                print(i, ". What was received pair: ETHUSD ", result[2][2],' ',result[2][3])
                store_eth_p.append(result[2][3])
                store_eth_v.append(result[2][2])
        if len(result2) == 3:
            if result2[1] == 'te':
                print(i, ". What was received pair: BTCUSD ", result2[2][2],' ',result2[2][3])
                store_btc_p.append(result2[2][3])
                store_btc_v.append(result2[2][2])
                if len(store_btc_p) > 1:
                    change_p = (store_btc_p[-1] - store_btc_p[-2])/store_btc_p[-2]
                    if len(store_btc_v) % 52 == 0:
                        simple_stat = sum(store_btc_v[-51:])
                        print("\n \n --- Growth mean --- ", sum(btc_p_c)/len(btc_p_c))
                        print("\n \n------------sum last 51 trans: ",simple_stat, ' -----------\n \n' )
                    change_p = 100*(store_btc_p[-1] - store_btc_p[-2])/store_btc_p[-2]
                    btc_p_c.append(change_p)
                    print("Growth price", change_p)

    time.sleep(1)

ws.close()
