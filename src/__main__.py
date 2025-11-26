from src.api import create_app
import uvicorn
import os

def run():
    app = create_app()
    port = int(os.environ.get("PORT", 8000))  
    uvicorn.run(app, host="0.0.0.0", port=port)

if __name__ == "__main__":
    run()
