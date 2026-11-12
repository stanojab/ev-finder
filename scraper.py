from playwright.sync_api import sync_playwright
def scrape_box(page, prefix):
    rows = page.locator(f".{prefix}-box .{prefix}-row").all()
    matches = []

    for row in rows:
        home_team = row.locator(f".{prefix}-team").first.inner_text()
        away_team = row.locator(f".{prefix}-team").nth(1).inner_text()
        meta_data = row.locator(f".{prefix}-meta").inner_text().split(" · ")
        probability = row.locator(f".{prefix}-idx b").inner_text().replace("%", "")

        match = {
            "home": home_team,
            "away": away_team,
            "time": meta_data[0],
            "country": meta_data[1],
            "league": meta_data[2],
            "probability": int(probability),
        }
        matches.append(match)

    return matches
with sync_playwright() as p:
    browser=p.chromium.launch()
    page=browser.new_page()
    page.goto("https://www.vitibet.com/index.php?clanek=quicktips&sekce=fotbal&lang=en")
    print(page.title())
    print("---OVER 2.5 GOALS---")
    over_matches=scrape_box(page, "t5o")
    for match in over_matches:  
        print(f"{match['home']} | {match['away']} | {match['time']} | {match['country']} | {match['league']} | {match['probability']}")
    print("---UNDER 2.5 GOALS---")
    under_matches=scrape_box(page,"t5u")
    for match in under_matches:
        print(f"{match['home']} | {match['away']} | {match['time']} | {match['country']} | {match['league']} | {match['probability']}")
    
    browser.close()
