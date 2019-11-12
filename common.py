# ===================================================
# Common Function and Library
# ===================================================
import json

# ===================================================
# jprint
#
# Create a formatted string of the Python JSON object
# ===================================================
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=2)
    print(text)