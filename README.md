# Binance Futures Testnet Trading Bot

This is a command-line trading bot for Binance Futures Testnet, written in Python.

## Features
- Place MARKET and LIMIT orders via CLI
- Input validation for all order parameters
- Logging to both console and `trading_bot.log`
- Handles API/network errors gracefully

## Setup

1. **Clone this repo and install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Create a `.env` file at the project root:**
   ```ini
   BINANCE_API_KEY=your_testnet_api_key
   BINANCE_API_SECRET=your_testnet_api_secret
   ```
   Get your keys from https://testnet.binancefuture.com/

3. **Run the CLI:**
   - Market order:
     ```sh
     python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.01
     ```
   - Limit order:
     ```sh
     python cli.py --symbol BTCUSDT --side BUY --order_type LIMIT --quantity 0.01 --price 30000
     ```

## Notes
- All logs (API requests, responses, errors) go to `trading_bot.log` in the current directory.
- Only works on Binance Futures Testnet (not mainnet).
- For best results, test with MARKET orders first.

## Requirements
- Python 3.10+
- `python-binance`, `python-dotenv`

---

**This project is for educational/testing purposes only. Made for an company internship assignment.**
