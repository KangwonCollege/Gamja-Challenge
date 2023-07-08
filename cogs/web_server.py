import logging
import importlib
import importlib.util
import os

from aiohttp import web
from discord.ext import interaction
from discord.ext import tasks

from utils.directory import directory

app = web.Application()
# routes = web.RouteTableDef()
log = logging.getLogger()


class WebServer:
    def __init__(self, client: interaction.Client):
        self.client = client

        views = [
            "views." + file[:-3] for file in os.listdir(
                os.path.join(directory, "views")
            ) if file.endswith(".py")
        ]
        for view in views:
            spec = importlib.util.find_spec(view)
            if spec is None:
                log.error("Extension Not Found: {0}".format(view))
                continue

            lib = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(lib)  # type: ignore
            except Exception as e:
                log.error("Extension Failed: {0} ({1})".format(view, e.__class__.__name__))
                continue

            try:
                routes = getattr(lib, 'routes')
                setattr(lib, 'bot', self.client)
                setattr(lib, 'bot', self.client)
            except AttributeError:
                log.error("No Entry Point Error: {0}".format(view))
                continue

            try:
                app.add_routes(routes)
            except Exception as e:
                log.error("Extension Failed: {0} ({1})".format(view, e.__class__.__name__))
                continue

    @tasks.loop()
    async def web_server(self):
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, host='0.0.0.0', port=8080)
        await site.start()

    @web_server.before_loop
    async def web_server_before_loop(self):
        await self.client.wait_until_ready()


async def setup(client: interaction.Client):
    client.add_interaction_cog(WebServer)
