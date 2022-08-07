# abbreav

Abbrevation bot for discord.

### Configuration

Copy `example-config.toml` to `config.toml`. Update the bot token and any initial abbreviations you would like to register. Bot will delete the command requesting the expansion and post a new message with the expanded form.

```toml
[secrets]
# Secrets required for the bot to run.
token = TOKEN_HERE

[abbr]
# Abbreviations registered with the bot.
demo = "this is a demo"
nc = "/newCommand arg1 arg2 argN"
```

### Usage

Built-in commands:

- `save`: Write the current config to `config.toml`. This _saves_ any changes you've made.

Adding abbreviations is done like so: `>ab ABBR VALUE [...]`. Example `>ab nc /newCommand 123 234` where `nc` will then expand to `/newCommand 123 234`.

Using abbreviations:

Have the bot expand your abbreviation by using `>ab abbreviation` such as `>ab nc` to expand the example we set earlier.
