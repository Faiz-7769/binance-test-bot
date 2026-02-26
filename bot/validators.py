def validate_symbol(symbol: str):
    if not isinstance(symbol, str) or not symbol.strip():
        raise ValueError('Symbol must be a non-empty string.')
    if symbol != symbol.upper():
        raise ValueError('Symbol must be uppercase.')


def validate_side(side: str):
    if side not in ('BUY', 'SELL'):
        raise ValueError("Side must be 'BUY' or 'SELL'.")


def validate_order_type(order_type: str):
    if order_type not in ('MARKET', 'LIMIT'):
        raise ValueError("Order type must be 'MARKET' or 'LIMIT'.")


def validate_quantity(quantity):
    try:
        q = float(quantity)
        if q <= 0:
            raise ValueError
    except Exception:
        raise ValueError('Quantity must be a positive number.')


def validate_price(order_type: str, price):
    if order_type == 'LIMIT':
        if price is None:
            raise ValueError('Price is required for LIMIT orders.')
        try:
            p = float(price)
            if p <= 0:
                raise ValueError
        except Exception:
            raise ValueError('Price must be a positive number for LIMIT orders.')
    # For MARKET, price is ignored
