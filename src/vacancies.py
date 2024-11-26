class Vacancies:
    """Класс для работы с вакансиями"""

    __vacancies_list = []

    def __init__(
            self,
            name: str,
            url: str,
            salary: dict | str = "Зарплата не указана",
            description: str = "Описание не указано",
            requirements: str = "Требования не указаны"
    ):
        """Конструктор класса"""

        self.__name = name
        self.__url = url
        self.__salary = self.__validate(salary)
        self.__description = description
        self.__requirements = requirements
        dict_vacancies = {
            name: self.__name,
            url: self.__url,
            salary: self.__salary,
            description: self.__description,
            requirements: self.__requirements
        }
        self.__vacancies_list.append(dict_vacancies)

    @staticmethod
    def __validate(salary):
        """Метод валидации зарплаты"""

        if salary is None:
            return {"from": 0, "to": 0}
        else:
            return {"from": salary.get("from"), "to": salary.get("to"), "currency": salary.get("currency")}

    def __ge__(self, other):
        """Метод сравнений вакансий по зарплате"""

        if self.__salary.get("to") is None or other.__salary.get("to") is None:
            return self.__salary.get("from") >= other.__salary.get("from")
        elif self.__salary.get("from") is None or other.__salary.get("from") is None:
            return self.__salary.get("to") >= other.__salary.get("to")
        else:
            avg_self_salary = (self.__salary.get("from") + self.__salary.get("to")) // 2
            avg_other_salary = (other.__salary.get("from") + other.__salary.get("to")) // 2
            return avg_self_salary >= avg_other_salary

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def salary(self):
        return self.__salary

    @property
    def description(self):
        return self.__description

    @property
    def requirements(self):
        return self.__requirements


if __name__ == "__main__":
    vac1 = Vacancies("Тестировщик", "https://api.hh.ru/areas/26", {"from": 0, "to": 0, "currency": "RUB"}, "Какое-то описание", "Какие-то требования")
    print(vac1.name)
    print(vac1.url)
    print(vac1.salary)
    print(vac1.description)
    print(vac1.requirements)
