import discord
import asyncio
from aiohttp import web

routes = web.RouteTableDef()
bot: discord.Client


@routes.get('/login/github')
async def github_login(request: web.Request):
    return web.HTTPFound(
        f"https://github.com/login/oauth/authorize?"
        f"{}"
    )
