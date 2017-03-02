
import pandas, folium, json


choromap = folium.Map(location=[40, -100], zoom_start=4)
us_states = r'us_states.json'   # TODO what?

data = pandas.read_csv('mammoth_data.csv')  # dataframe from CSV

# Need to aggregate all fossils for one state into a new dataframe
# TODO Add up the abund_unit value (or 1 if not present) for each state

# groupby returns a GroupBy object. reset_index() turns that object into a DataFrame
state_data_groups = data.groupby(by=['state']).count().reset_index()

states_abbr = json.load(open('us_states_abbr.json'))

# Add missing states to dataframe or choropleth will error
# Extra regions, countries, or states will be ignored
# TODO is there a shortcut for this?
for abbr in states_abbr.keys():
    if abbr not in state_data_groups['state'].values:
        state_data_groups = state_data_groups.append({'state':abbr, 'name':0}, ignore_index=True)

# Neat! Replace with dictionary of { orig: replace }
state_data_groups = state_data_groups.replace(states_abbr)

choromap.choropleth(geo_path=us_states,   # does this read the file?
data=state_data_groups,
columns=['state', 'name'],
key_on='id',     # The key in the geo_path
fill_color='BuPu', fill_opacity=0.6, line_opacity=0.4,
threshold_scale=[0,1,5,10,20,40],  # six items max!
legend_name="Mammoth finds per state"
)

choromap.save('mammoth_choropleth.html')
