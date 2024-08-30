# Image Data Merger
This Python script provides a solution for merging image data from a separate CSV file (images.csv) into a main download data CSV file (download.csv). It achieves this by matching item numbers between the files and associating the corresponding image URLs with relevant columns in the download data.

# Features
- Loads CSV files using pandas library.
- Extracts specific columns from the image data file.
- Creates new columns in the download data file for image URLs.
- Iterates through image data and merges information based on item number.
- Assigns image URLs to "featured_image" or "product_image_gallery" columns based on a flag.
- Saves the merged data to a new CSV file.
  
# Usage
## Prerequisites:
- Python environment with pandas library installed (e.g., pip install pandas).
- Two CSV files:
  - images.csv: Containing columns "itemNumber", "url", and "main" (where "main" is a flag indicating the featured image).
  - download.csv: Your main download data with an "itemNumber" column.
## Running the Script:
- Save the Python script as image_data_merger.py in the same directory as your CSV files.
- Execute the script using a Python interpreter or environment (e.g., python image_data_merger.py).
## Output:
- A new CSV file named merged_download1.csv will be created containing the merged data.
  
# Code Structure
The script leverages pandas for efficient data manipulation and utilizes several key functions:

- pd.read_csv: Reads data from CSV files.
- DataFrame.iterrows: Iterates over rows in a DataFrame.
- DataFrame.loc: Accesses and modifies specific rows/columns based on labels.
## Contributing
Feel free to fork this repository and make improvements! Consider adding functionalities like handling missing values or customizing the output filename.

## License
This code is provided under the MIT License.
