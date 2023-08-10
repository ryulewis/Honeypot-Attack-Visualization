# Honeypot Attack Visualization

This project generates an interactive heatmap to visualize honeypot attack data provided in a CSV file. The heatmap illustrates the frequency and distribution of attacks across different countries.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.6 or higher
- Pandas library (`pip install pandas`)
- Folium library (`pip install folium`)
- A CSV file containing your honeypot attack data

## Data Format

The CSV file must contain at least the following columns:

- `latitude` - Latitude coordinate of the attack
- `longitude` - Longitude coordinate of the attack
- `country` - Country where the attack originated

Any additional columns will be ignored.

## Usage

1. Place your honeypot attack data CSV file in the same directory as `honeypot_visualization.py` 
2. Open `honeypot_visualization.py` and update the CSV filename on line 10 to match your data file.
3. Tweak the heatmap settings on lines 35-37 to best visualize your data distribution.
4. Adjust the legend location and number of top countries on lines 44-58.
5. Run `python honeypot_visualization.py`
6. The output heatmap HTML will be saved as `honeypot_heatmap.html`

## Customization

- Adjust heatmap radius, blur, and max zoom to fit your data distribution.
- Update the legend location by modifying the CSS values.
- Change number of top countries shown in the legend.
- Further customize the Folium map - see the library docs for more options.
- Additional data cleaning or filtering may be needed depending on your data quality.

## Troubleshooting

- Ensure your CSV data file matches the required format.
- Try different heatmap parameter values if the data looks too dense or sparse.  
- Check that the legend country names match values present in your data.
- Refer to Folium documentation for help customizing the map.

## Disclaimer

This project is intended for educational and informational purposes only. The map visualization provides an overview of attack trends based on the provided data, but does not incorporate additional context or verification.

The results should not be used to make definitive security-related decisions without further analysis. The creator is not responsible for any misuse, misinterpretation, or unintended consequences from the use of this visualization.
