import discord
import aiohttp


async def get_mother_language_options():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/schnack_api/v1/get_mother_languages/') as response:
            data = await response.json()

    return [discord.SelectOption(label=item["label"], value=item["value"]) for item in data]


async def get_correction_style_options():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/schnack_api/v1/get_correction_styles/') as response:
            data = await response.json()

    return [discord.SelectOption(label=item["label"], value=item["value"]) for item in data]


async def get_target_level_options():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/schnack_api/v1/get_target_levels/') as response:
            data = await response.json()

    return [discord.SelectOption(label=item["label"], value=item["value"]) for item in data]


async def get_german_level_options():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/schnack_api/v1/get_german_levels/') as response:
            data = await response.json()

    return [discord.SelectOption(label=item["label"], value=item["value"]) for item in data]
