import json
import os
from datetime import date

# Load data
def load_data(file):
    if os.path.exists(file):
        f = open(file, "r")
        data = json.load(f)
        f.close()
        return data
    else:
        return []


# Save data
def save_data(file, data):
    f = open(file, "w")
    json.dump(data, f, indent=4)
    f.close()