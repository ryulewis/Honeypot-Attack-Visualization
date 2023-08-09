# Honeypot Attack Visualization Project 

This project involves the creation of a honeypot attack visualization using Python's pandas and Folium libraries. The purpose of this project is to provide a geographical representation of honeypot attacks by plotting them on a heatmap. The heatmap displays the frequency and distribution of attacks across different countries. The project also includes data cleaning and filtering to ensure accurate and meaningful visualization results.

## Requirements

Before running the code, make sure you have the following requirements installed:

- Python (3.6+)
- pandas library (`pip install pandas`)
- Folium library (`pip install folium`)

## Getting Started

1. Clone or download this repository to your local machine.
2. Ensure you have the necessary libraries installed by running the provided installation commands or using your preferred package manager.

## Usage

1. Place your honeypot attack data in a CSV file named `honeypot.csv` in the same directory as the script.
2. Open the script file (`honeypot_visualization.py`) in a Python-compatible IDE or text editor.

### Script Overview

The script performs the following steps:

1. **Loading Data**: The script imports the required libraries and loads the attack data from the `honeypot.csv` file into a pandas DataFrame.

2. **Data Cleaning**: The script converts latitude and longitude columns to float data types and removes any data points with latitude values outside the valid range of -90 to 90.

3. **Filtering**: The script filters the data to remove outliers based on the valid latitude range.

4. **Calculating Country Frequencies**: The script calculates the frequency of occurrences for each country in the filtered dataset.

5. **Sorting Countries**: The countries are sorted in descending order based on their attack frequencies.

6. **Creating the Heatmap**: A Folium map is created centered around the mean latitude and longitude of the filtered dataset. A heatmap is generated using the latitude and longitude coordinates.

7. **Adding a Legend**: A legend displaying the top N countries with the highest attack frequencies is added to the map.

8. **Saving the Map**: The final map, including the heatmap and legend, is saved as an HTML file named `honeypot_heatmap.html`.

## Customization

You can customize various parameters of the heatmap and the legend to fit your preferences. Adjust parameters such as the heatmap radius, blur, max_zoom, and the number of top countries displayed in the legend.

## Disclaimer

This project is intended for educational and informational purposes only. The project should not be used for making security-related decisions without proper validation and analysis of real attack data. The creator of this project is not responsible for any misuse, misinterpretation, or unintended consequences resulting from the use of this project.

## Running the Script

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script (`honeypot_visualization.py`).
3. Run the script using the command: `python honeypot_visualization.py`
4. The script will process the data, generate the heatmap, and save it as `honeypot_heatmap.html` in the same directory.

## Conclusion

This project provides a visual representation of honeypot attacks' geographical distribution, making it easier to identify trends and analyze attack patterns across different countries. The heatmap and legend provide insights into the frequency of attacks, allowing for informed decision-making in terms of cybersecurity strategies and mitigation efforts.
