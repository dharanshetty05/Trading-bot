from bot.client import get_client

def test_market_order():
    client = get_client()

    response = client.futures_create_order(
        symbol="BTCUSDT",
        side="BUY",
        type="MARKET",
        quantity=0.001
    )

    print("Order Response:")
    print(response)