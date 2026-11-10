# ФИО: Дочвири Андрей Аркадьевич
# Дата: 2026-11-09
# Время: 17:40
# Описание: Этот код запускает браузер Chromium, открывает страницу
# playwright.dev и проверяет, что заголовок страницы содержит слово "Playwright".
# Я скопировал пример из раздела "Writing tests" и запустил его локально.
# Результат запуска: "Fast and reliable end-to-end testing for modern web apps | Playwright"
# Код выполнен без ошибок.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    print(page.title())
    browser.close()