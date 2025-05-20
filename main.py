from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Login-Ms - Autenticação e autorização aplicação UrbanFood PosTech Fiap')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level='info', reload=True)


"""
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzQ4MzY4NDkzLCJpYXQiOjE3NDc3NjM2OTMsInN1YiI6IjMifQ.WEOZ58W9YDGH_UrnZE8b7SwzFT3YgNpbDlXhUUCSJsg
Tipo: bearer


"""