import discord
import aiohttp

backend_url = 'http://schnack.up.railway.app/schnack_api/v1/'


async def get_mother_language_options():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{backend_url}get_mother_languages/') as response:
                data = await response.json()

        return [discord.SelectOption(label=item["label"], value=item["label"]) for item in data]
    except:
        return [discord.SelectOption(label='Error', value='....')]


async def get_correction_style_options():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{backend_url}get_correction_styles/') as response:
                data = await response.json()

        return [discord.SelectOption(label=item["label"], value=item["label"]) for item in data]
    except:
        return [discord.SelectOption(label='Error', value='....')]


async def get_target_level_options():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{backend_url}get_target_levels/') as response:
                data = await response.json()

        return [discord.SelectOption(label=item["label"], value=item["label"]) for item in data]
    except:
        return [discord.SelectOption(label='Error', value='....')]


async def get_german_level_options():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{backend_url}get_german_levels/') as response:
                data = await response.json()

        return [discord.SelectOption(label=item["label"], value=item["label"]) for item in data]
    except:
        return [discord.SelectOption(label='Error', value='....')]


async def save_user_preference_to_backend(payload):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{backend_url}user_preferences/', json=payload) as response:
                return (response.status, await response.json())
    except Exception as error:
        print('Sending Preferences to backend failed silently: ', error)


async def check_if_user_exists(user_id):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{backend_url}user_preferences/{user_id}/') as response:
                return response.status
    except Exception as error:
        print('Checking if used id exists failed silently: ', error)


async def respond_to_user(discord_user_id, user_input):
    try:
        payload = {"discord_user_id": discord_user_id,
                   "user_input": user_input}
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{backend_url}gemini/respond/', json=payload) as response:
                return await response.json()
    except Exception as error:
        print('Responding to user failed silently: ', error)


async def save_user_history(user_id, user_message, schnack_response):
    try:
        payload = {"user": user_id, "user_message": user_message, "schnack_response": schnack_response}
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{backend_url}user_history/', json=payload) as response:
                return response.status
    except Exception as error:
        print('Saving user history failed silently: ', error)