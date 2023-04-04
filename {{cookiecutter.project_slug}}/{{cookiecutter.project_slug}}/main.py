from {{cookiecutter.project_slug}}.app import Application
from {{cookiecutter.project_slug}}.routers import routers


app = Application(routers=routers)
