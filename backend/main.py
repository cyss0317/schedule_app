from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Person(BaseModel):
    id: int
    name: str
    age: int


DB: List[Person] = [
  Person(id=1, name="Yun", age=33)
]


@app.get("/")
def read_root():
    return DB


@app.get("/{id}")
def get_person(id: int):
    for person in DB:
        if person.id == id:
            return person

            