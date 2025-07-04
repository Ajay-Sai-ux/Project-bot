import logging
from app.core.kite import kws


# WebSocket event callbacks
def on_ticks(ws, ticks):
    logging.debug("Ticks: {}".format(ticks))
    # print("Received ticks:", ticks)
    

def on_connect(ws, response):
    print("WebSocket connected.")
    ws.subscribe([738561, 5633])  # Example instrument tokens
    ws.set_mode(ws.MODE_FULL, [738561])

def on_close(ws, code, reason):
    print(f"WebSocket closed with code={code}, reason={reason}")
    ws.stop()

def start_kite_ws():
    # Assign the callbacks
    kws.on_ticks = on_ticks
    kws.on_connect = on_connect
    kws.on_close = on_close

    # Connect (blocking call)
    kws.connect(threaded=True)  # Run in a background thread


