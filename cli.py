import argparse
import sys
from bot.client import BinanceClient, BinanceClientError
from bot.orders import place_order
from bot.logging_config import get_logger

logger = get_logger(__name__)

def main():
    logger.info("\n" + "="*70)
    logger.info("NEW EXECUTION STARTED")
    logger.info("="*70)
    parser = argparse.ArgumentParser(description='Binance Futures Testnet Trading Bot')
    parser.add_argument('--symbol', required=True, help='Trading symbol, e.g. BTCUSDT')
    parser.add_argument('--side', required=True, choices=['BUY', 'SELL'], help='Order side')
    parser.add_argument('--order_type', required=True, choices=['MARKET', 'LIMIT'], help='Order type')
    parser.add_argument('--quantity', required=True, type=float, help='Order quantity')
    parser.add_argument('--price', type=float, help='Order price (required for LIMIT)')
    args = parser.parse_args()

    print(f"\nOrder Request Summary:")
    print(f"  Symbol:     {args.symbol}")
    print(f"  Side:       {args.side}")
    print(f"  Type:       {args.order_type}")
    print(f"  Quantity:   {args.quantity}")
    if args.order_type == 'LIMIT':
        print(f"  Price:      {args.price}")
    print()

    try:
        client = BinanceClient()
        response = place_order(
            client,
            args.symbol,
            args.side,
            args.order_type,
            args.quantity,
            price=args.price
        )
        print("SUCCESS: Order placed.")
        print(f"  orderId:     {response['orderId']}")
        print(f"  status:      {response['status']}")
        print(f"  executedQty: {response['executedQty']}")
        print(f"  avgPrice:    {response['avgPrice']}")
    except Exception as e:
        print(f"FAILURE: {e}")
        logger.exception(f"Order failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
