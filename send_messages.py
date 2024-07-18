import asyncio
from telegram import Bot

async def send_message_to_group():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    bot_token = '7111699077:AAE-eiXfPfCTXnJLd4Jkry1Xgc0mKA_wotQ'
    
    # Replace 'GROUP_CHAT_ID' with the actual group chat ID
    group_chat_id = '-1001715391741'
    
    # The message you want to send
    message = 'Hello, this is a message from your bot!'

    # Create a Bot instance
    bot = Bot(token=bot_token)

    try:
        # Send the message
        await bot.send_message(chat_id=group_chat_id, text=message)
        print("Message sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the async function
asyncio.run(send_message_to_group())