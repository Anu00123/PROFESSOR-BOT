import re, asyncio, time, shutil, psutil, os, sys
from pyrogram import Client, filters, enums
from pyrogram.types import ChatJoinRequest, message, *
from info import BOT_START_TIME, ADMINS
from utils import humanbytes  





gif = [
    'https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4',
    'https://telegra.ph/file/03c6e49bea9ce6c908b87.mp4',
    'https://telegra.ph/file/9ebf412f09cd7d2ceaaef.mp4',
    'https://telegra.ph/file/293cc10710e57530404f8.mp4',
    'https://telegra.ph/file/506898de518534ff68ba0.mp4',
    'https://telegra.ph/file/dae0156e5f48573f016da.mp4',
    'https://telegra.ph/file/3e2871e714f435d173b9e.mp4',
    'https://telegra.ph/file/714982b9fedfa3b4d8d2b.mp4',
    'https://telegra.ph/file/876edfcec678b64eac480.mp4',
    'https://telegra.ph/file/6b1ab5aec5fa81cf40005.mp4',
    'https://telegra.ph/file/b4834b434888de522fa49.mp4'
]




@Client.on_message(filters.private & filters.command("status") & filters.user(ADMINS))          
async def stats(bot, update):
    currentTime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - BOT_START_TIME))
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    ms_g = f"""<b><u>Bot Status</b></u>

Uptime: <code>{currentTime}</code>
CPU Usage: <code>{cpu_usage}%</code>
RAM Usage: <code>{ram_usage}%</code>
Total Disk Space: <code>{total}</code>
Used Space: <code>{used} ({disk_usage}%)</code>
Free Space: <code>{free}</code> """

    msg = await bot.send_message(chat_id=update.chat.id, text="__Processing...__", parse_mode=enums.ParseMode.MARKDOWN)         
    await msg.edit_text(text=ms_g, parse_mode=enums.ParseMode.HTML)
    
@Client.on_message(filters.command("restart") & filters.user(ADMINS))
async def stop_button(bot, message):
    msg = await bot.send_message(text="**🔄 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...**", chat_id=message.chat.id)       
    await asyncio.sleep(3)
    await msg.edit("**✅️ 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴**")
    os.execl(sys.executable, sys.executable, *sys.argv)


@Client.on_chat_join_request(filters.group | filters.channel)
async def approve(client, message: ChatJoinRequest):
    chat = message.chat
    user = message.from_user
    try:
        await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
        add_group(chat.id)
        img = random.choice(gif)
        await client.send_video(chat_id=user.id, video=img)
        add_user(user.id)
    except Exception as err:
        print(str(err))


