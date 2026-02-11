import pandas as pd
from math import radians, sin, cos, sqrt, atan2

def haversine_formula(lat1, long1, lat2, long2):
    if lat1==lat2 and long1==long2:
        return 0

    R = 6371

    lat1_rad = radians(lat1)
    long1_rad = radians(long1)
    lat2_rad = radians(lat2)
    long2_rad = radians(long2)

    dlat = lat2_rad - lat1_rad
    dlong = long2_rad - long1_rad

    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlong / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c 
    return round(distance, 2) 


postcodes = pd.read_csv('australian_postcodes.csv')
postcodes_list = postcodes['postcode'].tolist()

distance_matrix = pd.DataFrame(index = postcodes_list, columns = postcodes_list)

for index_i, row_i in postcodes.iterrows():
    for index_j, row_j in postcodes.iterrows():
        row_i_lat = row_i['lat']
        row_i_long = row_i['long']
        row_i_postcode = row_i['postcode']

        row_j_lat = row_j['lat']
        row_j_long = row_j['long']
        row_j_postcode = row_j['postcode']

        distance = haversine_formula(row_i_lat, row_i_long, row_j_lat, row_j_long)

        distance_matrix.loc[row_i_postcode, row_j_postcode] = distance
        distance_matrix.loc[row_j_postcode, row_i_postcode] = distance

        print(f"found distance for {row_i_postcode} and {row_j_postcode}: {distance}")

distance_matrix.to_csv('distance_matrix.csv')




