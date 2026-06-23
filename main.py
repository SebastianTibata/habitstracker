from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database.SessionLocal import get_db

app = FastAPI()


@app.get("/")
def read_root(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    return {"db_result": result.fetchone()[0]}