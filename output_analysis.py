import pandas as pd
from geopy.geocoders import Nominatim

def get_input_data(name: str) -> list:
    input_data = pd.read_csv('./input/' + name + '.csv').transpose()
    return list(input_data.iloc[0])

def geocoding(address: str) -> list:
    try:
        geo = geo_local.geocode(address)
        x_y = [geo.latitude, geo.longitude]
        return x_y
    except:
        return [0, 0]

geo_local = Nominatim(user_agent='South Korea')
entire_name = get_input_data('한국행정구역')

num = 0
for i, x in enumerate(entire_name):
    detail_name = get_input_data(x)
    
    for j, y in enumerate(detail_name):
        url = f'./output/{x}/{x}_{y}.csv'
        df = pd.read_csv(url)

        geo_data = []
        for k in range(14):
            geo_data.append(geocoding(df.iloc[k, 1]))
        pd.Series(geo_data).to_csv(f'./output/{x}/geo/geo_{x}_{y}.csv')