import pandas as pd

# Save Excel file in same folder at this .py file

# Import Excel file sheets
sheet_purchase = pd.read_excel("C:\\Users\\Karishma Mathur\\Documents\\Analyst_Dataset.xlsx", sheet_name=0)
sheet_airings = pd.read_excel("C:\\Users\\Karishma Mathur\\Documents\\Analyst_Dataset.xlsx", sheet_name=1)
sheet_lookup = pd.read_excel("C:\\Users\\Karishma Mathur\\Documents\\Analyst_Dataset.xlsx", sheet_name=2)

# Clean Exit Purchase Survey tab
sheet_purchase = sheet_purchase.fillna(0)
sheet_purchase = sheet_purchase.drop([sheet_purchase.index[0], sheet_purchase.index[1], sheet_purchase.index[2]])
sheet_purchase['Submitted Application Timestamp'] = sheet_purchase['Submitted Application Timestamp'].astype(float)
sheet_purchase['Unnamed: 29'] = sheet_purchase['Unnamed: 29'].astype(float)
sheet_purchase = sheet_purchase.drop(sheet_purchase.columns[0], axis=1)
sheet_purchase.columns = sheet_purchase.iloc[0]
sheet_purchase = sheet_purchase.drop([sheet_purchase.index[0]])

# Create column for purchase count per network
sheet_purchase["Purchases_Count"] = sheet_purchase.sum(axis=1)
sheet_purchase.drop(sheet_purchase.iloc[:, 1:56], inplace = True, axis = 1)

# Clean Lookup tab
sheet_lookup = sheet_lookup.drop(sheet_lookup.columns[2], axis=1)
sheet_lookup.columns = sheet_lookup.iloc[0]
sheet_lookup = sheet_lookup.drop(sheet_lookup.index[0])
sheet_lookup["Exit Survey"] = sheet_lookup["Exit Survey"].str.lower()

# Clean Airings tab
sheet_airings.drop(sheet_airings.iloc[:, 0:4], inplace = True, axis = 1)
sheet_airings = sheet_airings.drop(sheet_airings.columns[3], axis=1)

# Create new dataframes

data1 = [sheet_purchase["Source"], sheet_purchase["Purchases_Count"]]
headers1 = ["Source", "Purchases_Count"]

concat1 = pd.concat(data1, axis=1, keys=headers1)

merge1 = pd.merge(left=concat1,  
                      right=sheet_lookup,  
                      left_on ='Source',  
                      right_on ='Exit Survey') 

merge1 = merge1.drop(merge1.columns[2], axis=1)

# Grouped Spend + Lift in Airings

data2 = [(sheet_airings.groupby("Network")["Spend"].sum()).astype(int),
         (sheet_airings.groupby("Network")["Lift"].sum()).astype(int)]
headers2 = ["Spend", "Lift"]

concat2 = pd.concat(data2, axis=1, keys=headers2)
#concat2['Spend'] = concat2['Spend'].astype(int)
#concat2['Lift'] = concat2['Lift'].astype(int)
concat2["CostperVisitor"] = concat2["Spend"] / concat2["Lift"]

# Merge Cost per Visitor calculation to dataframe

merge2 = pd.merge(left=merge1,
                  right=concat2,
                  left_on = 'Airings',
                  right_on = 'Network')

# Conversion Rate calculation

merge2['Conversion_Rate'] = (merge2['Purchases_Count'] / merge2['Lift'])*100

# CPA calculation

merge2['CPA'] = merge2['Spend'] / merge2['Purchases_Count']

# Cleanup final dataset for report output

merge2 = merge2.drop(merge2.columns[1], axis=1)
merge2 = merge2.drop(merge2.columns[2], axis=1)
merge2 = merge2.drop(merge2.columns[2], axis=1)
merge2.columns = ['Source', 'Network', 'Cost per Visitor', 'Conversion Rate', 'Cost per Acquisition']

print(merge2)

# End of script