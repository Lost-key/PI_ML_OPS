from fastapi import FastAPI
# from typing import Union
# from fastapi.responses import HTMLResponse
# from typing import List, Dict, Tuple, Sequence, Any, Union, Optional, Callable
from functions import PlayTimeGenre
from functions import UserForGenre
from functions import UsersRecommend
from functions import UsersWorstDeveloper
from functions import sentiment_analysis
from functions import recomendacion_juego

app = FastAPI()


@app.get("/PlayTimeGenre/{genre}")
async def user(genre: str):
    try:
        result = PlayTimeGenre(genre)
        return result
    except Exception as e:
        return {"error": str(e)}
    

@app.get("/UserForGenre/{genre}")
async def user(genre: str):
    try:
        result = UserForGenre(genre)
        return result
    except Exception as e:
        return {"error": str(e)}
    

@app.get("/UsersRecommend/{year}")
async def user(year: int):
    try: 
        
        result = UsersRecommend(year)
        return result
    except Exception as e:
        return {"error": str(e)}  
    
   

@app.get("/UsersWorstDeveloper/{year}")
async def user(year: int):
    try:
        result = UsersWorstDeveloper(year)
        return result
    except Exception as e:
        return {"error": str(e)}  
    
    
@app.get("/sentiment_analysis/{developer}")
async def user(developer: str):
    try:
        result = sentiment_analysis(developer)
        return result
    except Exception as e:
        return {"error": str(e)}
    

@app.get("/recomendacion_juego/{id}")
async def user(id: int):
    try:
        result = recomendacion_juego(id)
        return result
    except Exception as e:
        return {"error": str(e)}
    