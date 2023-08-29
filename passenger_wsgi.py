import sys, os

# path to the virtual environment's site-packages
venv_site_packages = "/users/PZS0714/travert/ondemand/dev/sciGatewayApp/.venv/lib/python3.6/site-packages"

# Add it to sys.path
sys.path.append(venv_site_packages)

# passenger_wsgi.py
from app import MyApp as application
