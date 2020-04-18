import requests
import csv
import pandas as pd
from resources import Resources as R


def get_csv_request(url):
    with requests.Session() as s:
        download = s.get(url)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        nested_list = list(cr)
    return nested_list


if __name__ == "__main__":
    confirmed_file = R.JOHN_HOPKINS_BASE_URL + R.JOHN_HOPKINS_TIME_SERIES_FOLDER + R.JOHN_HOPKINS_CONFIRMED_FILE

    confirmed = get_csv_request(confirmed_file)
    df = pd.DataFrame(confirmed[1:], columns=confirmed[0])
    print(df)
