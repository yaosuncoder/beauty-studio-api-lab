
import os

import psycopg
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from Beauty Studio API!"}


@app.get("/health")
def health_check():
    return {"status": "okkk"}


@app.get("/db-check")
def db_check():
    try:
        with psycopg.connect(
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"],
            dbname=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            connect_timeout=3,
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
                result = cur.fetchone()

        return {
            "database": "connected",
            "query_result": result[0],
        }

    except Exception:
        return {
            "database": "connection_failed",
        }
