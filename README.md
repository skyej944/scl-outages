  # Seattle City Light Outages (SCL)
  This repo tracks Seattle City Light outage events over time by recording
  the raw JSON response from the outage map endpoint in Git history.

  ## Data source
  - https://utilisocial.io/datacapable/v2/p/scl/map/events

  ## How it works
  - A GitHub Actions workflow runs every 15 minutes.
  - It fetches the JSON, writes `outages.json`, and commits changes.
  - The commit history is the time series.

  ## Files
  - `outages.json` — latest fetched data
  - `scripts/fetch_outages.py` — fetch + normalize script
  - `.github/workflows/scrape.yml` — scheduled scrape
  - `.github/workflows/keepalive.yml` — monthly keepalive commit

  - Times in the data are epoch milliseconds.
