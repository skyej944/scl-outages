#!/usr/bin/env python3
  import json
  import urllib.request

  URL = "https://utilisocial.io/datacapable/v2/p/scl/map/events"

  def main():
      req = urllib.request.Request(
          URL,
          headers={
              "User-Agent": "scl-outages-scraper/1.0"
          }
      )
      with urllib.request.urlopen(req, timeout=30) as resp:
          if resp.status != 200:
              raise SystemExit(f"Unexpected status: {resp.status}")
          data = json.loads(resp.read().decode("utf-8"))

      data_sorted = sorted(data, key=lambda x: (x.get("id", 0), x.get("identifier", "")))
      with open("outages.json", "w", encoding="utf-8") as f:
          json.dump(data_sorted, f, indent=2, sort_keys=True)

  if __name__ == "__main__":
      main()
