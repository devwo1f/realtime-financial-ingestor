import websocket
import json
import pandas as pd
import time
from datetime import datetime

# 1. Define the Coinbase WebSocket URL
SOCKET = "wss://ws-feed.exchange.coinbase.com"

# 2. Define what happens when we get data
def on_message(ws, message):
    data = json.loads(message)
    
    # We only care about "ticker" messages (actual trades)
    if 'price' in data and 'product_id' in data:
        price = data['price']
        crypto = data['product_id']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Print to console (so we know it's working)
        print(f"[{timestamp}] {crypto}: ${price}")
        
        # --- HERE IS WHERE WE WOULD SAVE TO CSV (Step 3) ---
        # We will add the CSV saving logic in the next step.

def on_error(ws, error):
    print(f"Error occurred: {error}")

def on_close(ws, close_status_code, close_msg):
    print("### Connection Closed ###")

def on_open(ws):
    print("Connection Opened! Subscribing to Bitcoin (BTC-USD)...")
    # Subscribe to Bitcoin trades
    subscribe_message = {
        "type": "subscribe",
        "channels": [{"name": "ticker", "product_ids": ["BTC-USD"]}]
    }
    ws.send(json.dumps(subscribe_message))

# 3. The "Proud" Part: Auto-Reconnection Logic
def start_pipeline():
    while True:
        try:
            ws = websocket.WebSocketApp(
                SOCKET,
                on_open=on_open,
                on_close=on_close,
                on_message=on_message,
                on_error=on_error
            )
            ws.run_forever()  # Keep the connection open
        except Exception as e:
            print(f"Connection failed: {e}")
        
        # If the connection drops, wait 5 seconds and try again
        print("Reconnecting in 5 seconds...")
        time.sleep(5)

if __name__ == "__main__":
    start_pipeline()