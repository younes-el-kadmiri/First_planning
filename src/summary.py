def show_stats(df):
    print(df.info())
    print(df.describe())

def count_gender(df):
    print(df['gender'].value_counts())
