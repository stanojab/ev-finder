from playwright.sync_api import sync_playwright
def scrape_box(page, prefix):
    rows = page.locator(f".{prefix}-box .{prefix}-row").all()
    matches = []

    for row in rows:
        home_team = row.locator(f".{prefix}-team").first.inner_text()
        away_team = row.locator(f".{prefix}-team").nth(1).inner_text()
        meta_data = row.locator(f".{prefix}-meta").inner_text().split(" · ")
        probability = row.locator(f".{prefix}-idx b").inner_text().replace("%", "")
        fixture_id= row.get_attribute("href").split("fixture_id=")[1].split("&")[0]

        match = {
            "home": home_team,
            "away": away_team,
            "time": meta_data[0],
            "country": meta_data[1],
            "league": meta_data[2],
            "probability": int(probability),
            "fixture_id": int(fixture_id),
        }
        matches.append(match)

    return matches
def print_matches(matches):
    for match in matches:
         print(f"{match['home']} | {match['away']} | {match['time']} | {match['country']} | {match['league']} | {match['probability'] } |{match['fixture_id'] } ")
with sync_playwright() as p:
    browser=p.chromium.launch()
    page=browser.new_page()
    page.goto("https://www.vitibet.com/index.php?clanek=quicktips&sekce=fotbal&lang=en")
    print(page.title())
    print("---OVER 2.5 GOALS---")
    print_matches(scrape_box(page,"t5o"))

    print("---UNDER 2.5 GOALS---")
    print_matches(scrape_box(page,"t5u"))
    
    browser.close()
