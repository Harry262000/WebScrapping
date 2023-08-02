import json
import requests
import pandas as pd

# Create a list to store all property details from all pages
all_property_details = []
page = 1
has_more_data = True

while has_more_data:
    url = f"https://www.magicbricks.com/mbsrp/propertySearch.html?editSearch=Y&category=R&propertyType=10002,10003,10021,10022,10020,10001,10017&city=3327&page={page}&groupstart={30 * page}&offset=0&maxOffset=397&sortBy=premiumRecent&postedSince=1&pType=10002,10003,10021,10022,10020,10001,10017&isNRI=N&multiLang=en"
    res = requests.get(url)
    data = json.loads(res.text)
    result_list = data.get('resultList', [])

    if not result_list:
        has_more_data = False
    else:
        for item in result_list:
            property_detail = {
                'Title': item.get('propertyTitle'),
                'Price': item.get('priceD'),
                'Area': f"{item.get('coveredArea')} {item.get('covAreaUnit', '')}",
                'BHK': item.get('bedroomD'),
                'Bathrooms': item.get('bathD'),
                'Furnished': item.get('furnishedD'),
                'Balconies': item.get('balconiesD'),
                'Floor': item.get('floorNo'),
                'Ownership': item.get('OwnershipTypeD'),
                'Facing': item.get('facingD'),
                'Amenities': item.get('amenFacingD'),
                'Transaction Type': item.get('transactionTypeD'),
                'Property Type': item.get('propTypeD'),
                'Location': item.get('ctName'),
                'Year of Construction': item.get('operatingSinceYear'),
                'Is Luxury': item.get('isLuxury'),
                'Description': item.get('auto_desc'),
                'Property Image': item.get('propImg'),
            }
            all_property_details.append(property_detail)

        # Increment the page number for the next iteration
        page += 1

# Create a DataFrame from the property details list
df = pd.DataFrame(all_property_details)

# Save the DataFrame to a JSON file (without index)
json_file_path = 'property_details.json'
df.to_json(json_file_path, orient='records', lines=True)

print(f"Property details saved to {json_file_path}.")
