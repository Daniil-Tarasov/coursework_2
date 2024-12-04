from src.vacancies import Vacancies

vac1 = Vacancies("Тестировщик", "https://hh.ru/", {"from": 1, "to": 2, "currency": "RUB"}, "Как-то", "Что-то")
vac2 = Vacancies.get_vacancies_from_list(
    [
        {
            "name": "Разработчик",
            "url": "https://hh.ru/",
            "salary": {"from": 1, "to": 2, "currency": "RUB"},
            "snippet": {"responsibility": "разрабатывать", "requirements": "жив"},
        }
    ]
)


def test_init_vacancies():
    assert vac1.name == "Тестировщик"
    assert vac1.url == "https://hh.ru/"
    assert vac1.salary == {"from": 1, "to": 2, "currency": "RUB"}
    assert vac1.responsibility == "Как-то"
    assert vac1.requirements == "Что-то"


def test_get_vacancies_from_list():
    assert vac2 == [
        {
            "name": "Тестировщик",
            "url": "https://hh.ru/",
            "salary": {"from": 1, "to": 2, "currency": "RUB"},
            "responsibility": "Как-то",
            "requirements": "Что-то",
        },
        {
            "name": "Разработчик",
            "url": "https://hh.ru/",
            "salary": {"from": 1, "to": 2, "currency": "RUB"},
            "responsibility": "разрабатывать",
            "requirements": "жив",
        },
    ]


def test_validate_data():
    vac3 = Vacancies.get_vacancies_from_list(
        [
            {
                "name": "Разработчик",
                "alternate_url": "https://hh.ru/",
                "salary": {"from": 1, "to": 2, "currency": "RUB"},
                "snippet": {},
            }
        ]
    )
    assert vac3 == [
        {
            "name": "Тестировщик",
            "url": "https://hh.ru/",
            "salary": {"from": 1, "to": 2, "currency": "RUB"},
            "responsibility": "Как-то",
            "requirements": "Что-то",
        },
        {
            "name": "Разработчик",
            "url": "https://hh.ru/",
            "salary": {"from": 1, "to": 2, "currency": "RUB"},
            "responsibility": "разрабатывать",
            "requirements": "жив",
        },
        {
            "name": "Разработчик",
            "url": "https://hh.ru/",
            "salary": {"from": 1, "to": 2, "currency": "RUB"},
            "responsibility": "Обязанности не указаны",
            "requirements": "Требования не указаны",
        },
    ]


def test_str_vacancies():
    assert (
        str(vac1)
        == "Тестировщик - https://hh.ru/. Зарплата: {'from': 1, 'to': 2, 'currency': 'RUB'}. Описание: Как-то. Требования: Что-то."
    )


# def test_comparison_vacancies():
#     assert vac1.__ge__(vac2) == True
