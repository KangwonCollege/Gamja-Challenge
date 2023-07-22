import aiofiles
import asyncio


async def read_file(file_path):
    async with aiofiles.open(file_path, mode="r") as file:
        content = await file.read()
        return content
