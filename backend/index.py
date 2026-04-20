from typing import Optional
from fastapi import FastAPI, Body, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True #default value is True, if not provided, it will be True
    rating: Optional[int] = None #optional field, can be None

my_posts = [
                {"id": 1,
                "title": "title of post 1", 
                "content": "content of post 1", 
                "published": True,
                "rating": 5
                },
                {"id": "2",
                "title": "title of post 2", 
                "content": "content of post 2", 
                "published": False,
                "rating": None
                },
            ]

def find_post(id):
    for i, post in enumerate(my_posts):
        if str(post['id']) == str(id):
            return post, i

    # for post in my_posts:
    #     if int(post['id']) == int(id):
    #         return post

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(new_post: Post):
    post_dict = new_post.model_dump()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/latest")
def get_latest_post():
    latest_post = my_posts[-1]
    return {"data": latest_post}

@app.get("/posts/{id}")
def get_post(id: str, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} not found")
    return {"data": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: str):
    post, index = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} not found")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)