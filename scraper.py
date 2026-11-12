from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch()
    page=browser.new_page()
    page.goto("https://www.vitibet.com/index.php?clanek=quicktips&sekce=fotbal&lang=en")
    print(page.title())
    over_rows=page.locator(".t5o-box .t5o-row").all()
    under_rows=page.locator(".t5u-box .t5u-row").all()
    print(len(over_rows))
    print()
    print("---OVER 2.5 GOALS---")
    for row in over_rows:
        home_team_row=row.locator(".t5o-team").first.inner_text()
        away_team_row=row.locator(".t5o-team").nth(1).inner_text()
        meta_data=row.locator(".t5o-meta").first.inner_text().split(" · ")
        start_time=meta_data[0]
        country=meta_data[1]
        league=meta_data[2]
        probability=row.locator(".t5o-idx b").inner_text().replace("%", "")
        probability_num=int(probability)
    
        print(f"{home_team_row} | {away_team_row} | {start_time} | {country} | {league} | {probability_num}")
    print("---UNDER 2.5 GOALS---")
    for row in under_rows:
        home_team_row=row.locator(".t5u-team").first.inner_text()
        away_team_row=row.locator(".t5u-team").nth(1).inner_text()
        meta_data=row.locator(".t5u-meta").first.inner_text().split(" · ")
        start_time=meta_data[0]
        country=meta_data[1]
        league=meta_data[2]
        probability=row.locator(".t5u-idx b").inner_text().replace("%", "")
        probability_num=int(probability)
        
        print(f"{home_team_row} | {away_team_row} | {start_time} | {country} | {league} | {probability_num}")
    # ·
    browser.close()
