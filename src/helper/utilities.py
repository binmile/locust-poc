import os
from random import randint
import uuid, json, pathlib

def getUUID(length=32):
    return str(uuid.uuid4()).replace("-","")[0:length]

def get_random_number_with_N_digit(n=6):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def read_json_file(path):
    # Opening JSON file
    f = open(path, encoding="utf8")
    # returns JSON object as a dictionary
    data = json.load(f)
    f.close()
    return data

def write_data_tojson(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)