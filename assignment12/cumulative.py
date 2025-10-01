import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("../db/lesson.db")

# SQL query: total price per order
query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

# Load into DataFrame
df = pd.read_sql_query(query, conn)
conn.close()

# Method 1: cumulative using apply()
def cumulative(row):
    totals_above = df['total_price'][0:row.name+1]
    return totals_above.sum()

df['cumulative_apply'] = df.apply(cumulative, axis=1)

# Method 2: cumulative using cumsum() (simpler)
df['cumulative'] = df['total_price'].cumsum()

# Plot cumulative revenue vs order_id
ax = df.plot(
    x="order_id",
    y="cumulative",
    kind="line",
    marker="o",
    title="Cumulative Revenue by Order",
    legend=False
)

ax.set_xlabel("Order ID")
ax.set_ylabel("Cumulative Revenue ($)")
plt.grid(True)
plt.tight_layout()
plt.show()
