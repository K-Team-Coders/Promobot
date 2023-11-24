from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from database.sqlalchemy import current_session, bbase, engine

from inputs import message, file
from services import organisations

app = FastAPI()

bbase.metadata.create_all(engine, checkfirst=True)

# Inputs routers
app.include_router(
    message.router, 
    prefix="/api",
    tags=["inputs"]
    )

app.include_router(
    file.router, 
    prefix="/api",
    tags=["inputs"]
    )

app.include_router(
    organisations.router, 
    prefix="/api",
    tags=["database"]
    )

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello World"}