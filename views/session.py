import discord
from aiohttp import web

from utils.getConfig import get_config
from modules.githubOauth2 import GithubOAuth2, Scope


routes = web.RouteTableDef()
bot: discord.Client

parser = get_config()
oauth2_client = GithubOAuth2(
    client_id=parser.get('Github', 'client_id'),
    client_secret=parser.get('Github', 'client_secret')
)


@routes.get('/login/github')
async def github_login(request: web.Request):
    state = request.rel_url.query.get('state')
    return web.HTTPFound(
        oauth2_client.authorize(
            redirect_url="https://" + request.host + "/login/callback",
            scope=[Scope.user],
            state=state
        )
    )


@routes.get('/login/callback')
async def github_login_callback(request: web.Request):

    return web.Response("성공적! 페이지를 닫습니다.")
