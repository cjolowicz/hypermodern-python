"""Command-line interface for the hypermodern Python project."""
import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main() -> None:
    """The hypermodern Python project."""
