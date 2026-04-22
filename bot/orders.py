from bot.client import get_client
import time

def test_market_order():
    client = get_client()

    response = client.futures_create_order(
        symbol="BTCUSDT",
        side="BUY",
        type="MARKET",
        quantity=0.001
    )

    print("Initial Response:")
    print(response)

    order_id = response["orderId"]

    time.sleep(2)

    order_status = client.futures_get_order(
        symbol="BTCUSDT",
        orderId=order_id
    )

    print("\nUpdated Order Status:")
    print(order_status)