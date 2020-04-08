import json

# Here the JSON data is in a big string named json_string.
# It starts and the first triple quotation marks and extends
# down to the last triple quotation marks.
json_string = """
{
    "people": [
        {
            "Full Name": "Angst, Annie",
            "Birth Year": 1982,
            "Date Joined": "01/11/2011",
            "Is Active": true,
            "Balance": 300
        },
        {
            "Full Name": "Schadenfreude, Sandy",
            "Birth Year": 2004,
            "Date Joined": "03/03/2003",
            "Is Active": true,
            "Balance": 0
        }
    ]
}
"""

# Load JSON data from the big json_string string.
peep_data = json.loads(json_string)

# Now we can loop through the peep_data collection.
for p in peep_data['people']:
    print(p["Full Name"], p["Birth Year"], p["Date Joined"], p["Is Active"], p["Balance"])
