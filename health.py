import json

from typing import Type

from aiohttp.web import Request, Response

from maubot import Plugin
from maubot.handlers import web
from maubot.loader import PluginLoader


class HealthBot(Plugin):
    @web.get("/health")
    async def health(self, request: Request) -> Response:
        plugins = [plugin.to_dict() for plugin in PluginLoader.id_cache.values()]

        return Response(status=200,
                        content_type="application/json",
                        text=json.dumps({"status": "ok"}))
