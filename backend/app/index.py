from time import time
from typing import Optional
from fastapi import FastAPI, Body, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True #default value is True, if not provided, it will be True
    rating: Optional[int] = 0 #optional field, can be None

while True:
    try :
        conn = psycopg2.connect(host="localhost", database="fastapi", 
                                user = "postgres", password = "postgres",
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Database connection failed")
        print("Error: ", error)
        time.sleep(2)


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
    for post in my_posts:
        if str(post['id']) == str(id):
            return post
    return None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM local""")
    posts = cursor.fetchall()
    print(posts)
    return {"data ": posts}

@app.get("/posts/return")
def return_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    cursor.execute("""INSERT INTO local (title, content, published) 
                    VALUES (%s, %s, %s)
                    RETURNING *""", 
                    (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()

    return {"data": new_post}

@app.get("/posts/latest")
def get_latest_post():
    latest_post = my_posts[-1]
    return {"data": latest_post}

@app.get("/posts/{id}")
def get_post(id: str, response: Response):
    cursor.execute("""SELECT * FROM local WHERE id = %s""", str((id)))
    post = cursor.fetchone()
    print(post)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} not found")
    return {"data": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: str):
    
    cursor.execute ("""DELETE FROM local WHERE id = %s RETURNING * """, str((id)))
    post = cursor.fetchone()
    conn.commit()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} not found")
    # my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: str, updated_post: Post):
    cursor.execute ("""UPDATE local SET title = %s, content = %s, published = %s 
                    WHERE id = %s RETURNING * """, 
                    (updated_post.title, updated_post.content, updated_post.published, str((id))))
    updated_post = cursor.fetchone()
    conn.commit()
    # post, index = find_post(id)
    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id: {id} not found")
    # updated_post_dict = updated_post.model_dump()
    # updated_post_dict['id'] = post['id']
    # my_posts[index] = updated_post_dict
    return {"data": updated_post}
