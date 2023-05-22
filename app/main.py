from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from fake_reeck import calculate_reccomend
#create server and configure token_api
app = FastAPI()
api_tokens = [
    open("../api-key").read()
]
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def api_auth_key(api_key: str=Depends(oauth2_scheme)):
    if api_key not in api_tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )

@app.get("/", dependencies= [Depends(api_auth_key)])
async def get_root():
    return "hello world"

#API interfaces
@app.get("/reccomendation/{id_user}")
async def reccomend_beer(id_user: int, id_location: int, randomness: int =1):
    rec_beer_id = calculate_reccomend(id_user, id_location, randomness)    
    return rec_beer_id
