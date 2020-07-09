#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import logging

from telegram.ext import Updater, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

class Reading:
    def __init__(self, title, link, skippable):
        self.title = title
        self.link = link
        self.skippable = skippable
readings = [
    Reading("A Quick Summary of Philippians 4:10-23", "https://ymi.today/2019/05/ymi-reading-philippians-summary-6-a-quick-summary-of-philippians-4-10-23/", True),
    Reading("All in One Family", "https://ymi.today/2019/05/ymi-reading-philippians-day-30-all-in-one-family/", False),
    Reading("How Much Are You Willing to Give?", "https://ymi.today/2019/05/ymi-reading-philippians-day-29-how-much-are-you-willing-to-give/", False),
    Reading("The Gift of Generosity", "https://ymi.today/2019/05/ymi-reading-philippians-day-28-the-gift-of-generosity/", False),
    Reading("What Gives You Strength?", "https://ymi.today/2019/05/ymi-reading-philippians-day-27-what-gives-you-strength/", False),
    Reading("Do You Have Enough?", "https://ymi.today/2019/05/ymi-reading-philippians-day-26-do-you-have-enough/", False),
    Reading("YMI Reading Philippians 3rd Lockscreen", "https://ymi.today/2019/05/ymi-reading-philippians-lockscreen-3/", False),
    Reading("A Quick Summary of Philippians 4:4-9", "https://ymi.today/2019/05/ymi-reading-philippians-summary-5-a-quick-summary-of-philippians-4-4-9/", True),
    Reading("What’s Directing Your Thoughts?", "https://ymi.today/2019/05/ymi-reading-philippians-day-25-whats-directing-your-thoughts/", False),
    Reading("Rest in God’s Peace", "https://ymi.today/2019/05/ymi-reading-philippians-day-24-rest-in-gods-peace/", False),
    Reading("How to Overcome Anxiety", "https://ymi.today/2019/05/ymi-reading-philippians-day-23-how-to-overcome-anxiety/", False),
    Reading("Having Gentle Hands", "https://ymi.today/2019/04/ymi-reading-philippians-day-22-having-gentle-hands/", False),
    Reading("When You Don’t Feel Like Rejoicing", "https://ymi.today/2019/04/ymi-reading-philippians-day-21-when-you-dont-feel-like-rejoicing/", False),
    Reading("A Quick Summary of Philippians 3:7-4:3", "https://ymi.today/2019/04/ymi-reading-philippians-summary-4-a-quick-summary-of-philippians-3-7-4-3/", True),
    Reading("Work Through Your Conflicts", "https://ymi.today/2019/04/ymi-reading-philippians-day-20-work-through-your-conflicts/", False),
    Reading("Live for Our True Home", "https://ymi.today/2019/04/ymi-reading-philippians-day-19-live-for-our-true-home/", False),
    Reading("Who Are You Following?", "https://ymi.today/2019/04/ymi-reading-philippians-day-18-who-are-you-following/", False),
    Reading("What Are You Setting Your Eyes On?", "https://ymi.today/2019/04/ymi-reading-philippians-day-17-what-are-you-setting-your-eyes-on/", False),
    Reading("Let’s Get to Know Christ", "https://ymi.today/2019/04/ymi-reading-philippians-day-16-lets-get-to-know-christ/", False),
    Reading("YMI Reading Philippians 2nd Lockscreen", "https://ymi.today/2019/04/ymi-reading-philippians-lockscreen-2/", True),
    Reading("A Quick Summary of Philippians 2:14-3:6", "https://ymi.today/2019/04/ymi-reading-philippians-summary-3-a-quick-summary-of-philippians-2-14-3-6/", True),
    Reading("Are you a Good Christian?", "https://ymi.today/2019/04/ymi-reading-philippians-day-15-are-you-a-good-christian/", False),
    Reading("Watch Out for the Signs", "https://ymi.today/2019/04/ymi-reading-philippians-day-14-watch-out-for-the-signs/", False),
    Reading("A Leader Who Takes Risks", "https://ymi.today/2019/04/ymi-reading-philippians-day-13-a-leader-who-takes-risks/", False),
    Reading("A Leader Who Genuinely Cares", "https://ymi.today/2019/04/ymi-reading-philippians-day-12-a-leader-who-genuinely-cares/", False),
    Reading("The Secret to Not Complaining", "https://ymi.today/2019/04/ymi-reading-philippians-day-11-the-secret-to-not-complaining/", False),
    Reading("A Quick Summary of Philippians 1:29-2:13", "https://ymi.today/2019/04/ymi-reading-philippians-summary-2-a-quick-summary-of-philippians-1-29-2-13/", True),
    Reading("Should We Earn Our Salvation?", "https://ymi.today/2019/04/ymi-reading-philippians-day-10-should-we-earn-our-salvation/", False),
    Reading("Suffer Now, Glory Later", "https://ymi.today/2019/04/ymi-reading-philippians-day-9-suffer-now-glory-later/", False),
    Reading("Walking in Christ’s Humility", "https://ymi.today/2019/04/ymi-reading-philippians-day-8-walking-in-christs-humility/", False),
    Reading("Walking in Unity", "https://ymi.today/2019/04/ymi-reading-philippians-day-7-walking-in-unity/", False),
    Reading("The Privilege of Suffering for Christ", "https://ymi.today/2019/04/ymi-reading-philippians-day-6-the-privilege-of-suffering-for-christ/", False),
    Reading("YMI Reading Philippians Week 1’s Lockscreen", "https://ymi.today/2019/04/ymi-reading-philippians-lockscreen-week-1/", True),
    Reading("A Quick Summary of Philippians 1:1-28", "https://ymi.today/2019/04/ymi-reading-philippians-summary-1-a-quick-summary-of-philippians-11-27/", True),
    Reading("Are You Making Excuses for Your Sin?", "https://ymi.today/2019/04/ymi-reading-philippians-day-5-are-you-making-excuses-for-your-sin/", False),
    Reading("What Are You Living For?", "https://ymi.today/2019/04/ymi-reading-philippians-day-4-what-are-you-living-for/", False),
    Reading("Are You Afraid of Sharing the Gospel?", "https://ymi.today/2019/04/ymi-reading-philippians-day-3-are-you-afraid-of-sharing-the-gospel/", False),
    Reading("What Does It Mean to Love?", "https://ymi.today/2019/04/ymi-reading-philippians-day-2-what-does-it-mean-to-love/", False),
    Reading("No Ordinary Fellowship", "https://ymi.today/2019/04/ymi-reading-philippians-day-1-no-ordinary-fellowship/", False)
]
readings.reverse()

