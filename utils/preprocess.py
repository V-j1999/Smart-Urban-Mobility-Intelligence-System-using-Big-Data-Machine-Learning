def clean_data(df):
    df = df[df['trip_distance'] > 0]
    df = df[df['fare_amount'] > 0]
    return df
