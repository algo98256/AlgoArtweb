from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo, InlineKeyboardButton, MenuButton, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ApplicationBuilder, MessageHandler, filters
import asyncio
#from detamod import Detaman
from deta import Deta
from tkuser import Tkuser
from tkman import Tkman
from tokeni import AToken

import bbot,json

is_done = False
logs=list()
#logs.append("mylogs\n")
service_name = "atekretestman"
active_cmd = {}
tasks_made = {}
token_server = "https://tokener-1-r6555868.deta.app"
deta_data_token = "d0xuy41v68a_97QYgZqGPUiwUPVAd6TD4kVPy6rGQnG4"
jwt_secret_key = "iwasbornandraisedbutcutfromadifferentcloth,lifewasn'tfunnywhenbeingcalledbrokewasajoke"
token_service = "algoaibard"#str()
tele_token = "6307675210:AAHmUq1gTcYKYN-eYq3SbBtREppsvYhUHq8"#str()
#detaguy = Detaman(deta_data_token,"tokens_db")
detaguy = Deta(deta_data_token)
deta_userz = detaguy.Base("ayeuserz")
deta_tokenz = detaguy.Base("ayetokenz")

tapp = ApplicationBuilder().token(tele_token).build()
#asyncio.run(tapp.initialize())
async def askToken(ask_txt,update):
    print(update)
    print("\n\n\n")
    button1 = InlineKeyboardButton(text='Get token', web_app=WebAppInfo(token_server))
    button2 = InlineKeyboardButton(text='write token',callback_data = "writetoken")
    keyboard = InlineKeyboardMarkup([[button1,button2]])
    await update.message.reply_text(ask_txt, reply_markup=keyboard)

async def processService(update,last_update,context):
    txt = update.message.text
    chatid = update.message.chat_id
    #print(f"processing service: {txt}")
    #asyncio.create_task(bardbot.bardChat(txt))
    #bard_reply = 
    await bbot.handle_message(update,context)
    #print(bard_reply)
    #await update.message.reply_text(bard_reply)
    #await context.bot.edit_message_text(chat_id=chatid,message_id = last_update.message_id,text=bard_reply)

async def processToken(update):
    cid = update.effective_user.id
    tk = update.message.text
    print(f"processing token: {tk}")
    ausr = Tkuser(cid,service_name,deta_userz)
    global detaguy
    atoken = AToken(tk,jwt_secret_key)
    token_data = atoken.getId()
    #token_data = tokener.decode_token(tk,jwt_secret_key)
    if token_data == None:
        #await update.message.reply_text(f'sorry, token is expired or not good but you can make another one')
        await askToken("sorry, your token is faulty",update)
    else:
        #put_res = detaguy.putToken(cid,token_service,token_data,token_exp[extimestamp])
        tk_cid = Tkman(token_data,deta_tokenz)
        tk_stat = tk_cid.isValid()
        if tk_stat == None:
                await askToken("sorry, your token is off: ",update)
        elif tk_stat == False:
                await askToken("sorry, you token has already been used: ",update)
        elif tk_stat == True:
                tk_cid.validate()
                ausr.addUser(atoken,"process_service")
                await update.message.reply_text("You are free to use this service")
       # if put_res == None:
       #     await update.message.reply_text(f'token is bad, create another one')
       # else:
           # active_cmd[cid] = "process_service"
        #    await update.message.reply_text(f'your token is good but only for 1 day')

async def authToken(update):
    print('authing user')

async def chatMan(update,context):
    print("chatter")
    cid = update.effective_user.id
    print(f"cid is {cid}")
    last_update = await update.message.reply_text(f'please world, wait katono......')
    print(f"\n\nuser id is: {cid}")
    #await asyncio.sleep(30)
    print(f"\n\nlets go eyes: {cid}\n")
    cidman = Tkuser(cid,service_name,deta_userz)
    iactive_cmd = cidman.getCmd()
    #if active_cmd[cid]== "process_token":
    if iactive_cmd == None or iactive_cmd=="process_token":
        print("processing token")
        await processToken(update)
    #elif active_cmd[cid] == "process_service":
    elif iactive_cmd == "process_service":
        #await processService(last_update,context)
        await processService(update,last_update,context)
        print("service started")
    else:
        print("token error")
    is_done = True

