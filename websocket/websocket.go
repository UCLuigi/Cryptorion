package main

import (
	"context"
	"log"
	"time"

	"github.com/bitfinexcom/bitfinex-api-go/v2"
	"github.com/bitfinexcom/bitfinex-api-go/v2/websocket"
)

func main() {
	c := websocket.New()

	err := c.Connect()
	if err != nil {
		log.Fatal("Error connecting to web socket : ", err)
	}

	ctx, cxl2 := context.WithTimeout(context.Background(), time.Second*75)
	defer cxl2()

	go listen(c, ctx, bitfinex.TradingPrefix+bitfinex.BTCUSD, bitfinex.OneMinute)
	go listen(c, ctx, bitfinex.TradingPrefix+bitfinex.ETHUSD, bitfinex.OneMinute)
	go listen(c, ctx, bitfinex.TradingPrefix+bitfinex.LTCUSD, bitfinex.OneMinute)

}

func listen(c *websocket.Client, ctx context.Context, token string, time bitfinex.CandleResolution) {

	_, err := c.SubscribeCandles(ctx, bitfinex.TradingPrefix+bitfinex.BTCUSD, bitfinex.OneMinute)
	if err != nil {
		log.Fatal(err)
	}
	for obj := range c.Listen() {
		switch obj.(type) {
		case error:
			log.Printf("channel closed: %s", obj)
			break
		default:
		}
		log.Printf("MSG RECV: %#v", obj)
	}
}
