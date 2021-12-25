from pyrogram import *
from pyrogram import Client , filters
from deep_translator import GoogleTranslator

bot = Client(
    session_name= 'robot' ,
    api_id= 8783612 ,
    api_hash= '559dc5515a4d6bfbe7faf1e9f5ea259c' ,
    bot_token= '2126514775:AAFcvKybu5NwAcX_yXHnYmudAcnsvFRqSqg'

)



@bot.on_message( filters.text ,group=1)
def trans (client, message):
    # print (message)
    
    text = message.text
    if text.startswith("/tr_fa "):
        text = text.replace("/tr_fa" , "")
        tran = GoogleTranslator('auto' , 'fa')
        trased = tran.translate(text)
        message.reply_text(trased)
    
    if text.startswith("/tr_en "):
        text = text.replace("/tr_en" , "")
        tran = GoogleTranslator('auto' , 'en')
        trased = tran.translate(text)
        message.reply_text(trased)

    if text.startswith("/about"):

        message.reply_text("محمد جواد محد زاده بدو فرار کن")


bot.run()
