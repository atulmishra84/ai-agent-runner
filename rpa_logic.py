
import os
import asyncio
from playwright.async_api import async_playwright

ENTRA_LOGIN = "rpabot@idenaccess.onmicrosoft.com"
ENTRA_PASSWORD = "Creation@12345"

async def run_rpa_task(user_data):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--start-maximized"])
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://entra.microsoft.com")
        await page.get_by_label("Email, phone, or Skype").fill(ENTRA_LOGIN)
        await page.get_by_role("button", name="Next").click()
        await page.get_by_label("Enter the password").fill(ENTRA_PASSWORD)
        await page.get_by_role("button", name="Sign in").click()
        await page.get_by_role("button", name="Yes").click()

        await page.wait_for_timeout(5000)
        await page.mouse.wheel(0, 1000)
        await page.wait_for_timeout(2000)
        await page.screenshot(path="entra-dashboard.png")

        await page.mouse.move(100, 300)
        await page.mouse.click(100, 300)
        for _ in range(10):
            await page.keyboard.press("Tab")
            await page.wait_for_timeout(200)
        await page.keyboard.press("Enter")
        await page.wait_for_timeout(3000)
        await page.screenshot(path="after-keyboard-users.png")

        await page.locator("span.ms-Button-label:has-text('New user')").click()
        await page.wait_for_timeout(1000)

        try:
            await page.locator("span.ms-Button-label:has-text('Create new user')").click()
        except Exception:
            try:
                await page.locator("text='Create new user'").click()
            except Exception as e:
                await page.screenshot(path="error-create-new-user-span.png")
                raise Exception(f"❌ Could not click span-based 'Create new user': {str(e)}")

        await page.wait_for_timeout(2000)
        await page.screenshot(path="after-create-user-span-click.png")

        await page.wait_for_selector("input[aria-label='User principal name']", timeout=60000)
        await page.fill("input[aria-label='User principal name']", user_data["username"])
        await page.fill("input[aria-label='Display name']", user_data["display_name"])
        await page.fill("input[type='password']", user_data["password"])

        await page.locator("button:has-text('Review + create')").click()
        await page.wait_for_timeout(1000)
        await page.locator("button:has-text('Create')").click()
        await page.wait_for_timeout(3000)
        await page.screenshot(path="user-creation-complete.png")

        await browser.close()
        return "✅ User created successfully using span-based dropdown"

def launch_rpa_agent(username, display_name, password):
    user_data = {
        "username": username,
        "display_name": display_name,
        "password": password
    }
    try:
        result = asyncio.run(run_rpa_task(user_data))
        return result, "user-creation-complete.png"
    except Exception as e:
        return f"❌ RPA failed: {str(e)}", "error-create-new-user-span.png"
