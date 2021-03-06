from functools import lru_cache

import requests
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from config import Settings


#
# Type Definition
#
# 引数で使用するクラスの命名規則
# RESTの引数は XXQuery
# GraphQLの場合は XXInput
#

class LineNotifyQuery(BaseModel):
    token: str
    message: str


class SlackNotifyQuery(BaseModel):
    webhook_url: str
    text: str


#
# Share Function Define
#

# env 読み出し
@lru_cache()
def get_settings():
    return Settings()


#
# FastAPI EndPoint Definition ->
#


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_settings().allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# LINE APIを叩く
@app.post('/line')
async def post_line_notify(query: LineNotifyQuery):
    line_notify_api = 'https://notify-api.line.me/api/notify'

    headers = {'Authorization': f'Bearer {query.token}'}
    data = {'message': f'{query.message}'}
    requests.post(line_notify_api, headers=headers, data=data)


# Slack APIを叩く
@app.post('/slack')
async def post_slack_notify(query: SlackNotifyQuery):
    icon_url = None
    if get_settings().icon_url != '':
        icon_url = get_settings().icon_url

    requests.post(query.webhook_url, json={
        'username': 'ほっとけーる',
        'icon_url': icon_url,
        'text': query.text
    })
