from fastapi import FastAPI, APIRouter
import uvicorn
from pydantic import BaseModel
from backend.v1 import database

class UpdateClicks(BaseModel):
    user_id: int
    clicks: int

app = FastAPI()
v1_client = APIRouter(prefix="/v1")

@v1_client.get("/clicks/get")
def get_clicks(user_id: int):
    return database.get_clicks(
        user_id=user_id
    )

@v1_client.put("/clicks/update")
def update_clicks(update: UpdateClicks):
    database.update_clicks(
        user_id=update.user_id,
        clicks=update.clicks
    )
    return {"update": "success"}

@v1_client.post("/user/new")
def new_user(user_id: int):
    database.new_user(
        user_id=user_id
    )
    return {"new_user": "success"}

@v1_client.delete("/user/delete")
def delete_user(user_id: int):
    database.delete_user(
        user_id=user_id
    )
    return {"delete": "success"}



if __name__ == "__main__":
    app.include_router(v1_client)

    uvicorn.run(app)
