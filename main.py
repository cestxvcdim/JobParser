from json_work.json_worker import JsonWorker

from api.head_hunter import HeadHunterAPI
from api.superjob import SuperJobAPI


hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()


def print_vacancy(vacancy):
    print(f'Должность - {vacancy["position"]}\n'
          f'Ссылка - {vacancy["url"]}\n'
          f'Зарплата {vacancy["salary_from"]} - {vacancy["salary_to"]}\n'
          f'Описание - {vacancy["description"]}\n'
          f'Требования - {vacancy["must_know"]}\n')


def user_interaction():
    vacancies = []
    print("Приветствуем, друг! Где будем искать вакансии?")
    chosen_platform = input("Введи цифру 1 или 2\n1 - HeadHunter\n2 - Superjob\n")
    query = input("По какой профессии ищешь вакансии?\n")
    check = True
    while check:
        if ("1" not in chosen_platform and "2" not in chosen_platform) or ("1" in chosen_platform and "2" in chosen_platform):
            print('Что-то пошло не так, друг. Попробуй снова')
            chosen_platform = input("Введи цифру 1 или 2\n1 - HeadHunter\n2 - Superjob\n")
            query = input("По какой профессии ищешь вакансии?\n")
            continue
        check = False

    if "1" in chosen_platform:
        vacancies = hh_api.get_vacancies(query)
    elif "2" in chosen_platform:
        vacancies = superjob_api.get_vacancies(query)

    for vacancy in vacancies:
        print_vacancy(vacancy)
    JsonWorker.add_vacancy(vacancies)

    salary_from, salary_to = map(int, input("Введи, в каком диапазоне хочешь видеть вакансии:\n"
                                            "(в формате '1000-2000')\n").split('-'))

    for vacancy in JsonWorker.get_vacancies_by_salary(salary_from, salary_to):
        print_vacancy(vacancy)
    JsonWorker.delete_vacancy(vacancies)

    n = int(input("Получи топ N вакансий, введи N:\n"))
    query = input("Теперь введи профессию:\n")
    print("Предложения из HeadHunter")
    hh_vacancies = hh_api.get_top_n_vacancies(n, query)
    for v in hh_vacancies:
        print_vacancy(v)
    print("Предложения из Superjob")
    sj_vacancies = superjob_api.get_top_n_vacancies(n, query)
    for v in sj_vacancies:
        print_vacancy(v)


if __name__ == "__main__":
    user_interaction()
