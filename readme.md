# TrickyLoots

A simple and customizable Telegram bot built using the [Pyrogram](https://docs.pyrogram.org/) library.

## TODO

- [x] Set Blocklist with Bot
- [ ] Set Domains with Bot

## Features

- **Read Messages**: Read messages from different channels using a user account.
- **Affiliate Link Conversion**: Convert affiliate links with your affiliate IDs.
- **Message Forwarding**: Send those messages with your links to your channels.

## Installation

### Prerequisites

- Python 3.9+
- A Telegram bot token from [BotFather](https://core.telegram.org/bots#botfather)
- Docker

### Steps

1. Pull the Docker image:

   ```bash
   docker pull ghcr.io/aumirza/trickyloots-bot:latest`
   ```

2. Copy `.env.example` and rename it to `.env`.
3. Fill the `.env` file with the required details:

   - `BOT_TOKEN`: Your bot token from BotFather
   - `API_ID`: Your Telegram API ID
   - `API_HASH`: Your Telegram API Hash
   - Any other necessary configurations

4. Start the container:

   `docker compose up -d`

5. Generate the session string:

   - Access the container's terminal:
     `docker exec -it <container_name> /bin/bash`
   - Run the session string generation script:
     `python app/generate_sessionstring.py`
   - Follow the instructions to generate the session string.

6. Update the `.env` file with the generated session string:

   - Copy the session string generated from the previous step.
   - Add the session string to your `.env` file under `SELF_STRING` and `BOT_STRING`.

7. Restart the container to apply the new configuration:
   `docker compose down`
   `docker compose up -d`

## Usage

The bot will automatically connect to Telegram and start reading messages, converting links, and forwarding them to your specified channels.

## Configuration

You can configure various parameters in the `.env` file, such as:

- `BOT_TOKEN`: Your bot token
- `API_ID`: Your Telegram API ID
- `API_HASH`: Your Telegram API Hash
- `SELF_STRING`: Your session string
- Any other necessary configurations

## Contributors

Thanks to these wonderful people who have contributed to this project:

<table>
  <tr>
    <td align="center"><a href="https://github.com/aumirza"><img src="https://avatars.githubusercontent.com/u/31508843?v=4" width="100px;" alt=""/><br /><sub><b>Ahmadullah Mirza</b></sub></a></td>
    <td align="center"><a href="https://github.com/habibmy"><img src="https://avatars.githubusercontent.com/u/29559410?v=4" width="100px;" alt=""/><br /><sub><b>Habib Siddiqui</b></sub></a></td>
  </tr>
</table>

## Acknowledgements

- Pyrogram - Telegram MTProto API Client Library and Framework for Python
- [Python](https://www.python.org/) - Programming language

## Contact

If you have any questions, feel free to reach out to me at trickyloot@habibsiddiqui.in.
