# ==============================================================================
#       DOCSTRINGS, TYPE HINTS, MULTIPLE RETURNS & COMPOSITION
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. DOCSTRINGS, TYPE HINTS & RETURN STATEMENTS
# ------------------------------------------------------------------------------
# Real-World Scenario: A temperature converter (Celsius to Fahrenheit).
# - Type hints (`celsius: float -> float`) act as clear documentation for IDEs.
# - The docstring explains the exact mathematical formula and parameter specs.
# - `return` passes the computed value back so it can be reused in calculations.

print("--- 1. Docstrings, Type Hints & Return ---")

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit.

    Formula:
        (Celsius * 9/5) + 32

    Parameters:
        celsius (float): The temperature in degrees Celsius.

    Returns:
        float: The equivalent temperature in degrees Fahrenheit.
    """
    return (celsius * 9 / 5) + 32

# Using the function
water_boiling_c = 100.0
water_boiling_f = celsius_to_fahrenheit(water_boiling_c)
print(f"{water_boiling_c}°C = {water_boiling_f:.1f}°F")  # Output: 100.0°C = 212.0°F

# Reading the docstring programmatically:
# print(celsius_to_fahrenheit.__doc__)


# ------------------------------------------------------------------------------
# 2. DEFAULT PARAMETER VALUES & KEYWORD ARGUMENTS
# ------------------------------------------------------------------------------
# Real-World Scenario: An e-commerce discount and currency formatter.
# - `discount_percent=0.0` and `currency="$"` make those parameters optional.
# - RULE: Positional arguments must always precede default arguments.

print("\n--- 2. Default Parameters & Keyword Arguments ---")

def calculate_item_price(price: float, discount_percent: float = 0.0, currency: str = "$") -> str:
    """Calculates final price after discount and attaches the currency symbol."""
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return f"{currency}{final_price:.2f}"

# 2.1 Using only the required argument (defaults apply: 0% discount, '$' currency):
print("Standard Item:", calculate_item_price(100.0))  # $100.00

# 2.2 Overriding positional argument (20% discount):
print("Sale Item:", calculate_item_price(100.0, 20.0))  # $80.00

# 2.3 Using keyword argument to override currency only:
print("International Item:", calculate_item_price(100.0, currency="€"))  # €100.00

# 2.4 Providing all arguments explicitly:
print("Custom Order:", calculate_item_price(200.0, discount_percent=15.0, currency="₹"))  # ₹170.00


# ------------------------------------------------------------------------------
# 3. RETURNING MULTIPLE VALUES (TUPLE PACKING & UNPACKING)
# ------------------------------------------------------------------------------
# Real-World Scenario: A 2D Geometry Analyzer.
# - Python packs comma-separated return values into a single tuple automatically.
# - The caller can unpack them directly into distinct variables.

print("\n--- 3. Multiple Return Values (Tuple Unpacking) ---")

def analyze_rectangle(length: float, width: float):
    """
    Computes both area and perimeter for a given rectangle.

    Returns:
        tuple: (area, perimeter)
    """
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter  # Packed into a tuple: (area, perimeter)

# 3.1 Unpacking into separate variables
rect_area, rect_perimeter = analyze_rectangle(10, 5)
print(f"Rectangle Area: {rect_area} sq units")
print(f"Rectangle Perimeter: {rect_perimeter} units")

# 3.2 Capturing the packed tuple directly
geometry_result = analyze_rectangle(4, 3)
print(f"Packed Result: {geometry_result} (Type: {type(geometry_result).__name__})")


# ------------------------------------------------------------------------------
# 4. FUNCTION COMPOSITION (MODULAR PIPELINE DESIGN)
# ------------------------------------------------------------------------------
# Real-World Scenario: Automated Payroll Processing.
# - Modular code delegates work to small, single-purpose helper functions.
# - Step 1: `compute_gross_pay` handles hours and overtime logic.
# - Step 2: `deduct_tax` handles tax reduction.
# - Step 3: `generate_pay_slip` orchestrates both into a printable summary.

print("\n--- 4. Function Composition ---")

# Step 1: Gross earnings calculation (1.5x for hours above 40)
def compute_gross_pay(hours_worked: float, hourly_rate: float) -> float:
    """Calculates gross pay including 1.5x overtime for hours worked over 40."""
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        return (40 * hourly_rate) + (overtime_hours * hourly_rate * 1.5)
    return hours_worked * hourly_rate

# Step 2: Tax deduction logic
def deduct_tax(gross_amount: float, tax_rate: float = 0.20) -> float:
    """Deducts income tax from gross earnings (default: 20%)."""
    tax_amount = gross_amount * tax_rate
    return gross_amount - tax_amount

# Step 3: Orchestrator function composing the pipeline
def generate_pay_slip(employee_name: str, hours: float, rate: float) -> str:
    """Composes wage calculation and tax deduction into a structured payslip."""
    gross = compute_gross_pay(hours, rate)
    net_pay = deduct_tax(gross)
    
    return (
        f"--- PAYSLIP: {employee_name.upper()} ---\n"
        f"  Hours Worked: {hours} hrs @ ${rate:.2f}/hr\n"
        f"  Gross Income: ${gross:.2f}\n"
        f"  Net Payout  : ${net_pay:.2f} (after 20% tax)"
    )

# Executing the composition
employee_slip = generate_pay_slip("Alex Morgan", hours=45, rate=20.0)
print(employee_slip)