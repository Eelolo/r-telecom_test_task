from fastapi import FastAPI
import uvicorn
from db.base import database
from endpoints import contacts
from endpoints import ping_pong_and_parse


app = FastAPI(title='r-Telecom test task')
app.include_router(ping_pong_and_parse.router)
app.include_router(contacts.router, prefix='/contacts', tags=['contacts'])


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
