import pandas as pd

def get_input_data(name: str) -> list:
    input_data = pd.read_csv('./input/' + name + '.csv').transpose()
    return list(input_data.iloc[0])

def put_level_data(x: str, y: str, level: int) -> None:
    try:
        url = f'./output/{x}/{x}_{y}.csv'
        data = pd.read_csv(url)
        data['level'] = level
        print(data)
        data.to_csv(f'./output/{x}/{x}_{y}.csv', index=False)
    except:
        print("error")

df = pd.read_csv('level.csv')
df['level'] = 0
for i in range(188):
    if i <= 10:
        df.loc[i, 'level'] = 1
        print(1)
        put_level_data(df.loc[i, '광역지자체명'], df.loc[i, '기초지자체명'], 1)
    elif i <= 35:
        df.loc[i, 'level'] = 2
        put_level_data(df.loc[i, '광역지자체명'], df.loc[i, '기초지자체명'], 2)
    elif i <= 70:
        df.loc[i, 'level'] = 3
        put_level_data(df.loc[i, '광역지자체명'], df.loc[i, '기초지자체명'], 3)
    elif i <= 120:
        df.loc[i, 'level'] = 4
        put_level_data(df.loc[i, '광역지자체명'], df.loc[i, '기초지자체명'], 4)
    else:
        df.loc[i, 'level'] = 5
        put_level_data(df.loc[i, '광역지자체명'], df.loc[i, '기초지자체명'], 5)
        