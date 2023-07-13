import nest_asyncio
from telegram import Update
nest_asyncio.apply()
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
#from telegram.utils.asyncio import run_coroutine_threadsafe
import asyncio,threading
import subprocess,aibot,os

app = FastAPI()
athd = None

#3991
#loop = asyncio.get_event_loop()
class TelegramUpdate(BaseModel):
    update_id: int
    message: dict


@app.get("/")
async def root():
    #portin = os.environ.get("UVICORN_PORT")
    #print(f"started: {portin}")
    return f"HELLOWORLD , WELCOME TO MYSPACES, Great love from space! 🚀: man"

def start_bot():
    print("bot started")
    #loop = asyncio.new_event_loop()
    #loop.create_task(bot.main())
    #bot.main()

@app.on_event("startup")
async def startup_event():
    #portin = os.environ.get("UVICORN_PORT")
    #print(f"started: {portin}")
    #aibot.logs.append(f"web event started")
    await aibot.main()
   #threading.Thread(target=start_bot).start()
    #loop = asyncio.get_event_loop()
    #(bot.main()))
    #app.bg_task = asyncio.create_task(start_bot())
print("event loop ok")
#asyncio.set_event_loop(loop)
#loop.run_forever()
@app.get("/mefile")#, response_class=HTMLResponse)
async def get_index():
    return "okay index"
    # Load the index.html file
    #with open("hi.mp3") as f:
    #    index_html = f.read()
    #if index_html == None:
    #    return "file error"
    #else:
    #    return index_html
@app.post("/tbard/webhook")
async def telegram_webhook(request: Request):
    #aibot.logs.append(f"gotten data")
    json_req = await request.json()
    #aibot.logs.append(f"gotten data {json_req}")
    update_in = Update.de_json(json_req, aibot.tapp.bot)
    #update_in = await abot.get_updates(limit=100)
    updates_len = 0#len(update_in)
    #print(update)
    #aibot.logs.append(update_in)
    #aibot.logs.append(":update_ends_here:")
    #aibot.logs.append(f"updates size: {updates_len}")
    await aibot.tapp.process_update(update_in)
    #asyncio.create_task((aibot.tapp.process_update(update_in)))
    #handle_update(update)
    return {"status": "ok"}

#asyncio.set_event_loop(loop)

#import uvicorn
#uvicorn.run(app, host="0.0.0.0", port=8080)
#asyncio.create_task(start_bot())