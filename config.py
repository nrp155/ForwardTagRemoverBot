# ForwardTagRemoverBot - A Telegram Bot To Hide Forward Source
# Copyright (C) 2023 by Abdul Razaq <https://github.com/Artis7eeR>
# ForwardTagRemoverBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# ForwardTagRemoverBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7472794797:AAGXeMzA-hnggHrXunBhJGKAsRogobHPzvA")
    SOURCE = "https://github.com/Artis7eeR/ForwardTagRemoverBot"
    START_TEXT = """
Hi [{}](tg://user?id={}) 
I am A Forward Tag remover Bot.
Send /help to know more ©[Abdul Razaq](https://github.com/artis7eer)"""
    HELP_TEXT = "Forward Me A File,Video,Audio,Photo or Anything And \nI will Send You the File Back\n\n`How to Set Caption?`\nReply Caption to a File,Photo,Audio,Media"
