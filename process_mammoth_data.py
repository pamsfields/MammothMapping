import csv

mammoth_data = []

with open('pbdb_data.csv', 'r') as csvfile:

    reader = csv.reader(csvfile)

    # The first row is the column types, read this line. Keep if needed, but we can discard.
    columns = reader.__next__()

    # Are interested in col 9, accepted_name
    # Abundance val and abundance unit 22 and 23
    # lat, lng, cols 24 and 25
    # State, county, in 27 , 28
    # geocomment 32
    for row in reader:

        # get data of interest. Convert numeric types to floats
        # write out to new CSV file that another module can read
        name = row[9]
        abd = row[22]
        abd_unit = row[23]
        lat = float(row[25])  # These are reversed from expected order
        lng = float(row[24])  # lng first, then lat
        state = row[27]
        county = row[28]
        comment = row[32]

        mammoth_data.append([name, abd, abd_unit, lat, lng, state, county, comment])


with open('mammoth_data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(['name', 'abd', 'abd_unit', 'lat', 'lng', 'state', 'county', 'comment'])
    writer.writerows(mammoth_data)
