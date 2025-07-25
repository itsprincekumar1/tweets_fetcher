import click
from core.user_fetcher import get_latest_tweet

@click.command()
@click.argument("username")
def cli(username):
    """Fetches the most recent tweet of a given user."""
    tweet = get_latest_tweet(username)
    print(f"\n📢 Latest tweet from @{username}:\n\n{tweet}\n")
