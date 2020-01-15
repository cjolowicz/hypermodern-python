import textwrap

import typer

from . import wikipedia


def _main(
    language: str = typer.Option(  # noqa: B008
        "en",
        "--language",
        "-l",
        help="Language edition of Wikipedia",
        metavar="LANG",
        show_default=True,
    )
) -> None:
    """The hypermodern Python project."""
    page = wikipedia.random_page(language=language)

    typer.secho(page.title, fg="green")
    typer.echo(textwrap.fill(page.extract))


def main() -> None:
    return typer.run(_main)
