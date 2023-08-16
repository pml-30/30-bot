import asyncio
import base64
from pathlib import Path

from aiohttp import ClientSession
from jinja2 import Environment, FileSystemLoader

from src.app.core.dto.database import LessonDTO, DefaultDayDTO, DayDTO

DAYS = {
    0: "Понедельник",
    1: "Вторник",
    2: "Среда",
    3: "Четверг",
    4: "Пятница",
    5: "Суббота",
    6: "Воскресенье",
}


async def render_svg(lessons: list[LessonDTO], schedule: DefaultDayDTO | DayDTO, templates_path: Path) -> str:
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
        "round": round,
        "len": len(lessons),
        "warns": [],
        "day": DAYS.get(schedule.weekday, "Неизвестный день"),
        "loc": schedule.location,
    }

    return await env.get_template("schedule.svg").render_async(data)


async def render_png(input_svg: str, api_key: str) -> bytes:
    data = {
        "apikey": api_key,
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

        for x in range(20):
            async with session.get(f"https://api.convertio.co/convert/{conv_id}/status") as response:
                json = await response.json()
                if json["status"] == "ok":
                    if json["data"]["step"] == "finish":
                        download_url = json["data"]["output"]["url"]
                        break
                else:
                    raise RuntimeError("Convertio response is bad: {}".format(json))
            await asyncio.sleep(1)
        else:
            raise RuntimeError("Conversion not ended: {}".format(json))

        async with session.get(download_url) as response:
            return await response.content.read()
