import pandas as pd

class CSVFile:

    def __init__(self, file):
        self.file = file

    # @staticmethod
    # def is_csv(file):
    #     if file is None:
    #         return False
    #     return file.name.lower().endswith(".csv")
    #
    # @staticmethod
    # def is_json(jfile):
    #     if jfile is None:
    #         return False
    #     return jfile.name.lower().endswith(".js")

    @staticmethod
    def load_dataframe(file):
        # file.seek(0)
        #
        # content = file.getvalue()
        #
        # if not content.strip():
        #     raise  ValueError("Uploaded CSV file is empty")
        #
        # file.seek(0)
        #
        name = file.name.lower()

        if name.endswith(".csv"):
            return pd.read_csv(file)

        if name.endswith(".js"):
            return pd.read_json(file)

        raise ValueError("Unsupported file type.")

