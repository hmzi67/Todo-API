# Todo API Documentation

This documentation outlines the usage and endpoints of the Todo API.

## Base URL

The base URL for all endpoints is `http://127.0.0.0:8000`.
## API Information

The Todo API is created using **FASTAPI** and utilizes the **Neon serverless Database**.
## Endpoints

### Get All Todos

- **URL:** `/todos/`
- **Method:** `GET`
- **Description:** Retrieve a list of all todos.
- **Response:** List of todo objects.

### Create Todo

- **URL:** `/todos/`
- **Method:** `POST`
- **Description:** Create a new todo.
- **Request Body:** JSON object containing `content` (string) and `isComplete` (boolean) fields.
- **Response:** Created todo object.

### Get Todo by ID

- **URL:** `/todos/{id}`
- **Method:** `GET`
- **Description:** Retrieve a specific todo by its ID.
- **Parameters:** 
  - `id` (integer) - The ID of the todo to retrieve.
- **Response:** Todo object.

### Edit Todo

- **URL:** `/todos/{id}`
- **Method:** `PUT`
- **Description:** Update an existing todo.
- **Parameters:** 
  - `id` (integer) - The ID of the todo to update.
- **Request Body:** JSON object containing `content` (string) and `isComplete` (boolean) fields.
- **Response:** Updated todo object.

### Delete Todo

- **URL:** `/todos/{id}`
- **Method:** `DELETE`
- **Description:** Delete a todo by its ID.
- **Parameters:** 
  - `id` (integer) - The ID of the todo to delete.
- **Response:** Success message if the todo is deleted successfully.

## Data Model

The todo object has the following structure:

- `id` (integer, optional): The unique identifier of the todo.
- `content` (string): The content or description of the todo.
- `isComplete` (boolean): Indicates whether the todo is complete or not.

## Errors

- **404 Not Found:** Returned when a requested resource (todo) is not found.

### MIT License

Copyright (c) 2024 Hamza Waheed

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Todo API"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
