import github  # pyGithub
from pyrogram import filters

from SpamX.services.pyrogram import pbot as client


@client.on_message(filters.command("contributors") & ~filters.edited)
async def give_cobtribs(c, m):
    g = github.Github()
    co = ""
    n = 0
    repo = g.get_repo("Shavin77/SpamXX")
    for i in repo.get_contributors():
        n += 1
        co += f"{n}. [{i.login}](https://github.com/{i.login})\n"
    t = f"**SpamX Contributors**\n\n{co}"
    await m.reply(t, disable_web_page_preview=True)
