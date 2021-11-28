def welcome():
    return (
        "Welcome to Binance RACA notifier bot!\n\n"
        "Use /subscribe command to be notified when RACA is available on Binance.\n\n"
        "Notifications will be as bunch of spam messages, so make sure to set "
        "the most annoying custom ringtone you can find for this bot."
    )

def pretest():
    return (
            "The test will be started in 10 seconds.\n"
            "Make sure to exit the app so that you receive push notifications instead of in-app."
            )

def notification(link):
    return (
            "RACA is finally on Binance!\n\n"
            f"{ link }"
            )

def github():
    return (
            "You can check out the source code on Github: https://github.com/memreyagci/binance-raca-bot"
            )

def subscribed():
    return (
            "You are successfully subscribed. You will get lots of notifications when RACA is available on Binance.\n\n"
            "To test the notification, you can use /test command , and stop it with by simply blocking the bot.\n\n"
            "To stop the actual notifications when it happens, /unsubscribe or block the bot."
            )
