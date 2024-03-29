from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select
from todo import settings
from typing import Annotated
from contextlib import asynccontextmanager


# STEPS TO CREATE THIS TODO API
# Step-1: Create Database on Neon
# Step-2: Create .env file for environment variables
# Step-3: Create setting.py file for encrypting DatabaseURL
# Step-4: Create a Model
# Step-5: Create Engine
# Step-6: Create a function for table creation
# Step-7: Create a function for session management
# Step-8: Create contexT manager for app lifespan
# Step-9: Create all endpoints and requests of the todo app

# Creating Model
    # Data Model
    # Tabel Model
class Todo(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)    
    content: str = Field(index=True, min_length=3, max_length=54)
    isComplete: bool = Field(default=False)

# creating engine
# engine is one for whole application
connection_string: str = str(settings.DATABASE_URL).replace("postgresql", "postgresql+psycopg") 
engine = create_engine(connection_string, connect_args= {"sslmode" : "require"}, pool_recycle= 300, pool_size=8)   

# creating tables
async def create_tables():
    SQLModel.metadata.create_all(engine)

# todo: Todo = Todo(content="First todo")
# tode1: Todo = Todo(content="2nd todo")

# using Session
# each functionality/transaction have seprate session
# session = Session(engine)

# adding todos to our data base
# session.add(todo)
# session.add(tode1)
# print(f"Before commit {todo}")
# session.commit()
# session.refresh(todo)
# print(f"After commit {todo}")
# session.close()


# creating generator function act as a dependency
def get_session():
    with Session(engine) as session:
        yield session

# what should run when app will start???
@asynccontextmanager
async def lifeSpan(app:FastAPI):
    print("Creating Tables in Database")
    create_tables()
    print("Tables Created Successfully")
    yield

app: FastAPI = FastAPI(lifespan=lifeSpan, title="Todos API", version="1.0")

@app.get('/')
async def root():
    return {"message": "Welcome to my Todo API"}

@app.post("/todos/", response_model=Todo)
async def create_todo(todo: Todo, session: Annotated[Session, Depends(get_session)]):
    session.add(todo)
    session.commit()
    session.refresh(todo)
    if todo:
        return todo
    else:
        raise HTTPException(status_code=404, detail="No task found")

@app.get("/todos/", response_model= list[Todo])
async def get_all(session:Annotated[Session, Depends(get_session)]):    # Depends: Dependency injection 
    statement = select(Todo)
    todos = session.exec(statement).all()
    if todos:
        return todos
    else:
        raise HTTPException(status_code=404, detail="No task found")

@app.get("/todos/{id}", response_model=Todo)
async def get_one_todo(id: int, session: Annotated[Session, Depends(get_session)]):
    todo = session.exec(select(Todo).where(Todo.id == id)).first()
    if todo:
        return todo
    else:
        raise HTTPException(status_code=404, detail="No task found")
 
@app.put("/todos/{id}")
async def edit_todo(id: int, todo: Todo, session: Annotated[Session, Depends(get_session)]):
    existing_todo = session.exec(select(Todo).where(Todo.id == id)).first()
    if existing_todo:
        existing_todo.content = todo.content
        existing_todo.isComplete = todo.isComplete
        session.add(existing_todo)
        session.commit()
        session.refresh(existing_todo)
        return existing_todo
    else:
        raise HTTPException(status_code=404, detail="No task found")

@app.delete("/todos/{id}")
async def delete_todo(id: int, session: Annotated[Session, Depends(get_session)]):
    todo = session.exec(select(Todo).where(Todo.id == id)).first()
    # we can also get todo like 
    # todo = session.get(Todo, id)
    if todo:
        session.delete(todo)
        session.commit()
        return {"message": "Task is Successfuly deleted"}
    else:
        raise HTTPException(status_code=404, detail="No task found")