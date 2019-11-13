import nox


nox.options.sessions = "lint", "mypy", "pytype", "tests"
locations = "src", "tests", "noxfile.py"


@nox.session(python="3.8")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python=["3.8", "3.7"])
def lint(session):
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-import-order",
    )
    session.run("flake8", *args)


@nox.session(python=["3.8", "3.7"])
def mypy(session) -> None:
    args = session.posargs or locations
    session.install("mypy")
    session.run("mypy", *args)


@nox.session(python="3.7")
def pytype(session):
    args = session.posargs or locations
    session.install("pytype")
    session.run("pytype", "--config=pytype.cfg", *args)


@nox.session(python=["3.8", "3.7"])
def tests(session):
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)
