import json
import pathlib

import pandas


def get_airlines():
    airlines_file_path = pathlib.Path('../example_data/airlines.txt').resolve()

    with open(airlines_file_path, 'r') as f:
        airlines = json.load(f)

    df = {
        'Name': [al['title'] for al in airlines],
        'Code': [al['airline-code'].upper() for al in airlines],
        'Size': [al['fleet-size'].rstrip('aircraft') for al in airlines],
    }

    return pandas.DataFrame(df)