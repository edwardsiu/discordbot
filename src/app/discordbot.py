from discord.ext import commands

class DiscordBot(commands.Bot):
    def setup_config(self, config):
        self._config = config
