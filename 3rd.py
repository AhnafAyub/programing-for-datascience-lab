import pandas as pd

# Load the CSV file 
df = pd.read_csv("gender_submission.csv")

print("Dataset loaded successfully!")

# 1. Display first 10 rows
print("First 10 rows:")
display(df.head(10))

# 2. Find number of rows and columns
print("Dataset shape:", df.shape)
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# 3. Identify column names
print("Column names:")
print(df.columns)

# 4. Check data types
print("Data types:")
print(df.dtypes)

# 5. Display descriptive statistics
print("Descriptive statistics:")
display(df.describe())



print("Last 5 rows:")
display(df.tail())


print("Dataset information:")
df.info()



# 1. Select the Age column
print("Age column:")
display(df["Age"])

# 2. Select multiple columns
print("Name, Age and Sex columns:")
display(df[["Name", "Age", "Sex"]])

# 3. Select rows using loc
print("First 5 rows using loc:")
display(df.loc[0:4])

# 4. Select specific rows and columns using loc
print("Selected rows and columns using loc:")
display(df.loc[0:4, ["Name", "Age", "Sex"]])

# 5. Select rows using iloc
print("First 5 rows using iloc:")
display(df.iloc[0:5])

# 6. Select specific rows and columns using iloc
print("Selected rows and columns using iloc:")
display(df.iloc[0:5, 0:3])



# 1. Passengers belonging to first class
print("First-class passengers:")
display(df[df["Pclass"] == 1])

# 2. Passengers younger than 18
print("Passengers younger than 18:")
display(df[df["Age"] < 18])

# 3. Male passengers who survived
print("Male passengers who survived:")
display(df[(df["Sex"] == "male") & (df["Survived"] == 1)])

# 4. Passengers who paid more than 100
print("Passengers who paid more than 100:")
display(df[df["Fare"] > 100])



# 1. Sort by fare in ascending order
print("Passengers sorted by lowest fare:")
display(df.sort_values(by="Fare", ascending=True))

# 2. Sort by fare in descending order
print("Passengers sorted by highest fare:")
display(df.sort_values(by="Fare", ascending=False))

# 3. Display the 10 highest fares
print("Top 10 highest fares:")
display(df.sort_values(by="Fare", ascending=False).head(10))



# 1. Average fare by passenger class
print("Average fare by passenger class:")
display(df.groupby("Pclass")["Fare"].mean())

# 2. Average age by gender
print("Average age by gender:")
display(df.groupby("Sex")["Age"].mean())

# 3. Survival rate by passenger class
print("Survival rate by passenger class:")
display(df.groupby("Pclass")["Survived"].mean() * 100)

# 4. Survival rate by gender
print("Survival rate by gender:")
display(df.groupby("Sex")["Survived"].mean() * 100)



# 1. Total number of passengers
print("Total passengers:", df.shape[0])

# 2. Average passenger age
print("Average passenger age:", df["Age"].mean())

# 3. Passenger class with the highest number of passengers
class_counts = df["Pclass"].value_counts()

print("Passenger count by class:")
display(class_counts)

print("Class with the most passengers:", class_counts.idxmax())

# 4. Average fare by gender
print("Average fare by gender:")
display(df.groupby("Sex")["Fare"].mean())

# 5. Gender with the higher survival rate
survival_gender = df.groupby("Sex")["Survived"].mean() * 100

print("Survival rate by gender:")
display(survival_gender)

print("Gender with higher survival rate:", survival_gender.idxmax())

# 6. Survival rate by passenger class
print("Survival rate by passenger class:")
display(df.groupby("Pclass")["Survived"].mean() * 100)