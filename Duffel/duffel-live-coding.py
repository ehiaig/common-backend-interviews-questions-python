# Return a sorted result based on the Price
results = [
    {
        'destination': 'LGW',
        'origin': 'JFK',
        'arrival_time': '17:50',
        'departure_time': '18:00',
        'price': '432GBP',
        'source': 'duffel_air'
    },
    {
        'flights': 'JFK/LGW',
        'arrival_time': '17:50',
        'departure_time': '18:00',
        'price_fractional': '12300',
        'currency_code': 'GBP',
        'source': 'virgin'
    },
    {
        'flights': 'JFK/LGW',
        'arrival_time': '19:30',
        'departure_time': '15:00',
        'price_fractional': '10900',
        'currency_code': 'GBP',
        'source': 'virgin'
    },
    {
        'destination_code': 'lgw',
        'origin_code': 'jfk',
        'arrival_datetime': '2020-07-23 12:07:53 +0000',
        'departure_time': '2020-07-23 09:01:20 +0000',
        'price': {
            'code': 'USD',
            'value': '325.50'
        },
        'source':  'aa'
    },
    {
        'destination_code': 'lgw',
        'origin_code': 'jfk',
        'duration': '542',
        'take_off_at': '2020-07-23 09:01:20 +0000',
        'price': {
            'code': 'GBP',
            'value': '425.50'
        },
        'source': 'ba',
    }
]


import re

def refactor_list(result):
    my_list = []
    for key, row in enumerate(result):
        row = row.copy()
        if row["source"] == "aa":
            row["price"] = float(row["price"]['value'])/0.8
        elif row["source"] == "ba":
            row["price"] = float(row["price"]["value"])
        elif row["source"] == "virgin":
            row["price"] = float(row["price_fractional"])
        else:
            price_split = re.split('(\d+)', row["price"])
            row["price"] = float(price_split[1])
            row["currency_code"] = price_split[2]
        row["id"] = key
        my_list.append(row)
    return sorted(my_list, key=lambda x: x["price"])


def sorted_result(result_lists):
    sorted_list = refactor_list(result_lists)
    sorted_ind = [i["id"] for i in sorted_list]
    result = [result_lists[i] for i in sorted_ind]
    print("final", result)

sorted_result(results)