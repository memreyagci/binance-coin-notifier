import logging
import os
from time import sleep

import telegram
from telegram.ext import CommandHandler, Updater

from database import add_user, remove_user, check_if_user_exists, get_users, init_db

import texts
import announcement
API = os.environ.get("BINANCE_TELEGRAM_BOT_API")

KEYWORDS = [
        "RNDR",
        "RACA",
        "Radio",
        "Caca"
        ]

def add_handlers():
    # The commands used in Telegram that starts with '/'. eg. /subscribe
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("subscribe", subscribe))
    dispatcher.add_handler(CommandHandler("unsubscribe", unsubscribe))
    dispatcher.add_handler(CommandHandler("test", start_test_notification))

def start(update, context):
    tid = update.effective_user.id

    try:
        context.bot.send_message(
            chat_id=tid,
            text=texts.welcome(),
        )
        context.bot.send_message(
            chat_id=tid,
            text=texts.github(),
        )
    except telegram.error.Unauthorized:
        remove_user(tid)

def subscribe(update, context):
    tid = update.effective_user.id

    if check_if_user_exists(tid) == False:
        add_user(tid)
        context.bot.send_message(
            chat_id=tid,
            text=texts.subscribed(),
        )
    else:
        context.bot.send_message(
            chat_id=tid,
            text="You are already subscribed!",
        )

def unsubscribe(update, context):
    tid = update.effective_user.id

    if check_if_user_exists(tid) == True:
        remove_user(tid)
        context.bot.send_message(
            chat_id=tid,
            text="Unsubscribed! You won't get any notifications.",
        )
    else:
        context.bot.send_message(
            chat_id=tid,
            text="You are not subscribed.",
        )

def start_test_notification(update, context):
    context.bot.send_message(
            chat_id=update.effective_user.id,
            text=texts.pretest(),
            )
    sleep(10)
    for _ in range(20):
        context.bot.send_message(
                chat_id=update.effective_user.id,
                text="Test!",
                )
        sleep(1.5)

def update_job(context):
    driver = announcement.get_driver()
    announcements = announcement.get_all(driver)
    users = get_users()

    for a in announcements:
        found = announcement.check_keywords(a["title"], a["article"], KEYWORDS)
        if found == True:
            for _ in range(50):
                for user in users:
                    if check_if_user_exists(user[0]) == True:
                        context.bot.send_message(
                                chat_id=user[0],
                                text=texts.notification(a["link"]),
                                )
                    else:
                        break
                sleep(1.5)     

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    init_db()

    updater = Updater(token=API)
    dispatcher = updater.dispatcher

    add_handlers()

    updater.start_polling()
    updater.job_queue.run_repeating(update_job, interval=600, first=10)
    updater.idle()
