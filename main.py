from fastapi import FastAPI

app = FastAPI(title="Safewalk API")

@app.get("/")
def read_root():
  return {"message": "Safewalk backend is running!"}
