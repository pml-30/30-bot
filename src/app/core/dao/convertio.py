import asyncio
import base64
from pathlib import Path

from aiohttp import ClientSession
from jinja2 import Environment, FileSystemLoader

from src.app.core import dto

DAYS = {
    0: "Понедельник",
    1: "Вторник",
    2: "Среда",
    3: "Четверг",
    4: "Пятница",
    5: "Суббота",
    6: "Воскресенье",
}


class Convertio:
    def __init__(self, project_dir: Path, convertio_api_key: str) -> None:
        self._project_dir = project_dir
        self.__api_key = convertio_api_key

    async def render_svg(self, lessons: list[dto.Lesson], schedule: dto.DefaultDay, templates_path: Path) -> str:
        env = Environment(
            loader=FileSystemLoader(templates_path),
            enable_async=True
        )

        data = {
            "font": "JetBrains Mono",
            "bg_color": "525fe1",
            "text_color": "fff6f4",
            "warn_color": "ff0060",
            "lessons": lessons,
            "len": len(lessons),
            "day": DAYS.get(schedule.weekday, "Неизвестный день"),
            "loc": schedule.location,
        }

        return await env.get_template("schedule.svg").render_async(data)

    async def render_png(self, input_svg: str) -> bytes:
        data = {
            "apikey": self.__api_key,
            "input": "base64",
            "file": base64.b64encode(input_svg.encode()).decode(),
            "filename": "sh.svg",
            "outputformat": "png"
        }

        async with ClientSession() as session:
            async with session.post("https://api.convertio.co/convert", json=data) as response:
                json = await response.json()
                if json["status"] == "ok":
                    conv_id = json["data"]["id"]
                else:
                    raise RuntimeError("Convertio response is bad: {}".format(json))

            while True:
                async with session.get(f"https://api.convertio.co/convert/{conv_id}/status") as response:
                    json = await response.json()
                    if json["status"] == "ok":
                        if json["data"]["step"] == "finish":
                            download_url = json["data"]["output"]["url"]
                            break
                    else:
                        raise RuntimeError("Convertio response is bad: {}".format(json))
                await asyncio.sleep(1)
            # else:
            #     raise RuntimeError("Conversion not ended: {}".format(json))

            async with session.get(download_url) as response:
                return await response.content.read()

    async def get_schedule(self, lessons: list[dto.Lesson], schedule: dto.DefaultDay) -> bytes:
        svg = await self.render_svg(lessons, schedule, self._project_dir / "src" / "templates")
        png = await self.render_png(svg)
        return png
