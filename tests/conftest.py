import os

# The documentation routes are only enabled in dev mode, so the tests run in dev.
# Must be set before app.main is imported (it reads the settings at import time).
os.environ["ENVIRONMENT"] = "dev"
