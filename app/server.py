from fastapi import FastAPI
from langserve import add_routes

app = FastAPI()

from research_assistant import chain as research_assistant_chain

add_routes(app, research_assistant_chain, path="/research-assistant")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
