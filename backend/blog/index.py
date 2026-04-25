from typing import Optional
# from uuid import uuid4
import fastapi as fastapi
from fastapi import FastAPI, Body, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange    


app = FastAPI()

post_id = []

posts = []


class Post(BaseModel):
    # id :int already suppled by the create post function, so we don't need to include it here
    title: str
    content: str
    published: bool = False #default value is False, if not provided, it will be False
    rating: Optional[int] = None #optional field, can be None


@app.get("/")
async def root():
    return {"data" : {p['title'] for p in posts}}


@app.get("/posts/{id}")
def get_post(id: str, response: Response):
    for i, p in posts:
        if str(i['id']) == str(id):
            return {"data": p}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} not found")


@app.post("/createposts")
def create_post(new_post: Post):
    post_dict = new_post.model_dump()
    post_dict['id'] = randrange(0, 1000000)
    while post_dict['id'] in post_id:
            post_dict['id'] = randrange(0, 1000000)
    post_id.append(post_dict['id'])
    posts.append(post_dict)
    return {"data": posts}

@app.put("/posts/{id}")
def update_post(id: str, updated_post: Post):
    for i, p in enumerate(posts):
        if str(p['id']) == str(id):
            posts[i] = updated_post.model_dump()
            posts[i]['id'] = int(id)
            return {"data": posts[i]}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} not found")