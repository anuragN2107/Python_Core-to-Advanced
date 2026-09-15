# ===============================================================================================================================
#                               CHAPTER 3: RESOURCE MANAGEMENT AND THE 'WITH' STATEMENT (CONTEXT MANAGERS)
# ===============================================================================================================================

# -------------------------------------------------------------------------------------------------------------------------------
# 1. WHY DO WE NEED THE 'WITH' STATEMENT?
# -------------------------------------------------------------------------------------------------------------------------------
# When working with external resources (like opening files, network connections, or database connections), you must 
# always close them properly after use, even if an exception occurs.
# 
# Traditionally, this required a `try-finally` block:
#   f = open("data.txt", "r")
#   try:
#       content = f.read()
#   finally:
#       f.close()  # Guarantees closure, but is bulky to write every time.
#
# The `with` statement (Context Manager) automates this cleanup process cleanly and safely behind the scenes!
# -------------------------------------------------------------------------------------------------------------------------------

print("=== CHAPTER 3: RESOURCE MANAGEMENT ===")

# Example: Safely reading a file using 'with'
print("\n--- Example 1: Using the 'with' statement for files ---")

# If the file doesn't exist, FileNotFoundError is thrown. 
# Whether an error happens or not, the 'with' block automatically closes the file securely.
try:
    # Simulating a file operation (using a non-existent file to show exception handling)
    with open("non_existent_file.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("[Caught Error]: The file could not be found, but resource cleanup was handled automatically!")


# -------------------------------------------------------------------------------------------------------------------------------
# 2. CREATING YOUR OWN CUSTOM CONTEXT MANAGER (ADVANCED)
# -------------------------------------------------------------------------------------------------------------------------------
# You can create your own custom context managers using Python's `__enter__` and `__exit__` magic methods inside a class,
# allowing you to control setup and teardown logic automatically.
# -------------------------------------------------------------------------------------------------------------------------------

print("\n--- Example 2: Custom Context Manager Class ---")

class ManagedDatabaseConnection:
    def __enter__(self):
        print("[Setup]: Opening database connection...")
        return self  # Returns the resource to the 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("[Teardown]: Closing database connection safely (Cleanup done).")
        # Returning True suppresses exceptions if needed, but here we let them propagate normally.
        return False  

    def query(self):
        print("Executing database query...")

# Testing the custom context manager
with ManagedDatabaseConnection() as db:
    db.query()
    # Even if an error happens inside this block, __exit__ is guaranteed to run!