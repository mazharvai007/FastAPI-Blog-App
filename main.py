from fastapi import FastAPI
from apis.base import api_router

# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel
# from typing import Optional

from core.config import settings


# class EmployeeCreate(BaseModel):
#     name: str
#     salary: int
#     experience: int


# class EmployeeUpdate(BaseModel):
#     name: str
#     salary: int
#     experience: int


# class EmployeePartialUpdate(BaseModel):
#     name: Optional[str] = None
#     salary: Optional[int] = None
#     experience: Optional[int] = None


# employees = [
#     {"id": 1, "name": "John Doe", "is_active": True, "salary": 55000, "experience": 5},
#     {
#         "id": 2,
#         "name": "Jane Smith",
#         "is_active": True,
#         "salary": 62000,
#         "experience": 7,
#     },
#     {
#         "id": 3,
#         "name": "Sam Brown",
#         "is_active": False,
#         "salary": 48000,
#         "experience": 3,
#     },
#     {
#         "id": 4,
#         "name": "Alice Johnson",
#         "is_active": True,
#         "salary": 75000,
#         "experience": 10,
#     },
#     {"id": 5, "name": "Bob White", "is_active": True, "salary": 54000, "experience": 4},
# ]

# Initialize the FastAPI app
app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
app.include_router(api_router)


@app.get("/")
def hello_python():
    print(settings.DATABASE_URL)
    return "Hello Python"


# @app.get("/employees")
# def gell_all_employee(active: Optional[bool] = None):
#     if active is not None:
#         response = [
#             employee for employee in employees if employee["is_active"] == active
#         ]
#         return response
#     else:
#         return employees


# # Get employee by id
# @app.get("/employees/{employee_id}")
# def get_employee_by_id(employee_id: int):
#     """
#     get your employee by id
#     """

#     for employee in employees:
#         if employee["id"] == employee_id:
#             return employee
#     return JSONResponse(
#         content=f"Error: Employee Id {employee_id} not found",
#         status_code=status.HTTP_404_NOT_FOUND,
#     )


# # Add new employee
# @app.post("/employees")
# def create_employee(employee: EmployeeCreate):
#     new_employee = {
#         "id": len(employees) + 1,
#         "name": employee.name,
#         "salary": employee.salary,
#         "experience": employee.experience,
#         "is_active": True,
#     }

#     employees.append(new_employee)

#     return JSONResponse(
#         content="Success: Employee created successfully!",
#         status_code=status.HTTP_201_CREATED,
#     )


# # Update employee information
# @app.put("/employees/{employee_id}")
# def update_employee_info_by_id(employee: EmployeeUpdate, employee_id: int):
#     update_employee = jsonable_encoder(employee)
#     employees[employee_id] = update_employee
#     return update_employee

#     # return JSONResponse(content="Success: Employee update successfully!", status_code=status.HTTP_201_CREATED)


# # Delete Employee
# @app.delete("/employees/{employee_id}")
# def delete_employee_by_id(employee_id: int):
#     return JSONResponse(
#         content="Success: Employee deleted successfully!",
#         status_code=status.HTTP_204_NO_CONTENT,
#     )


# # Patch (Partial update) update of the employee
# @app.patch("/employees/{employee_id}", response_model=EmployeePartialUpdate)
# def partial_employee_update_by_id(employee_id: int, employee: EmployeePartialUpdate):
#     if employee.name:
#         print(employee.name)

#     if employee.salary:
#         print(employee.salary)

#     if employee.experience:
#         print(employee.experience)

#     return JSONResponse(
#         content="Success: Employee updated successfully!",
#         status_code=status.HTTP_200_OK,
#     )
