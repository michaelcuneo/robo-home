# Installation

```console
# Clone the project.
git clone git@github.com:michaelcuneo/robo-home.git

# Navigate to the project directory
cd robo-home

# Install UV (If you don't have it already)
brew install uv

# Or
pipx install uv

# Run uv sync (Which will read the project.toml and uv.lock and install the environment)
uv sync

# Run the application
uv run main.py
