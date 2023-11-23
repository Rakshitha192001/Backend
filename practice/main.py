from fastapi import FastAPI,Body,Depends
from model import PostSchema,UserSchema,UserLoginSchema
from jwt_handler import signJWT
from jwt_bearer import jwtBearer

posts = [
    {
        "id":1,
        "title":"pengiuns",
        "text":"sdedwed",
    },
    {
        "id":2,
        "title":"pengiuns",
        "text":"sdedwed",
    },
    {
        "id":3,
        "title":"pengiuns",
        "text":"sdedwed",
    },
]

users=[]

app=FastAPI()

  
# @app.get('/')
# async def hello():
#     return {"hello":"world"}

#Get post
@app.get("/posts",tags=["posts"])
def get_posts():
    return {"data":posts}

#get by  id
@app.get("/posts/{id}",tags=["posts"])
def get_one_post(id:int):
    if id>len(posts):
        return{
            "error":"does not exist"
        }
    for post in posts:
        if post["id"]==id:
            return{
                "data":post
            }
            
#post a blog post
@app.post("/posts",dependencies=[Depends(jwtBearer())],tags=["posts"] )
def add_post(post:PostSchema):
    post.id=len(posts)+1
    posts.append(post.dict())
    return{
        "info":"post added"
        
    }
    
#user signup[create a new user]
@app.post("/user/signup",dependencies=[Depends(jwtBearer())],tags=["user"])
def user_signup(user:UserSchema=Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data:UserLoginSchema):
    for user in users:
        if user.email==data.email and user.password==data.password:
            return True
        
        else:
            return False
        
@app.post("/user/login",tags=["user"])
def user_signup(user:UserLoginSchema=Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return{
            "error":"Invalid"
        }


