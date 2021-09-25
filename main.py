import asyncio
from playwright.async_api import async_playwright
from modules.banners import print_banner


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://docs.microsoft.com/en-us/learn/modules/chain-azure-functions-data-using-bindings/2-explore-input-and-output-binding-types-portal-lesson")
        element_handle = await page.query_selector("#unit-inner-section")
        await element_handle.screenshot(path="G:\\projects\\python\\POC\\google-images\\modules\\example.png")
        await browser.close()

asyncio.run(main())
