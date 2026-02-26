from bot.validators import validate_symbol, validate_side, validate_order_type, validate_quantity, validate_price
from bot.logging_config import get_logger

def place_order(client, symbol, side, order_type, quantity, price=None):
    logger = get_logger(__name__)
    try:
        validate_symbol(symbol)
        symbol_info = client.get_symbol_info(symbol)
        if not symbol_info:
            logger.error(f"Symbol not found on Binance Futures: {symbol}")
            raise ValueError(f"Symbol {symbol} not found on Binance Futures.")
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(order_type, price)
    except ValueError as ve:
        logger.error(f"Validation failed: {ve}")
        raise

    order_params = {
        'symbol': symbol,
        'side': side,
        'type': order_type,
        'quantity': float(quantity),
    }
    if order_type == 'LIMIT':
        order_params['price'] = float(price)
        order_params['timeInForce'] = 'GTC'

    try:
        response = client.futures_create_order(**order_params)
        result = {
            'orderId': response.get('orderId'),
            'status': response.get('status'),
            'executedQty': response.get('executedQty'),
            'avgPrice': response.get('avgPrice') or response.get('price')
        }
        logger.info(f"Order placed successfully: {result}")
        return result
    except Exception as e:
        logger.error(f"Order placement failed: {e}")
        raise
