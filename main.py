from repositories.database import Database
from models.tables.user import User
from fastapi import FastAPI
from web.routes import all_routes

database = Database()
user = User()
user.create_table()

app = FastAPI()

for route in all_routes:
    app.include_router(route)

@app.get("/")
def root():
    return {"message": "API running"}
