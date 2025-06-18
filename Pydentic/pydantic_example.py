# pydantic_example_v2.py

from pydantic import BaseModel, Field, EmailStr, ValidationError
from typing import List, Optional
from datetime import datetime

# -----------------------------------------
# 1. Define a Pydantic Model
# -----------------------------------------

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: Optional[int] = Field(default=None, ge=0, le=120)
    is_active: bool = True
    signup_ts: Optional[datetime] = None

# -----------------------------------------
# 2. Creating an instance with validation
# -----------------------------------------

user_data = {
    "id": "101",
    "name": "Alice",
    "email": "alice@example.com",
    "age": 25,
    "signup_ts": "2024-08-01T10:00:00"
}

user = User.model_validate(user_data)

print("\n✅ User object created:")
print(user)

print("\n📄 As dictionary:")
print(user.model_dump())  # Replaces .dict()

# -----------------------------------------
# 3. Handling Validation Errors
# -----------------------------------------

invalid_data = {
    "id": "x",
    "email": "not-an-email"
}

try:
    User.model_validate(invalid_data)
except ValidationError as e:
    print("\n❌ Validation Error:")
    print(e)

# -----------------------------------------
# 4. Nested Models
# -----------------------------------------

class Address(BaseModel):
    city: str
    state: str
    pincode: int

class Employee(BaseModel):
    name: str
    email: EmailStr
    addresses: List[Address]

emp_data = {
    "name": "John",
    "email": "john@company.com",
    "addresses": [
        {"city": "Bangalore", "state": "KA", "pincode": 560001},
        {"city": "Mumbai", "state": "MH", "pincode": 400001}
    ]
}

employee = Employee.model_validate(emp_data)
print("\n✅ Nested Model Example:")
print(employee)

# -----------------------------------------
# 5. Pydantic v2 JSON Output
# -----------------------------------------

print("\n🔄 JSON Output:")
print(employee.model_dump_json(indent=2))

# -----------------------------------------
# Summary:
# - Use `model_validate()` instead of constructor for parsing
# - Use `model_dump()` instead of `.dict()`
# - Use `model_dump_json()` instead of `.json()`
# - Pydantic v2 is stricter and cleaner, better for production apps
# -----------------------------------------