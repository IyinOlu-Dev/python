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
    rating: Optional[int] = 0 #optional field, can be None


@app.get("/")
async def root():
    for p in posts: 
        return {"data" : [{"title": p['title'], "content": p['content'][:300], "rating": p['rating']} for p in posts]}


@app.get("/posts/{id}")
def get_post(id: str, response: Response):
    '''This function retrieves a post by its ID. 
    It iterates through the list of posts and checks if the ID matches. 
    If a match is found, it returns the post data. 
    If no match is found after checking all posts, it raises an HTTP 404 Not Found exception 
    with a message indicating that the post with the specified ID was not found.'''
    for p in posts:
        if str(p['id']) == str(id):
            return {"data": p}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} not found")


@app.post("/createposts", status_code=status.HTTP_201_CREATED)
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

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: str):
    for i, p in enumerate(posts):
        if str(p['id']) == str(id):
            del posts[i]
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} not found")