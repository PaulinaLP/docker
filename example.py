import pandas as pd
import sys

check = sys.argv[1]

# Example DataFrame
data = {
    'Product ID': [1, 2, 3, 4, 5],
    'Product Name': ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Keyboard'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Accessories'],
    'Price': [999.99, 499.99, 299.99, 199.99, 49.99],
    'Stock': [50, 150, 100, 75, 200]
}

df = pd.DataFrame(data)
print (f'printing {check}')
