"""Command-line interface for the hypermodern Python project."""
import click

from . import __version__, splines


@click.command()
@click.option("-n", "--count", default=-1, help="Number of splines to reticulate")
@click.version_option(version=__version__)
def main(count: int) -> None:
    """The hypermodern Python project."""
    for spline in splines.reticulate(count):
        click.echo(f"Reticulating spline {spline}...")