async def chatManCmd(update,context):
    #logs.append("processing message")
    #loop = asyncio.get_event_loop()
    #asyncio.run(await chatMan(update,context))
    #asyncio.create_task(chatMan(update,context))
    await chatMan(update,context)

async def callback(update,context):
        query = update.callback_query
        cid = query.from_user.id
        cidman = Tkuser(cid,service_name,deta_userz)
        iactive_cmd = cidman.getCmd()
        print(query)
        if query.data=="writetoken":
            print("\n\n")
            #print(active_cmd[cid])
            print(iactive_cmd)
            #active_cmd[cid]= "process_token"
            await query.message.reply_text("please write token and send to me")
        else:
            await query.message.reply_text("error callback")

async def writeToken(update, context):
    print(update.message.text)



async def startCmd(update,context):
    cid = update.effective_user.id
    print("start started")
    #logs.append("start chat up")
    cidman = Tkuser(cid,service_name,deta_userz)
    cmd = cidman.getCmd()
    print(update)
    if cmd == None:
        print("user error")
        await askToken("sorry, you are out of tokens: ",update)
    else:
        token_id = cidman.getTokenID()
        if token_id == None:
            await askToken("sorry, you don't have any token: ",update)
        else:
            tk_cid = Tkman(token_id,deta_tokenz)
            tk_stat = tk_cid.isValid()
            if tk_stat == None:
                await askToken("sorry, you token is off: ",update)
            #if tk_stat == False:
            #    await askToken("sorry, you token has already been used: ",update)
            #if tk_stat == True:
            else:
                await update.message.reply_text("You are free to use this service")


async def start(update, context):
    print("start update")
    cid = update.effective_user.id
    #kb = [
    #    [KeyboardButton("Show me Google!", web_app=WebAppInfo("https://google.com"))]
    #]
   # await update.message.reply_text(f'pliz {cid} wait katono')
   # await asyncio.sleep(30)
    #asyncio.create_task(startCmd(update,context))
    #for webhooks
    await startCmd(update,context)
    print("\n\nok off we go\n\n")


async def runCmd(update,context):
    cid = update.effective_user.id
    task_made = asyncio.create_task(start(update,context))
    await task_made


#async 
async def main():
    await tapp.initialize()
    #loop = asyncio.new_event_loop()
    #asyncio.set_event_loop(loop)
    #global tapp
    # Set up your bot token and create an Updater instance
    #tapp = 
    #updater = Updater(token=).Updater()#, use_context=True)
    #dispatcher = updater.dispatcher

    # Add command handlers
    #start_handler = CommandHandler('start', startCmd)
    start_handler = CommandHandler('start', start)
    msg_handler = MessageHandler(filters.TEXT,callback=chatManCmd)
    tapp.add_handler(start_handler)
    tapp.add_handler(msg_handler)

    # Add callback query handler for button clicks
    callback_handler = CallbackQueryHandler(callback)
    tapp.add_handler(callback_handler)
    webhook_url = "https://artekreartwh-1-k6224123.deta.app/tbard/webhook"
    abot = tapp.bot#
    print(abot)
    #update = Update.de_json(json.loads('{"update_id":12345}'), tapp.bot)
    #print(update)
    await abot.set_webhook(webhook_url)
    
    #await abot.deleteWebhook()
    #update_in = await abot.get_updates(limit=100)
    #updates_len = len(update_in)
    #print(update_in)
    
    #await update_in[(updates_len-1)].message.reply_text("welcome home budy")
    #await chatMan(update_in[(updates_len-1)],None)
    #await tapp.process_update(update_in[(updates_len-1)])
    #while True:
    #    if is_done == True:
    #        print("all well")
    #        break
    #print("update finished")
    #tapp.bot = bot
    #webin = await xbot.getWebhookInfo()
    #tapp.bot = bot
    #logs.append(str(webin))
    #print(f"logs {logs}")
    #print(f"info: {str(webin)}")
    # Start the bot
    #app.run_polling()
    #updater.idle()
    #loop = asyncio.get_event_loop()
    #loop.run_forever()

#if __name__ == '__main__':
#asyncio.run(main())
