import plotly.express as px
import plotly.data as pldata
import pandas as pd

# Load the dataset
df = pldata.wind(return_type='pandas')

# Show first and last 10 rows
print("First 10 rows:")
print(df.head(10))
print("\nLast 10 rows:")
print(df.tail(10))

# Clean the 'strength' column: remove non-numeric chars, convert to float
df['strength'] = df['strength'].str.replace(r'[^0-9.]', '', regex=True).astype(float)

# Create interactive scatter plot
fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind Strength vs Frequency by Direction",
    labels={"strength": "Wind Strength", "frequency": "Frequency"}
)

# Save plot as HTML
fig.write_html("wind.html")

print("\nPlot saved as wind.html")
