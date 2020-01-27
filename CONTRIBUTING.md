# How to Contribute

You need Python 3.7+ and the following tools:

- [Poetry](https://poetry.eustace.io/)
- [Nox](https://nox.thea.codes/)

Install the package with development requirements:

```sh
$ poetry install
```

Reformat your changes:

```sh
$ nox --session=black
```

Run the command-line interface:

```sh
$ poetry run hypermodern-python
```

Run the test suite:

```sh
$ nox
```
