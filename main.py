import asyncio

class Bot:
    def __init__(self):
        pass

    async def run(self):
        print("✅ Bot started successfully on Render")
        await self.start()

    async def start(self):
        # yahan apna actual bot code daalo
        while True:
            await asyncio.sleep(10)
