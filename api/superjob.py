import os

from dotenv import load_dotenv
from requests import request

from api.api_base import APIbase
from model.vacancy import Vacancy

load_dotenv()
API_KEY = os.getenv("SECRET_KEY")


class SuperJobAPI(APIbase):
    def __init__(self):
        self._vacancies: list = list()
        self._params: dict = {"keywords": ""}
        self._headers: dict = {"X-Api-App-Id": API_KEY}

    @property
    def vacancies(self):
        return self._vacancies

    def get_vacancies(self, search_request: str) -> list:
        self._params["keywords"] = search_request
        data = request(method="GET", url="https://api.superjob.ru/2.0/vacancies/", params=self._params,
                       headers=self._headers).json()["objects"]
        self._vacancies = self._pretty_view(data)
        return self._vacancies

    def _pretty_view(self, data: list) -> list:
        vacancies = []
        for vacancy in data:
            if vacancy["payment_from"] == 0 or vacancy["payment_from"] is None:
                continue
            vacancies.append(Vacancy(
                position=vacancy["profession"],
                url=vacancy["link"],
                salary_from=vacancy["payment_from"],
                salary_to=vacancy["payment_to"],
                description=vacancy["vacancyRichText"],
                must_know=vacancy["candidat"]
            ).__dict__)
        self._vacancies = vacancies
        return self._vacancies

    def get_top_n_vacancies(self, n: int, search_request: str) -> list:
        vacancies = self.get_vacancies(search_request)
        vacancies.sort(key=lambda x: x["salary_from"], reverse=True)
        return vacancies[:n]
