import pandas as pd
from sqlalchemy import create_engine

data_file_path = "/home/aneesh/Downloads/employee_dataset/employee_records.csv"
chunk_size = 100

def load_data(file_path: str, chunk_size: int = chunk_size) -> pd.DataFrame:
    data = pd.read_csv(file_path, chunksize=chunk_size)
    yield data


if __name__ == "__main__":
    for _ in range(2):
        data_chunk = next(load_data(data_file_path))
        print(data_chunk.head())