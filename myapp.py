from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

# Load the gapminder dataset
df = pldata.gapminder()

# Get unique list of countries
countries = df['country'].unique()

# Initialize Dash app
app = Dash(__name__)
server = app.server  # required for deployment

# Layout: dropdown + graph
app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": c, "value": c} for c in countries],  # populate dropdown
        value="Canada"  # default value
    ),
    dcc.Graph(id="gdp-growth")
])

# Callback: update plot when dropdown changes
@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(selected_country):
    # Filter the dataset for chosen country
    filtered = df[df["country"] == selected_country]
    
    # Create line plot: year vs GDP per capita
    fig = px.line(
        filtered,
        x="year",
        y="gdpPercap",
        title=f"GDP Per Capita Growth in {selected_country}"
    )
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)