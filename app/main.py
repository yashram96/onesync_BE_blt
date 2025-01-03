
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.routes import users_router,auth_router
from app.helpers.config import settings
app = FastAPI()


allowed_origins = settings.APP_ORIGIN.split(',')
origins = []
origins.extend(allowed_origins)

@app.get("/")
async def root():
    return {"message": "Hello World"}


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Add your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users_router)
app.include_router(auth_router)



if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 