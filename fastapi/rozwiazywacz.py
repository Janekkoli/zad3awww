from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Form


def solve_quadratic_equation(a, b, c):
    delta = b**2 - 4 * a * c
    if delta < 0:
        return None
    elif delta == 0:
        return -b / (2 * a)
    else:
        x1 = (-b - delta**0.5) / (2 * a)
        x2 = (-b + delta**0.5) / (2 * a)
        return (x1, x2)

tags_metadata = [
    {
        "name": "solver",
        "description": "Methods for solving quadratic equations.",
    },
    {
        "name": "obsolete",
        "description": "Methods that are no longer supported.",
    },
]
app = FastAPI(openapi_tags=tags_metadata)
@app.get("/solve/{a}/{b}/{c}", tags=["solver"])
async def solve(a: float, b: float, c: float):
    solution = solve_quadratic_equation(a, b, c)
    match solution:
        case None:
            return {"number_of_solutions": 0}
        case (x_1, x_2):
            return {"number_of_solutions": 2, "x_1": x_1, "x_2": x_2}
        case x:
            return {"number_of_solutions": 1, "x": x}

@app.post("/solve_post")
async def solve_post(
    a: Annotated[float, Form()],
    b: Annotated[float, Form()],
    c: Annotated[float, Form()],
):
    solution = solve_quadratic_equation(a, b, c)
    match solution:
        case None:
            return {"number_of_solutions": 0}
        case (x_1, x_2):
            return {"number_of_solutions": 2, "x_1": x_1, "x_2": x_2}
        case x:
            return {"number_of_solutions": 1, "x": x}




