from routes import webhook
from version import __version__
from fastapi import FastAPI


app = FastAPI(
    title="Efficient Data Pipeline",
    version=__version__,
    contact={
        "name": "Diogo Bastos",
        "url": "https://github.com/BastosDiogo",
        "email": "bmnetto.diogo@gmail.com",
    }
)

app.include_router(webhook.router)