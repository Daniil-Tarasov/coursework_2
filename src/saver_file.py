import json
import os

from src.base_file_saver import BaseFileSaver
# from src.vacancies import Vacancies


class JSONSaver(BaseFileSaver):
    """Класс для работы с файлом JSON"""

    def __init__(self, path: str = "../data/json_vacancies.json"):
        self.path = os.path.abspath(path)
        if not os.path.exists(self.path):
            with open(self.path, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def add_vacancy(self, vacancy_data):
        """Добавляет новую вакансию в файл"""

        dict_vacancies = {
            "name": vacancy_data.name,
            "url": vacancy_data.url,
            "salary": vacancy_data.salary,
            "description": vacancy_data.description,
            "requirements": vacancy_data.requirements
        }
        with open(self.path, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data.append(dict_vacancies)
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_vacancies(self, keyword):
        """Возвращает вакансии по указанному критерию"""

        vacancy_filtered = []
        with open(self.path, "r", encoding='utf-8') as file:
            vacancies = json.load(file)
            for vacancy in vacancies:
                for value in vacancy.values():
                    if keyword == value:
                        vacancy_filtered.append(vacancy)
            return vacancy_filtered

    def del_vacancy(self, name):
        """Удаляет вакансии по указанному имени"""

        new_vacancies = []
        with open(self.path, "r+", encoding='utf-8') as file:
            vacancies = json.load(file)
            for vacancy in vacancies:
                if vacancy.get("name") != name:
                    new_vacancies.append(vacancy)
            file.seek(0)
            file.truncate()
            json.dump(new_vacancies, file, ensure_ascii=False, indent=4)


# if __name__ == "__main__":
    # vac1 = Vacancies("Тестировщик", "https://api.hh.ru/areas/26", {"from": 0, "to": 0, "currency": "RUB"}, "Какое-то описание", "Какие-то требования")
    # save = JSONSaver()
    # save.add_vacancy(vac1)
    # vac1 = Vacancies("Разработчик", "https://api.hh.ru/areas/26", {"from": 0, "to": 0, "currency": "RUB"}, "Какое-то описание", "Какие-то требования")
    # save = JSONSaver()
    # save.add_vacancy(vac1)
    # save.del_vacancy("Разработчик")
