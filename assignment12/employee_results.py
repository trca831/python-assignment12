import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("../db/lesson.db")

# SQL query (already provided)
query = """
SELECT last_name, 
       SUM(price * quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id;
"""

# Load query results into a DataFrame
employee_results = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Plot using pandas plotting
ax = employee_results.plot(
    kind="bar",
    x="last_name",
    y="revenue",
    color="skyblue",
    legend=False,
    title="Employee Revenue"
)

# Label axes
ax.set_xlabel("Employee Last Name")
ax.set_ylabel("Revenue ($)")
plt.xticks(rotation=45)

# Show plot
plt.tight_layout()
plt.show()