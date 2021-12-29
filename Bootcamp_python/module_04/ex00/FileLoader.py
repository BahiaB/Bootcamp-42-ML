import pandas as pd

class FileLoader:
    
    def load(path):
        df = pd.read_csv(path)
        print(f'Loading dataset of dimensions {df.shape[0]} {df.shape[1]}')
        #print(df[0:50])
        return(df)

    def display(df, n):
        if n > 0:
            print(df[0 : n])
        else:
            print(df[:n-1:-1])

