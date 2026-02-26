import os
import time
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.logging_config import get_logger

load_dotenv()


class BinanceClientError(Exception):
    pass


class BinanceClient:
    def __init__(self):
        self.logger = get_logger(__name__)

        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            self.logger.error("API key/secret missing in .env")
            raise BinanceClientError("API key/secret missing in .env")

        try:
            self.client = Client(api_key, api_secret, testnet=True)

            server_time = self.client.get_server_time()
            self.client.timestamp_offset = (
                server_time["serverTime"] - int(time.time() * 1000)
            )

            self.logger.info("Binance client initialized successfully (Testnet).")

        except Exception as e:
            self.logger.error(f"Failed to initialize Binance client: {e}")
            raise BinanceClientError(f"Initialization failed: {e}")

    def futures_create_order(self, **kwargs):
        self.logger.info(f"Request: futures_create_order {kwargs}")

        try:
            response = self.client.futures_create_order(
                **kwargs,
                recvWindow=10000  
            )

            self.logger.info(f"Response: {response}")
            return response

        except (BinanceAPIException, BinanceRequestException) as e:
            self.logger.error(f"Binance API error: {e}")
            raise BinanceClientError(f"Binance API error: {e}")

        except Exception as e:
            self.logger.error(f"Network/Unknown error: {e}")
            raise BinanceClientError(f"Network/Unknown error: {e}")

    def get_symbol_info(self, symbol):
        self.logger.info(f"Request: get_symbol_info {symbol}")

        try:
            info = self.client.futures_exchange_info()

            for s in info["symbols"]:
                if s["symbol"] == symbol:
                    self.logger.info(f"Response: {s}")
                    return s

            self.logger.warning(f"Symbol {symbol} not found in exchange info.")
            return None

        except (BinanceAPIException, BinanceRequestException) as e:
            self.logger.error(f"Binance API error: {e}")
            raise BinanceClientError(f"Binance API error: {e}")

        except Exception as e:
            self.logger.error(f"Network/Unknown error: {e}")
            raise BinanceClientError(f"Network/Unknown error: {e}")