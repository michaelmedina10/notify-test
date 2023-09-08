from fastapi import APIRouter, status, Request
from fastapi.responses import JSONResponse
import json


repo_router = APIRouter(tags=['repository_notifier'])


@repo_router.post('/notify')
async def get_notification_repo(body: dict):

    with open('retorno_post.json', 'w') as file:
        json.dump(body, file, ensure_ascii=True, indent=2)

    if body is not None:
        return JSONResponse(content=body, status_code=status.HTTP_200_OK)
    return JSONResponse(content='No Content', status_code=status.HTTP_200_OK)


@repo_router.get('/teste')
async def get_notification_repo():
    return JSONResponse(content='Get Deu certo', status_code=status.HTTP_200_OK)
