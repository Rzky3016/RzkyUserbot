from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum...`")


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum...`")


@register(outgoing=True, pattern='^.L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumussalam...`")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumussalam...`")


@register(outgoing=True, pattern='^.S(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`sayang,mau gak jadi pacar aku?...`")


@register(outgoing=True, pattern='^.s(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`sayang,mau gak jadi pacar aku?...`")

CMD_HELP.update({
    "salam x gombal":
    "⚡𝘾𝙈𝘿⚡`.P`\
\nPenjelasan: Untuk Memberi salam ke semua orang.\
\n\n⚡𝘾𝙈𝘿⚡`.L`\
\nPenjelasan: Untuk Menjawab Salam ke semua orang.\
    "⚡𝘾𝙈𝘿⚡`.S`
    \npenjelasan: Untuk Baperin orang.\"
})
