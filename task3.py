import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------------------
# Step 1: Load or create data
# ---------------------------
file_name = "quotes_dataset.csv"

if not os.path.exists(file_name):
    print("Dataset not found. Creating sample data...")

    data = {
        "Quote": [
            "The world as we have created it is a process of our thinking.",
            "It is our choices that show what we truly are.",
            "There are only two ways to live your life.",
            "Imperfection is beauty, madness is genius.",
            "The person who reads too much loses himself."
        ],
        "Author": [
            "Albert Einstein",
            "J.K. Rowling",
            "Albert Einstein",
            "Marilyn Monroe",
            "Jane Austen"
        ],
        "Tags": [
            "change, deep-thoughts",
            "choices, inspirational",
            "life, simplicity",
            "beauty, life",
            "books, reading"
        ]
    }

    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False)

else:
    df = pd.read_csv(file_name)

# ---------------------------
# 1. Transform raw data
# ---------------------------
author_counts = df["Author"].value_counts()

# ---------------------------
# 2. Create visualizations
# ---------------------------

# Bar Chart
plt.figure()
author_counts.plot(kind="bar")
plt.title("Number of Quotes per Author")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")
plt.show()

# Pie Chart
plt.figure()
author_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Quote Distribution by Author")
plt.ylabel("")
plt.show()

# ---------------------------
# 3. Enhance understanding
# ---------------------------
print("Visualization shows which authors contribute more quotes.")

# ---------------------------
# 4. Data storytelling
# ---------------------------
top_author = author_counts.idxmax()
print(f"Insight: {top_author} has the highest number of quotes.")

# ---------------------------
# 5. Portfolio ready output
# ---------------------------
print("Visualizations created successfully and ready for portfolio.")
