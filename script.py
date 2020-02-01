from telethon import TelegramClient
import asyncio
import time
from telethon import events

api_id = '1011562'
api_hash = 'f7d23bea8adfcf4f849c97b5d96fee98'

client = TelegramClient('Iker_worker:', api_id, api_hash)

message = 'Sfarming test 1.'
start = '/start'
def main():

    client.start()
    
    @client.on(events.NewMessage(incoming=True))
    async def _(event):
        if event.is_private:
            time.sleep(5)  # pause for 1 second to rate-limit automatic replies
            await client.send_message(event.message.from_id, message)
            time.sleep(25)
            await client.send_message(event.message.from_id, start)
    client.run_until_disconnected()


if __name__ == '__main__':
    main()
    
