import heallol
import base64

# from io import BytesIO

heal = heallol.New("your_token_here")
tiktok = heal.tiktok


async def get_tiktok(url: str):
    resp, status = await tiktok.getpost(url)
    return resp, status


async def main():
    resp, status = await get_tiktok("https://www.tiktok.com/@near.amv/video/7333276422489771270")
    if status != 200:
        print(f'Error: {resp.get("error")}')
        return
    else:
        video = resp.get("video_binary")
        video = base64.b64decode(video)  # Decode the base64-encoded video.
        # You only have to do that if you're using discord.py.
        # video_io = BytesIO(video) # Convert the video to a file-like object.
        # video_file = discord.File(fp=video_io, filename="tiktok.mp4") # Create a discord.File object.
        with open("tiktok.mp4", "wb") as file:
            file.write(video)  # Save the video to a file.
        resp["video_binary"] = ""  # Remove the video_binary key from the response.
        print(resp)
