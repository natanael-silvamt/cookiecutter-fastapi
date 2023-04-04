from fastapi import APIRouter, status
from fastapi.response import JSONResponse

from {{cookiecutter.project_slug}}.healthchecks.models import HealthCheckResponse

router = APIRouter(tags=['healthchecks'])


@router.get('/ping', status_code=status.HTTP_200_OK, response_model=HealthCheckResponse, include_in_schema=False)
async def ping() -> JSONResponse:
    return JSONResponse(content='pong', status_code=status.HTTP_200_OK)
