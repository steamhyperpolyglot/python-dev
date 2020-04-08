import json

# Here the JSON data is in a big string named json_string
# It starts and the first triple quotation marks and extends
# down to the last triple quotation marks.
json_string = """
{
    "1": {
        "count": 9061,
        "lastreferrer": "https://difference-engine.com/Courses/tml-5-1118",
        "lastvisit": "12/20/2018",
        "page": "/etg/downloadpdf.html"
    },
    "2": {
        "count": 3342,
        "lastreferrer": "https://alansimpson.me/",
        "lastvisit": "12/09/2018",
        "page": "/html_css/index.html"
    }
}
"""

# Load JSON data from the big json_string string.
hits = json.loads(json_string)

# Now you can loop through the hits_data collection.
for k, v in hits.items():
    print(f"{k}. {v['count']:>5} - {v['page']}")

# Now look at the lastvisit date in the hits dictionary.
for k, v in hits.items():
    print(k,v)

# Copy new dictionary to JSON string.
new_dict = json.dumps(hits, indent=2, ensure_ascii=False)
print(new_dict)

# Write the modified data to a JSON file named hitcounts_new.json
with open('hitcounts_new.json', 'w', encoding='utf-8') as out_file:
    json.dump(hits, out_file, ensure_ascii=False, sort_keys=True)

print('Done')