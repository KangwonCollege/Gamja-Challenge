import logging
import os

from aiohttp import web
from discord.ext import interaction
from discord.ext import tasks
from sqlalchemy.orm import sessionmaker

from utils.directory import directory

app = web.Application()
routes = web.RouteTableDef()
log = logging.getLogger(__name__)


class WebServer:
    @routes.get('/')
    async def hello_world(self):
        return web.Response(text="Hello World")

    def __init__(self, client: interaction.Client):
        self.client = client

        views = [
            "views." + file[:-3] for file in os.listdir(
                os.path.join(directory, "views")
            ) if file.endswith(".py")
        ]
        app.add_routes(routes)

    @interaction.listener()
    async def on_ready(self):
        print("Ready")
        self.web_server.start()

    @tasks.loop()
    async def web_server(self):
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, host='0.0.0.0', port=8080)
        await site.start()


def setup(client: interaction.Client, factory: sessionmaker):
    client.add_interaction_cog(WebServer(client))
