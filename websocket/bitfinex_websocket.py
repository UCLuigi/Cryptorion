import websocket
import json
try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message2(ws, message):
    print("Hipso     ",message)

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        #demand = {'event': 'subscribe', 'channel': 'trades', 'pair': 'BTCUSD'}
        demand2 = {'event': 'subscribe', 'channel': 'trades', 'pair': 'ETHBTC'}
        demand3 = {'event': 'subscribe', 'channel': 'trades', 'pair': 'ETHUSD'}
        demand4 = {'event': 'subscribe', 'channel': 'trades', 'pair': 'LTCUSD'}
        demand5 = {'event': 'subscribe', 'channel': 'trades', 'pair': 'LTCBTC'}
        #demand = json.dumps(demand)
        demand2 = json.dumps(demand2)
        demand3 = json.dumps(demand3)
        demand4 = json.dumps(demand4)
        demand5 = json.dumps(demand5)
        for i in range(10): #This should be coverted to while True:
            #ws.send(demand)
            ws.send(demand2)
            ws.send(demand3)
            ws.send(demand4)
            time.sleep(7)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    #websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://api.bitfinex.com/ws/2",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
