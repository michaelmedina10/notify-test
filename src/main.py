from fastapi import FastAPI
import uvicorn

from __init__ import __version__, __title__
from router import notify


app = FastAPI(title=__title__, version=__version__)


app.include_router(notify.repo_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
