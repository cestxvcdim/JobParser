from dataclasses import dataclass


@dataclass
class Vacancy:
    """
    Класс для представления вакансии.

    Атрибуты:
    position (str): Название вакансии.
    url (str): Ссылка на вакансию.
    salary_from (int): Нижняя граница зарплаты.
    salary_to (int): Верхняя граница зарплаты.
    description (str): Описание вакансии.
    must_know (str): Необходимые навыки и требования.
    """
    position: str
    url: str
    salary_from: int
    salary_to: int
    description: str
    must_know: str
