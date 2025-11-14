import discord
import aiohttp
import asyncio

backend_url = 'http://127.0.0.1:8000/schnack_api/v1/'


async def get_mother_language_options():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{backend_url}get_mother_languages/') as response:
            data = await response.json()

    return [discord.SelectOption(label=item["label"], value=item["value"]) for item in data]


async def get_correction_style_options():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{backend_url}get_correction_styles/') as response:
            data = await response.json()

    return [discord.SelectOption(label=item["label"], value=item["value"]) for item in data]


async def get_target_level_options():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{backend_url}get_target_levels/') as response:
            data = await response.json()

    return [discord.SelectOption(label=item["label"], value=item["value"]) for item in data]


async def get_german_level_options():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{backend_url}get_german_levels/') as response:
            data = await response.json()

    return [discord.SelectOption(label=item["label"], value=item["value"]) for item in data]


async def send_user_preference_to_backend(payload):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{backend_url}user_preferences/', json=payload) as response:
            data = await response.json()
            print(data)
            status = response.status
            print(status)
            return status