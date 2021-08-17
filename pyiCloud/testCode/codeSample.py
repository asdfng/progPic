import os
import click
import datetime
from pyicloud import PyiCloudService

print("Setup Time Zone")
time.strftime("%X %x %Z")
os.environ["TZ"] = "America/New_York"

print("Py iCloud Services")
api = PyiCloudService()
