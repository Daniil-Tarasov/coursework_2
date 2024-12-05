from src.hh_api import HHApi
from src.saver_file import JSONSaver
from src.utils import compare_salaries
from src.vacancies import Vacancies


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    keyword = input("Введите поисковый запрос: ")
    print("Идёт поиск... ")
    hh = HHApi(file_worker="../data/vacancies.json")
    vacancies = hh.load_vacancies(keyword)  # получаем вакансии
    vacancies = Vacancies.get_vacancies_from_list(vacancies)  # записываем вакансии в класс Vacancies
    data = JSONSaver()
    data.add_vacancy(vacancies)  # записываем данные в JSON файл
    top = int(input("Введите количество вакансий для вывода в топ N: "))
    vacancies = data.load_data()
    top_vacancies = sorted(
        vacancies, key=lambda x: x["salary"].get("to", 0) or 0, reverse=True
    )  # сортируем вакансии по зарплате
    print(f"Топ {top} вакансий по зарплате:")
    for i, vacancy in enumerate(top_vacancies[:top], start=1):
        print(f"{i}. {vacancy['name']} - Зарплата: от {vacancy['salary']["from"]} до {vacancy['salary']["to"]}")
    keyword = input("Введите ключевое слово для поиска вакансий ")
    filtered_vacancies = data.get_vacancies(keyword)
    for vacancy in filtered_vacancies:
        print(
            f"{vacancy["name"]} - Зарплата: от {vacancy['salary']["from"]} до {vacancy['salary']["to"]}. {vacancy["responsibility"]}. {vacancy["requirements"]}"
        )
    question = input("Желаете сравнить 2 вакансии по зарплате?(да/нет) ")
    if question.lower() == "да":
        name1 = input("Укажите название первой вакансии ")
        name2 = input("Укажите название второй вакансии ")
        result = compare_salaries(vacancies, name1, name2)
        if result:
            print("Зарплата первой вакансии больше")
        else:
            print("Зарплата во второй вакансии больше")


# if __name__ == "__main__":
#     user_interaction()
