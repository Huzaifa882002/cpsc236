SALES_TAX_RATE = 0.06  

def calculate_sales_tax(total):
    """Calculate the sales tax based on the given total."""
    return round(total * SALES_TAX_RATE, 2)

def calculate_total_after_tax(total):
    """Calculate the total after adding sales tax."""
    return round(total + calculate_sales_tax(total), 2)