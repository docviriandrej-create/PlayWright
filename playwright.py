# ФИО: Дочвири Андрей Аркадьевич
# Дата: 2026-11-09
# Время: 17:40
# Описание: Этот код запускает браузер Chromium, открывает страницу
# playwright.dev и проверяет, что заголовок страницы содержит слово "Playwright".
# Я скопировал пример из раздела "Writing tests" и запустил его локально.
# Результат запуска: "Fast and reliable end-to-end testing for modern web apps | Playwright"
# Код выполнен без ошибок.

import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Ожидаем, что заголовок "содержит" подстроку.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Клик по ссылке "Get started".
    page.get_by_role("link", name="Get started").click()

    # Ожидаем, что на странице будет заголовок с именем Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()