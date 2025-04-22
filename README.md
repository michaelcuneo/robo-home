# Installation

## Clone the project

```console
git clone git@github.com:michaelcuneo/robo-home.git
```

## Navigate to the project directory

```console
cd robo-home
```

## Install UV (If you don't have it already)

```console
brew install uv
```

## Or

```console
pipx install uv
```

## Run uv sync (Which will read the project.toml and uv.lock and install the environment)

```console
uv sync
```

## Run the application

```console
uv run main.py
```
