from {{cookiecutter.project_slug}}.app import Application


def test_basic_app(routers):
    app = Application(routers)
    
    assert len(app.routes) == 5  # FastAPI Builtin routes (4) + 1 test route
