from fastapi import FastAPI
from models import User 


app = FastAPI()


class UserRoutes:
    
    def apply_routes(self, app: FastAPI) -> None:
        app.include_router(
            self.router,
            prefix="/users",
            tags=["users"],
            dependencies=[Depends(self.dependencies)],
        )

        DB: List[User] = [
            User(id=1, name="Yun", email="cyss0317@yahoo.com",
                birth_day="03/17/1990", preferred_days=["mon", "tue"]),
            User(id=2, name="Jason", email="cyss0317@yahoo.com",
                birth_day="03/17/1990", preferred_days=["mon", "tue"])
        ]


        @app.get("/")
        def read_root():
            answer = ""
            # put each user from the DB and return all the names
            for user in DB:
                answer += f"Hello, {user.name}. Your email is {user.email}"
            return answer


        @app.get("/{id}")
        def get_person(id: int):
            for person in DB:
                if person.id == id:
                    return person


        @app.post("/user")
        def create_user(user: User):
            DB.append(user)
            return user


        @app.delete("/delete/{id}")
        def delete_person(id: int):
            for person in DB:
                if person.id == id:
                    DB.remove(person)
                    return f"Delete {person.name} successfully"
    


