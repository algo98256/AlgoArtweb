from telegram import Update
from telegram.ext import Updater, MessageHandler, filters, ApplicationBuilder
import logging
import hugface

#atekre
#openai.api_key = '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'

#def ajok(user_message):
    
#    return chatgpt_reply


async def handle_message(update: Update, context):
    # Get the user's message
    user_message = update.message.text

    # Forward the user's message to ChatGPT
    image_reply = hugface.genArt(user_message)
    #get_chatgpt_reply(user_message)
    #print(image_reply)
    #image_bytes = b.getbuffer().tobytes()
    # Send the reply back to the user
    await update.message.reply_photo(image_reply)