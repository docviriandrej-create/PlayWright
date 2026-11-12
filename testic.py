# ФИО: Дочвири Андрей Аркадьевич
# Дата: 2026-11-12
# Время: 17:05
# Описание: Этот код переходит на страницу, проверяет что страница загрузилась, добовляет задачу, отмечает задачу как выполненную.


import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/")
    page.goto("https://demo.playwright.dev/todomvc/#/")
    expect(page.get_by_test_id("todo-title")).to_be_visible()
    page.get_by_role("heading", name="todos").click()
    page.get_by_text("This is just a demo of TodoMVC for testing, not the real TodoMVC app. todosMark").press("Enter")
    page.get_by_test_id("todo-title").click()
    expect(page.get_by_text("This is just a demo of")).to_be_visible()
    page.get_by_text("This is just a demo of TodoMVC for testing, not the real TodoMVC app. todosMark").click()
    page.get_by_test_id("todo-title").click()
    page.get_by_text("item leftAll Active Completed").click()
    page.get_by_role("heading", name="todos").click()
    page.get_by_role("heading", name="todos").click()
    expect(page.get_by_test_id("todo-title")).to_be_visible()
    page.get_by_role("link", name="Completed").click()
    page.get_by_role("link", name="All").click()
    page.get_by_test_id("todo-title").click()
    page.get_by_role("heading", name="todos").click()
    page.get_by_text("This is just a demo of").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)