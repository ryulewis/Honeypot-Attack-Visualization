import pandas as pd
import folium
from folium.plugins import HeatMap

# Load the data
df = pd.read_csv('honeypot.csv')

# Verify the number of rows in the original DataFrame
print("Number of rows in the original DataFrame:", len(df))

# Data cleaning
df['latitude'] = df['latitude'].astype(float)
df['longitude'] = df['longitude'].astype(float)

# Filter data to remove outliers
valid_latitude_range = (-90, 90)
filtered_df = df[(df['latitude'] >= valid_latitude_range[0]) & (df['latitude'] <= valid_latitude_range[1])]

# Verify the number of rows left after filtering
print("Number of rows left after filtering:", len(filtered_df))

# Calculate the frequency of occurrences for each country
country_frequencies = filtered_df['country'].value_counts().reset_index()
country_frequencies.columns = ['country', 'frequency']

# Sort countries based on frequency in descending order
sorted_countries = country_frequencies.sort_values(by='frequency', ascending=False)

# Select the top N countries to display in the legend (e.g., top 5)
top_countries = sorted_countries.head(5)

# Create a Folium map
m = folium.Map(location=[filtered_df['latitude'].mean(), filtered_df['longitude'].mean()], zoom_start=2)

# Create a list of latitudes and longitudes
locations = list(zip(filtered_df['latitude'], filtered_df['longitude']))

# Create a HeatMap with increased blur and max_zoom parameters
heat_map = HeatMap(locations, radius=3, blur=3, max_zoom=13)  # Adjust the parameters as needed

# Add the HeatMap to the map
heat_map.add_to(m)

# Create a legend with the top countries and their frequencies
legend_html = '''
     <div style="position: fixed; 
                 bottom: 50px; left: 50px; width: 150px; height: 140px; 
                 border:2px solid grey; z-index:9999; font-size:12px;
                 background-color:white; padding: 5px; text-align: center;">
         <b>Top Countries by Attack Frequency</b><br>
         {}<br>
         {}<br>
         {}<br>
         {}<br>
         {}<br>
     </div>
     '''.format(
         "{}: {}".format(top_countries.iloc[0]['country'], top_countries.iloc[0]['frequency']),
         "{}: {}".format(top_countries.iloc[1]['country'], top_countries.iloc[1]['frequency']),
         "{}: {}".format(top_countries.iloc[2]['country'], top_countries.iloc[2]['frequency']),
         "{}: {}".format(top_countries.iloc[3]['country'], top_countries.iloc[3]['frequency']),
         "{}: {}".format(top_countries.iloc[4]['country'], top_countries.iloc[4]['frequency'])
     )

m.get_root().html.add_child(folium.Element(legend_html))

# Save the map to an HTML file
m.save('honeypot_heatmap.html')
