# Modules
import os
import csv
#import datetime
from datetime import datetime
#the dictionary of the state names and the abbreviations  
stateabbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# CSV File
filename = os.path.join( "employee_data.csv")
# Lists to store data
fields= []
empid = []
firstname = []
lastname = []
dob = []
ssn = []
state = []
header = ["Emp Id", "First name", "Last Name", "Dob",
                "SSN", "State"]
# Open CSV file reader
with open(filename, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    fields = next(csvreader) 

    for row in csvreader:
        # Add emp_id
        empid.append(row[0])
        # Spliting the name in first and last
        fname = row[1].split(" ")[0]
        lname = row[1].split(" ")[1]
        # Add first name
        firstname.append(fname)
        # Add last name
        lastname.append(lname)
        # Add dob after converting the format
        date_strip = datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y')
        dob.append(date_strip)
        # Add ssn after masking 
        ssn.append("***-**-" + (row[3])[-4:])
        # Add state
        state.append(stateabbrev[row[4]])


# Zip lists together
filewrite_csv = zip(empid, firstname, lastname, dob, ssn, state)
# Set variable for output file
output_file = os.path.join("emp_data_out.csv")
# Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    # Write the header row
    writer.writerow(header)
    # Write in zipped rows
    writer.writerows(filewrite_csv)

