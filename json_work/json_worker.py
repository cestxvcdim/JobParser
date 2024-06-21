from json_work.utils import DataFile

VACANCIES_DATA_PATH = "./data/vacancies.json"


class JsonWorker:
    @staticmethod
    def add_vacancy(vacancies: list[dict]) -> None:
        DataFile.add_data(VACANCIES_DATA_PATH, vacancies)

    @staticmethod
    def get_vacancies_by_salary(salary_from: int, salary_to: int) -> list:
        result: list = list()
        vacancies = DataFile.read_file(VACANCIES_DATA_PATH)
        for vacancy in vacancies:
            if salary_from <= vacancy["salary_from"] <= salary_to:
                result.append(vacancy)
        return result

    @staticmethod
    def delete_vacancy(vacancies: list[dict]) -> None:
        data: list = DataFile.read_file(VACANCIES_DATA_PATH)
        for vacancy in vacancies:
            if vacancy in data:
                data.remove(vacancy)
        DataFile.write_data(VACANCIES_DATA_PATH, data)
