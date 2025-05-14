from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI(title='Minha API Bala!')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


@app.get('/ola-mundo', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_root_html():
    return """
            <html>
                <head>
                    <title>Primeiro HTML</title>
                </head>
                <body>
                    <h1>Olá mundo!</h1>
                </body>
            </html>"""
