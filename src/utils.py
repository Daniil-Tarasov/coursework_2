from src.vacancies import Vacancies


def compare_salaries(vacancies: list, name1: str, name2: str) -> bool:
    """True, если зарплата первой вакансии больше"""

    vacancy_dict1 = {}
    vacancy_dict2 = {}

    for vacancy in vacancies:
        if name1.lower() == vacancy["name"].lower():
            vacancy_dict1 = vacancy
            break

    for vacancy in vacancies:
        if name2.lower() == vacancy["name"].lower() and vacancy != vacancy_dict1:
            vacancy_dict2 = vacancy
            break

    vacancy1 = Vacancies(**vacancy_dict1)
    vacancy2 = Vacancies(**vacancy_dict2)
    return vacancy1.__ge__(vacancy2)


# if __name__ == "__main__":
#     vacancie_list = [
#         {
#             "name": "Тестировщик",
#             "url": "https://hh.ru/",
#             "salary": {"from": 1, "to": 2, "currency": "RUB"},
#             "responsibility": "Как-то",
#             "requirements": "Что-то",
#         },
#         {
#             "name": "Разработчик",
#             "url": "https://hh.ru/",
#             "salary": {"from": 1, "to": 2, "currency": "RUB"},
#             "responsibility": "разрабатывать",
#             "requirements": "жив",
#         },
#         {
#             "name": "Разработчик",
#             "url": "https://hh.ru/",
#             "salary": {"from": 1, "to": 2, "currency": "RUB"},
#             "responsibility": "Обязанности не указаны",
#             "requirements": "Требования не указаны",
#         }
#     ]
#
#     print(compare_salaries(vacancie_list, "тестировщик", "разработчик"))
