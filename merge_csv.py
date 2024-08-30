import csv
import pandas as pd

# Load images.csv and extract required columns
images_df = pd.read_csv('images.csv', usecols=['itemNumber', 'url', 'main'])

# Load download.csv
download_df = pd.read_csv('download.csv')

# Add new columns to download.csv
download_df['featured_image'] = ''
download_df['product_image_gallery'] = ''

# Iterate over images.csv and merge data
for index, row in images_df.iterrows():
    item_number = row['itemNumber']
    url = row['url']
    main = row['main']

    # Find matching itemNumber in download.csv
    match = download_df[download_df['itemNumber'] == item_number]

    if not match.empty:
        if main == 1:
            download_df.loc[match.index, 'featured_image'] = url
        else:
            current_gallery = download_df.loc[match.index, 'product_image_gallery'].values[0]
            if current_gallery:
                download_df.loc[match.index, 'product_image_gallery'] = current_gallery 
            else:
                download_df.loc[match.index, 'product_image_gallery'] = url

    else:
        print(f"No matching itemNumber found for {item_number}")

# Save the merged download.csv file
download_df.to_csv('merged_download1.csv', index=False)