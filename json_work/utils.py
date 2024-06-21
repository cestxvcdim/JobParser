import json


class DataFile:
    @staticmethod
    def read_file(path: str) -> list:
        data: list = []
        try:
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("File was empty")
        finally:
            return data

    @staticmethod
    def write_data(path: str, data: list) -> None:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def add_data(path: str, data: list) -> None:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
