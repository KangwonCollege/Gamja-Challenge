import discord
import asyncio
from aiohttp import web

routes = web.RouteTableDef()
bot: discord.Client


@routes.get('/')
async def hello_world(request):
    return web.Response(text="Hello World")
