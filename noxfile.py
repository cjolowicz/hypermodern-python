"""Nox sessions."""
import nox
from nox.sessions import Session


nox.options.sessions = "lint", "mypy", "pytype", "tests"
locations = "src", "tests", "noxfile.py", "docs/conf.py"


@nox.session(python="3.8")
def black(session: Session) -> None:
    """Run black code formatter."""
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python=["3.8", "3.7"])
def lint(session: Session) -> None:
    """Lint using flake8."""
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-annotations",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
        "darglint",
    )
    session.run("flake8", *args)


@nox.session(python=["3.8", "3.7"])
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or locations
    session.install("mypy")
    session.run("mypy", *args)


@nox.session(python="3.7")
def pytype(session: Session) -> None:
    """Type-check using pytype."""
    args = session.posargs or locations
    session.install("pytype")
    session.run("pytype", "--config=pytype.cfg", *args)


@nox.session(python=["3.8", "3.7"])
def tests(session: Session) -> None:
    """Run the test suite."""
    args = session.posargs or ["--cov", "--xdoctest"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


@nox.session(python="3.8")
def docs(session: Session) -> None:
    """Build the documentation."""
    session.install("sphinx", "sphinx-rtd-theme")
    session.run("sphinx-build", "docs", "docs/_build")
