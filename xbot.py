from telegram import Update
from telegram.ext import Updater, MessageHandler, filters, ApplicationBuilder
import logging
import openai,hugface

#atekre
openai.api_key = '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'

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

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Initialize the Telegram bot
botapp = ApplicationBuilder().token('6307675210:AAHmUq1gTcYKYN-eYq3SbBtREppsvYhUHq8').build()
#updater = Updater('6274961154:AAG_G3E1mYVQ-AVL_YJUteIgmaUvWlzMxss', use_context=True)
#dispatcher = updater.dispatcher



# Register the message handler function
message_handler = MessageHandler(filters.TEXT, handle_message)
botapp.add_handler(message_handler)

# Start the bot
#updater.start_polling()
botapp.run_polling()