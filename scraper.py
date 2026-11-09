from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch()
    page=browser.new_page()
    page.goto("https://www.vitibet.com/index.php?clanek=quicktips&sekce=fotbal&lang=en")
    print(page.title())
    overRows=page.locator(".t5o-box .t5o-row").all()
    underRows=page.locator(".t5u-box .t5u-row").all()
    print(len(overRows))
    print
    print("---OVER 2.5 GOALS---")
    for row in page.locator(".t5o-box .t5o-row").all():
        print(row.inner_text())
    print("---UNDER 2.5 GOALS---")
    for row in page.locator(".t5u-box .t5u-row").all():
            print(row.inner_text())
    
    browser.close()
