# Heal.lol

![](https://avatars.githubusercontent.com/u/164548157?s=200&v=4)

[![GPL](https://img.shields.io/github/license/heal-devs/heal-py?color=2f2f2f)](https://github.com/heal-devs/heal-py/blob/main/LICENSE) ![](https://img.shields.io/pypi/pyversions/heallol?color=2f2f2f) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Quick Links

- [PyPI Homepage](https://pypi.org/project/heallol/)
- [API Documentation](https://docs.heal.lol/)

# Install

To install the library, you need the latest version of pip and minimum Python 3.9

> Stable version
```
pip install heallol
```

> Unstable version (this one gets more frequent changes)
```
pip install git+https://github.com/heal-devs/heal-py
```

# Examples

In-depth examples are located in the [examples folder](https://github.com/heal-devs/heal-py/tree/main/examples)

Here's a quick example:

```py
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
```