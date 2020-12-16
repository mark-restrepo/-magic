def bucket_multicolor(df):
    def _bucket(df, color):
        return df[df['color'].apply(lambda val: color in val)]

    white_df = _bucket(df, 'W')
    blue_df = _bucket(df, 'U')
    black_df = _bucket(df, 'B')
    red_df = _bucket(df, 'R')
    green_df = _bucket(df, 'G')

    return {
        'white': white_df,
        'blue': blue_df,
        'black': black_df,
        'red': red_df,
        'green': green_df,
    }
