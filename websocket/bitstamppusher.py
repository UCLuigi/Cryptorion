import pusherclient
import sys
import time

# Add a logging handler so we can see the raw communication data
#import logging
#root = logging.getLogger()
#root.setLevel(logging.INFO)
#ch = logging.StreamHandler(sys.stdout)
#root.addHandler(ch)

global pusher

# We can't subscribe until we've connected, so we use a callback handler
# to subscribe when able

def callback1(data):
    print(' Data:: Bitcoin \n',data)

def callback2(data):
    print(' Data:: BTCXRP \n',data)

def callback3(data):
    print(' Data:: EthUSD \n',data)

def connect_handler(data):
    #channel = pusher.subscribe('live_trades')
    channel2 = pusher.subscribe('live_trades_xrpusd')
    #channel3 = pusher.subscribe('live_trades_ethusd')
    #channel.bind('trade', callback1)
    channel2.bind('trade2', callback2)
    #channel3.bind('trade3', callback3)
    print("hii \n \n \n", data)

appkey = "de504dc5763aeef9ff52"
pusher = pusherclient.Pusher(appkey)
pusher.connection.bind('pusher:connection_established', connect_handler)
pusher.connect()

while True:
    time.sleep(1)

print("finished")
