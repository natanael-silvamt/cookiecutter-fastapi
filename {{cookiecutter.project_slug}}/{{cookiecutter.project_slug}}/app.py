from fastapi import FastAPI
from typing import List

from starlette.middleware.cors import CORSMiddleware

from {{cookiecutter.project_slug}}.utils import load_identifier


class Application(FastAPI):
    def __init__(self: 'Application', routers: List[str], *args, **kwargs) -> None:
        super().__init__(
            title='{{cookiecutter.project_name}}',
            version='0.0.1',
            *args,
            **kwargs,
        )

        self._load_routes(routers=routers)

        self.add_middleware(
            CORSMiddleware,
            allow_origins=[],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )

    def _load_routes(self: 'Application', routers: List[str]) -> None:
        for router_name in routers:
            router = load_identifier(router_name)
            self.include_router(router)
