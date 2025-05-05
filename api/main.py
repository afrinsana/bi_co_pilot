from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

def valid_token(token: str) -> bool:
    # Replace with your actual token validation logic
    return token == "valid_token_example"
from machine_copilot import ModelOptimizer, load_model

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/optimize")
async def optimize_model(
    model_config: dict,
    token: str = Depends(oauth2_scheme)
):
    if not valid_token(token):  # Your auth logic
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    optimizer = ModelOptimizer(load_model(model_config))
    optimizer.prune_model(amount=0.2)
    return {"status": "optimized"}

# Run with: 
# uvicorn api.main:app --reload