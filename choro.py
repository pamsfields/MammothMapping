import pandas, folium, json

data = pandas.read_csv('mammoth_data.csv')  # dataframe from CSV

# Need to aggregate all fossils for one state. Some records have more than one
# mammoth discovered. The abd column has the number of fossils found at the site

# Create a quantity column with a copy of the abd column
quantities = data['abd']
# If there is no data, assume that the record is for one mammoth
quantities = quantities.fillna(value = 1)

# Add the new column to the dataframe
data['quantity'] = quantities

# Group by state, and sum the columns. We only need the sum of the quantity column.
# groupby returns a GroupBy object. reset_index() turns that object into a DataFrame
state_data_groups = data.groupby(by=['state']).sum().reset_index()

# Add missing states to dataframe.  About 15 states have no mammoths.
# Choropleth will error if states are missing (Extra regions, countries, or states will be ignored)
# Need to add a row with a zero value for missing states.
states_abbr = json.load(open('us_states_abbr.json'))
state_list = list(states_abbr.keys())

# Create a data frame from state names, with zero for each quantity
all_states_zeros = pandas.DataFrame({ 'state':state_list, 'quantity': 0 } )

# Append the zeros dataframe to the end of state_data_groups
all_states_data = state_data_groups.append(all_states_zeros)

# Drop second of duplicate value for the 'state' series,
#which will remove the zero version for states that were already in the dataframe
all_states_data = all_states_data.drop_duplicates('state', keep='first')

# Neat! Replace with dictionary of { orig: replace } ; which are in the form { 'Minnesota' : 'MN'}
state_data_groups = all_states_data.replace(states_abbr)

print(state_data_groups)


# And create the choropleth map

us_states_file = r'us_states.json'   # Path to geo-json file

choromap = folium.Map(location=[40, -120], zoom_start=3)

choromap.choropleth(
    geo_path=us_states_file,   # Reads this file
    data=state_data_groups,
    columns=['state', 'quantity'],
    key_on='id',     # The key in the geo_path data
    fill_color='BuPu', fill_opacity=0.6, line_opacity=0.4,
    threshold_scale=[0,5,10,15,20,90],  # six items max
    legend_name="Mammoth finds per state"
)

choromap.save('mammoth_choropleth.html')

#TODO - display more data when states are hovered over.
#This would help http://leafletjs.com/examples/choropleth/
