import pytest
from fastapi import status


@pytest.fixture
def url():
    return '/ping'


async def test_get_method_should_return_status_ok(client, url):
    response = await client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == 'pong'
