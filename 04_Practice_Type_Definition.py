# ===============================================================================================================================
#                                       PRACTICE EXERCISES: TYPE DEFINITIONS & HINTS
# ===============================================================================================================================

# -------------------------------------------------------------------------------------------------------------------------------
# EXERCISE 1: Basic Variable & Function Type Annotations
# -------------------------------------------------------------------------------------------------------------------------------
# Calculate bonus based on salary (float) and experience (int), returning a float.

def calculate_bonus(salary: float, experience: int) -> float:
    if experience > 5:
        return salary * 0.20
    return salary * 0.10

emp_salary: float = 50000.0
emp_years: int = 6
bonus_amount: float = calculate_bonus(emp_salary, emp_years)
print(f"Bonus Amount: ${bonus_amount}")


# -------------------------------------------------------------------------------------------------------------------------------
# EXERCISE 2: Typing Lists & Dictionaries
# -------------------------------------------------------------------------------------------------------------------------------
# Count completed projects given a dictionary mapping project names (str) to statuses (bool).

def count_completed_projects(statuses: dict[str, bool]) -> int:
    return sum(1 for is_completed in statuses.values() if is_completed)

projects: list[str] = ["Dashboard API", "ETL Pipeline", "ML Model UI"]
project_status: dict[str, bool] = {
    "Dashboard API": True,
    "ETL Pipeline": True,
    "ML Model UI": False
}

completed_count: int = count_completed_projects(project_status)
print(f"Completed Projects: {completed_count}")


# -------------------------------------------------------------------------------------------------------------------------------
# EXERCISE 3: Typing Homogeneous & Heterogeneous Tuples
# -------------------------------------------------------------------------------------------------------------------------------
# 1. Homogeneous tuple: any number of integer scores using `...`
# 2. Heterogeneous tuple: strict fixed record structure (Name, Age, IsActive)

recent_scores: tuple[int, ...] = (85, 90, 78, 92)
user_profile: tuple[str, int, bool] = ("Anurag", 28, True)

print(f"Scores: {recent_scores}, Profile: {user_profile}")


# -------------------------------------------------------------------------------------------------------------------------------
# EXERCISE 4: Union & Optional Types
# -------------------------------------------------------------------------------------------------------------------------------
# Accept multiple types using Union (`|`) and return Optional type (`str | None`).

def lookup_user(user_id: int | str) -> str | None:
    database = {101: "alice_dev", "EMP-02": "bob_analyst"}
    return database.get(user_id)

user_a = lookup_user(101)
user_b = lookup_user("EMP-99")  # Returns None if not found

print(f"User A: {user_a}, User B (Not Found): {user_b}")


# -------------------------------------------------------------------------------------------------------------------------------
# EXERCISE 5: Generic Functions using TypeVar
# -------------------------------------------------------------------------------------------------------------------------------
# Use TypeVar to accept any list type while preserving the exact return data type.

from typing import TypeVar

T = TypeVar('T')

def get_middle_element(items: list[T]) -> T:
    mid_index = len(items) // 2
    return items[mid_index]

number_list: list[int] = [10, 20, 30, 40, 50]
string_list: list[str] = ["apple", "banana", "cherry"]

mid_num = get_middle_element(number_list)    # Inferred as int
mid_str = get_middle_element(string_list)    # Inferred as str

print(f"Middle Number: {mid_num}, Middle String: {mid_str}")