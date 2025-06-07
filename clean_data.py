import pandas as pd

# 1. Load the CSV with appropriate encoding
file_path = "C:/Users/achsa/OneDrive/Desktop/project/Sample - Superstore.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# 2. Drop duplicates
df = df.drop_duplicates()

# 3. Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 4. Convert date columns
df['order_date'] = pd.to_datetime(df['order_date'], format='%m/%d/%Y')
df['ship_date'] = pd.to_datetime(df['ship_date'], format='%m/%d/%Y')

# 5. Clean text data (strip & lowercase)
text_cols = df.select_dtypes(include='object').columns
df[text_cols] = df[text_cols].apply(lambda x: x.str.strip().str.lower())

# 6. Fix postal code type
df['postal_code'] = df['postal_code'].astype('Int64')

# 7. Save to CSV with safe error handling
output_path = "C:/Users/achsa/OneDrive/Desktop/project/cleaned_superstore.csv"
try:
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to: {output_path}")
except PermissionError:
    print("Permission denied: Make sure the file is not open in Excel and try again.")

# 8. Print a summary
print("\n=== Dataset Info ===")
print(df.info())

print("\n=== Missing Values ===")
print(df.isnull().sum())

print("\n=== Basic Statistics ===")
print(df.describe(include='all'))

print("\n=== Sample Cleaned Data ===")
print(df.head())



 