class BotData:
    def __init__(self, chat_id, reading_index):
        self.chat_id = chat_id
        self.reading_index = reading_index

def start(update, context):
    update.message.reply_text('Hi! Use /startplan to start a daily Phillippians plan, and /stopplan to stop it :)')

def send_plan_message(context):
    job = context.job
    reading_index = context.job.context.reading_index
    if reading_index < len(readings):
        reading = readings[reading_index]
        context.job.context.reading_index += 1
        context.bot.send_message(job.context.chat_id, text=reading.title + " - " + reading.link)
        if context.job.context.reading_index == len(readings):
            job.schedule_removal()
            context.bot.send_message(job.context.chat_id,
                                     text="Great! You've finished! Give yourself a pat on the back :]")
        elif reading.skippable:
            send_plan_message(context)

def start_plan(update, context):
    chat_id = update.message.chat_id
    reading_index = 0
    bot_data = BotData(chat_id, reading_index)

    # Add job to queue and stop current one if already started
    if 'job' in context.chat_data:
        old_job = context.chat_data['job']
        old_job.schedule_removal()

    update.message.reply_text("Plan successfully started! Let's do this!")
    context.job_queue.run_once(send_plan_message, 0, context=bot_data)
    new_job = context.job_queue.run_daily(send_plan_message,
                                          time=datetime.datetime.strptime('9:00AM', '%I:%M%p').time(),
                                          context=bot_data)
    context.chat_data['job'] = new_job

    send_plan_message(context)

def stop_plan(update, context):
    """Remove the job if the user changed their mind."""
    if 'job' not in context.chat_data:
        update.message.reply_text("Hmm, I didn't find an active plan. ?_?")
        return

    job = context.chat_data['job']
    job.schedule_removal()

    update.message.reply_text('Plan stopped D:')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("INSERT_TOKEN_HERE", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("startplan", start_plan,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("stopplan", stop_plan, pass_chat_data=True))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()