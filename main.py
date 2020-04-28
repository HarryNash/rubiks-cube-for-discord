import discord, asyncio, argparse
from commands import hands, jumble, solve, custom, text
from cube_constants import (
    HANDS_OP,
    JUMBLE_OP,
    SOLVE_OP,
    CUSTOM_OP,
    TEXT_OP,
    HELP_OP,
    GRAFFITIED_IMAGE,
    HELP_TEXT,
)

client = discord.Client()
lock = asyncio.Lock()


class MyClient(discord.Client):
    database_connection: str

    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        """Detects and carries out any commands then sends a cube image or text."""
        txt = None
        await lock.acquire()
        if message.content.startswith(HANDS_OP):
            txt = hands(message.channel.id, message.content[len(HANDS_OP + " ") :])
        elif message.content.startswith(JUMBLE_OP):
            jumble(message.channel.id)
        elif message.content.startswith(SOLVE_OP):
            solve(message.channel.id, self.database_connection)
        elif message.content.startswith(CUSTOM_OP):
            txt = custom(
                message.channel.id,
                message.content[len(CUSTOM_OP + " ") :],
                self.database_connection,
            )
        elif message.content.startswith(TEXT_OP):
            txt = text(message.channel.id, self.database_connection)
        elif message.content.startswith(HELP_OP):
            txt = HELP_TEXT
        else:
            lock.release()
            return

        if txt == None:
            await message.channel.send_file(
                "cube.png", filename=GRAFFITIED_IMAGE, content="cube"
            )
        else:
            await message.channel.send(txt)
        lock.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("token", type=str, help="bot authentication token")
    parser.add_argument(
        "database_connection",
        type=str,
        help="'dbname=A user=B host=C port=D password=E'",
    )
    args = parser.parse_args()
    client = MyClient()
    client.database_connection = args.database_connection
    client.run(args.token)
