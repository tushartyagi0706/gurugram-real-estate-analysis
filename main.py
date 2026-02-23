import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("C:\\Users\\ASUS\\AppData\\Local\\Temp\\8f5e2050-8380-4201-90da-1222acd673d9_data of gurugram real Estate.csv.zip.3d9\\data of gurugram real Estate.csv")
df.head()
df.shape
df.info()
#data cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
#cleaning numeric columns
df["price"] = (
    df["price"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .astype(float)
    .astype(int)
)
df["area"] = (
    df["area"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .astype(float)
    .astype(int)
)

df["rate_per_sqft"] = (
    df["rate_per_sqft"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .astype(float)
    .astype(int)
)
# cleaning categorical columns
df["status"] = df["status"].str.strip().str.lower()
df["rera_approval"] = df["rera_approval"].str.strip().str.lower()
df["flat_type"] = df["flat_type"].str.strip().str.lower()
df = df.drop_duplicates()
#now answering business quesions
#1. What is the average price of properties in Gurugram?
average_price = df["price"].mean()
print(f"The average price of properties in Gurugram is: {average_price:.2f}")
#2 question compare the properties with and without RERA approval and make a bar chart to show the difference in average price between the two categories.
rera_comparison = df.groupby("rera_approval")["price"].mean().reset_index()
plt.figure(figsize=(8, 6))
sns.barplot(x="rera_approval", y="price", data=rera_comparison)
plt.title("Average Price of Properties with and without RERA Approval")
plt.xlabel("RERA Approval")
plt.ylabel("Average Price")
plt.savefig("rera_approval_comparison.png")
plt.show()
#question 3 area and price relationship and make a scatter plot to visualize the relationship between area and price.
sns.scatterplot(x="area", y="price", data=df)
plt.title("Relationship between Area and Price")
plt.xlabel("Area (sqft)")
plt.ylabel("Price")
plt.savefig("area_price_relationship.png")
plt.show()


