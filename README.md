A Telegram bot that notifies you when the coin wanted is announced on Binance 

Configuration (in *config.py*):

```python
bot_api = "" # API received from BotFather of Telegram
db_url = "" # Database URL and credentials
coin_keywords = [] # keywords to search for the coin. For example, for RACA: 
                   # "RNDR",
                   # "RACA",
                   # "Radio",
                   # "Caca"
```

To run:

```python
python bot.py
```
