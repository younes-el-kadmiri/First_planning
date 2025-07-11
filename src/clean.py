def clean_data(df):
    for col in df.select_dtypes(include='number').columns:
        df[col].fillna(df[col].mean(), inplace=True)

    for col in ['name', 'education', 'city', 'notes']:
        df[col].fillna('Unknown', inplace=True)
        df[col].replace('', 'Unknown', inplace=True)

    return df
