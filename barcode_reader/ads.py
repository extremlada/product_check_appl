import asyncio

from playwright.async_api import async_playwright
import requests

async def get_cookie_playwright():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://online.auchan.hu")
        await page.click("onetrust-accept-btn-handler")
        cookie = await context.cookies()
        print(cookie)

asyncio.run(get_cookie_playwright())
