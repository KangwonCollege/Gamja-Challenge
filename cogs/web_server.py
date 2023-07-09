import logging
import importlib
import importlib.util
import os
import sys

from aiohttp import web
from discord.ext import interaction
from discord.ext import tasks
from sqlalchemy.orm import sessionmaker

from utils.directory import directory

log = logging.getLogger(__name__)


class WebServer:
    def __init__(self, client: interaction.Client):
        self.client = client
        self.app = web.Application()

        views = [
            "views." + file[:-3] for file in os.listdir(
                os.path.join(directory, "views")
            ) if file.endswith(".py")
        ]
        for view in views:
            spec = importlib.util.find_spec(view)
            lib = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(lib)  # type: ignore
            except Exception as e:
                log.error("Extension Failed: {0} ({1})".format(view, e.__class__.__name__))
                continue

            try:
                web_route = getattr(lib, 'routes')
                setattr(lib, 'bot', self.client)
            except AttributeError:
                log.error("No Entry Point Error: {0}".format(view))
                continue
            sys.modules[view] = lib
            self.app.add_routes(web_route)

    @interaction.listener()
    async def on_ready(self):
        print("ready")
        self.web_server.start()

    @tasks.loop()
    async def web_server(self):
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, host='0.0.0.0', port=8080)
        await site.start()


def setup(client: interaction.Client, factory: sessionmaker):
    client.add_interaction_cog(WebServer(client))
