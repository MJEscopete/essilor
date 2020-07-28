import pandas as pd
from sys import argv

class FileTransformation:
    def __init__(self, filename):
        self.df = pd.read_csv(filename, error_bad_lines=False)
        self.df.columns = map(str.upper, self.df.columns)
        self.entities = self.df["SUB_ENTITY"].unique()

    def group_by_entity(self):
        for entity in self.entities:
            self.df[self.df["SUB_ENTITY"]==entity].to_csv(f"{entity}.csv", index=False)


def main():
    a = FileTransformation("example-file.csv")
    print(a.df)
    a.group_by_entity()


if __name__ == "__main__":
    main()
