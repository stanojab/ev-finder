# EV Finder

A daily Python script that looks for value bets on football Over/Under 2.5 goals markets.

It scrapes the top Over/Under 2.5 tips from vitibet.com, fetches bet365 odds from API-Football,
calculates the expected value (EV = probability × odds − 1), and flags a bet when EV ≥ 3%.
Results are printed, logged to a CSV file, and shown on an HTML page.

This is a learning project for practising Python and Git/GitHub.
