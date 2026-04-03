#!/usr/bin/env python3
"""
Croatian Loto 7/35 Scraper & Frequency Analyzer
Scrapes all historical draws from lotostatistika.com.hr (2018-2026)
and performs comprehensive statistical analysis.
"""

import re
import time
import json
from collections import Counter
from itertools import combinations
from urllib.request import Request, urlopen
from html.parser import HTMLParser


class LotoParser(HTMLParser):
    """Parse draw results from lotostatistika.com.hr HTML."""

    def __init__(self):
        super().__init__()
        self.draws = []
        self.in_table = False
        self.in_row = False
        self.in_cell = False
        self.current_row = []
        self.cell_text = ""

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.in_table = True
        elif tag == "tr" and self.in_table:
            self.in_row = True
            self.current_row = []
        elif tag == "td" and self.in_row:
            self.in_cell = True
            self.cell_text = ""

    def handle_endtag(self, tag):
        if tag == "td" and self.in_cell:
            self.in_cell = False
            self.current_row.append(self.cell_text.strip())
        elif tag == "tr" and self.in_row:
            self.in_row = False
            if self.current_row:
                self.draws.append(self.current_row)
        elif tag == "table":
            self.in_table = False

    def handle_data(self, data):
        if self.in_cell:
            self.cell_text += data


def fetch_year(year):
    """Fetch all draws for a given year."""
    url = f"https://lotostatistika.com.hr/Loto-7-hr/loto-7-35-rezultati-{year}.aspx"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "hr-HR,hr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Referer": "https://lotostatistika.com.hr/",
    }

    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="replace")
        return html
    except Exception as e:
        print(f"  Error fetching {year}: {e}")
        return None


def parse_draws_from_html(html):
    """Extract draw results from HTML. Returns list of (date, [numbers], bonus)."""
    results = []

    # Try regex approach - look for patterns of 7 numbers
    # The site typically shows: Kolo | Date | N1 | N2 | N3 | N4 | N5 | N6 | N7 | Bonus

    # First try: find all table rows with numbers
    row_pattern = re.compile(
        r'<tr[^>]*>.*?</tr>', re.DOTALL
    )

    # Look for sequences of 7+ numbers in table cells
    cell_pattern = re.compile(r'<td[^>]*>(.*?)</td>', re.DOTALL)

    rows = row_pattern.findall(html)
    for row in rows:
        cells = cell_pattern.findall(row)
        # Clean cell contents
        cells = [re.sub(r'<[^>]+>', '', c).strip() for c in cells]

        # Try to find rows with enough numeric cells (date + 7 numbers + bonus)
        numbers_in_row = []
        date_str = ""

        for cell in cells:
            # Check if it looks like a date
            if re.match(r'\d{1,2}\.\d{1,2}\.\d{4}', cell):
                date_str = cell
            # Check if it's a number 1-39
            elif re.match(r'^\d{1,2}$', cell):
                num = int(cell)
                if 1 <= num <= 39:
                    numbers_in_row.append(num)

        if len(numbers_in_row) >= 7 and date_str:
            main_numbers = sorted(numbers_in_row[:7])
            bonus = numbers_in_row[7] if len(numbers_in_row) > 7 else None
            results.append((date_str, main_numbers, bonus))

    return results


def analyze(all_draws):
    """Perform comprehensive frequency analysis."""
    print(f"\n{'='*60}")
    print(f"COMPREHENSIVE LOTO 7/35 ANALYSIS")
    print(f"Total draws analyzed: {len(all_draws)}")
    if all_draws:
        print(f"Period: {all_draws[-1][0]} to {all_draws[0][0]}")
    print(f"{'='*60}")

    # Flatten all numbers
    all_numbers = []
    for _, nums, _ in all_draws:
        all_numbers.extend(nums)

    freq = Counter(all_numbers)

    # 1. Full frequency table
    print(f"\n--- FREQUENCY TABLE (all {len(all_draws)} draws) ---")
    print(f"{'Num':>4} {'Count':>6} {'%':>7}  Bar")
    print("-" * 55)
    avg = len(all_numbers) / 35 if all_numbers else 0
    for num in range(1, 36):
        count = freq.get(num, 0)
        pct = (count / len(all_draws) * 100) if all_draws else 0
        bar_len = int(count / max(freq.values()) * 30) if freq else 0
        marker = " <<< HOT" if count > avg * 1.05 else (" <<< COLD" if count < avg * 0.95 else "")
        print(f"{num:>4} {count:>6} {pct:>6.1f}%  {'#' * bar_len}{marker}")

    # 2. Top 10 most frequent
    print(f"\n--- TOP 10 MOST FREQUENT ---")
    for rank, (num, count) in enumerate(freq.most_common(10), 1):
        pct = count / len(all_draws) * 100
        print(f"  #{rank}: Number {num:>2} - drawn {count} times ({pct:.1f}%)")

    # 3. Bottom 10 least frequent
    print(f"\n--- TOP 10 LEAST FREQUENT ---")
    for rank, (num, count) in enumerate(freq.most_common()[-10:], 1):
        pct = count / len(all_draws) * 100
        print(f"  #{rank}: Number {num:>2} - drawn {count} times ({pct:.1f}%)")

    # 4. Overdue analysis (last 30 draws)
    print(f"\n--- OVERDUE ANALYSIS (draws since last appearance) ---")
    overdue = {}
    for num in range(1, 36):
        for i, (_, nums, _) in enumerate(all_draws):
            if num in nums:
                overdue[num] = i
                break
        else:
            overdue[num] = len(all_draws)

    for num, ago in sorted(overdue.items(), key=lambda x: -x[1]):
        if ago >= 5:
            print(f"  Number {num:>2}: last seen {ago} draws ago")

    # 5. Pair analysis
    print(f"\n--- TOP 20 MOST COMMON PAIRS ---")
    pair_counter = Counter()
    for _, nums, _ in all_draws:
        for pair in combinations(sorted(nums), 2):
            pair_counter[pair] += 1

    for rank, (pair, count) in enumerate(pair_counter.most_common(20), 1):
        print(f"  #{rank}: ({pair[0]:>2}, {pair[1]:>2}) - appeared together {count} times")

    # 6. Odd/Even analysis
    print(f"\n--- ODD/EVEN DISTRIBUTION ---")
    odd_even_dist = Counter()
    for _, nums, _ in all_draws:
        odd_count = sum(1 for n in nums if n % 2 == 1)
        even_count = 7 - odd_count
        odd_even_dist[f"{odd_count}odd/{even_count}even"] += 1

    for combo, count in sorted(odd_even_dist.items(), key=lambda x: -x[1]):
        pct = count / len(all_draws) * 100
        print(f"  {combo}: {count} times ({pct:.1f}%)")

    # 7. Sum range analysis
    print(f"\n--- SUM RANGE ANALYSIS ---")
    sums = [sum(nums) for _, nums, _ in all_draws]
    if sums:
        print(f"  Average sum: {sum(sums)/len(sums):.1f}")
        print(f"  Min sum: {min(sums)}")
        print(f"  Max sum: {max(sums)}")
        # Find the range covering 70% of draws
        sorted_sums = sorted(sums)
        n = len(sorted_sums)
        p15 = sorted_sums[int(n * 0.15)]
        p85 = sorted_sums[int(n * 0.85)]
        print(f"  70% of draws fall between sum {p15} and {p85}")

    # 8. Repeat analysis
    print(f"\n--- REPEAT FROM PREVIOUS DRAW ---")
    repeat_dist = Counter()
    for i in range(1, len(all_draws)):
        prev = set(all_draws[i][1])
        curr = set(all_draws[i-1][1])
        repeats = len(prev & curr)
        repeat_dist[repeats] += 1

    for reps in sorted(repeat_dist.keys()):
        count = repeat_dist[reps]
        pct = count / (len(all_draws) - 1) * 100
        print(f"  {reps} repeats: {count} times ({pct:.1f}%)")

    # 9. COMPOSITE SCORING
    print(f"\n{'='*60}")
    print(f"COMPOSITE SCORE RANKING")
    print(f"(frequency x2 + overdue_bonus + pair_strength)")
    print(f"{'='*60}")

    max_freq = max(freq.values()) if freq else 1
    scores = {}
    for num in range(1, 36):
        f_score = (freq.get(num, 0) / max_freq) * 20
        o_bonus = min(overdue.get(num, 0) / 10, 3)  # small overdue bonus, capped
        # Pair strength: how many top pairs include this number
        p_score = sum(1 for (a, b), _ in pair_counter.most_common(50) if num in (a, b)) / 5
        scores[num] = f_score + o_bonus + p_score

    ranked = sorted(scores.items(), key=lambda x: -x[1])
    for num, score in ranked:
        f = freq.get(num, 0)
        o = overdue.get(num, 0)
        print(f"  Number {num:>2}: score {score:>5.1f}  (freq={f}, overdue={o} draws)")

    # 10. RECOMMENDED COMBINATIONS
    print(f"\n{'='*60}")
    print(f"RECOMMENDED COMBINATIONS")
    print(f"{'='*60}")

    top7 = [num for num, _ in ranked[:10]]

    # Pick 1: Top 7 by composite score
    pick1 = sorted(top7[:7])
    print(f"\n  Pick 1 (Top Composite): {pick1}  sum={sum(pick1)}")

    # Pick 2: Top frequent + overdue blend
    freq_top = [n for n, _ in freq.most_common(5)]
    overdue_top = [n for n, _ in sorted(overdue.items(), key=lambda x: -x[1]) if n not in freq_top][:2]
    pick2 = sorted(freq_top + overdue_top)
    print(f"  Pick 2 (Freq + Overdue): {pick2}  sum={sum(pick2)}")

    # Pick 3: Best pairs combined
    best_pair_nums = Counter()
    for (a, b), count in pair_counter.most_common(30):
        best_pair_nums[a] += count
        best_pair_nums[b] += count
    pick3 = sorted([n for n, _ in best_pair_nums.most_common(7)])
    print(f"  Pick 3 (Best Pairs):    {pick3}  sum={sum(pick3)}")

    # Save raw data for further analysis
    data = {
        "total_draws": len(all_draws),
        "frequency": dict(freq),
        "overdue": overdue,
        "top_pairs": [(list(p), c) for p, c in pair_counter.most_common(50)],
        "scores": {str(k): round(v, 2) for k, v in ranked},
    }
    with open("loto_analysis.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"\n  Raw data saved to loto_analysis.json")


def main():
    all_draws = []

    # Scrape years 2018-2026 (Loto 7/35 started Oct 2018)
    for year in range(2026, 2017, -1):
        print(f"Fetching {year}...")
        html = fetch_year(year)
        if html:
            draws = parse_draws_from_html(html)
            print(f"  Found {len(draws)} draws")
            all_draws.extend(draws)
        else:
            print(f"  Failed to fetch {year}")
        time.sleep(1)  # Be polite

    if not all_draws:
        print("\nNo data could be scraped. The site may require a browser.")
        print("Trying alternative: saving a Selenium-based scraper...")
        write_selenium_scraper()
        return

    print(f"\nTotal draws collected: {len(all_draws)}")
    analyze(all_draws)


def write_selenium_scraper():
    """Write a Selenium-based fallback scraper if urllib fails."""
    code = '''#!/usr/bin/env python3
"""
Selenium-based scraper for lotostatistika.com.hr
Run: pip install selenium webdriver-manager && python loto_selenium_scraper.py
"""
import time, json, re
from collections import Counter
from itertools import combinations

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    print("Install dependencies: pip install selenium webdriver-manager")
    exit(1)

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--lang=hr")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

all_draws = []
for year in range(2026, 2017, -1):
    url = f"https://lotostatistika.com.hr/Loto-7-hr/loto-7-35-rezultati-{year}.aspx"
    print(f"Fetching {year}...")
    driver.get(url)
    time.sleep(3)

    html = driver.page_source
    # Parse tables for draw data
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', html, re.DOTALL)
    for row in rows:
        cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL)
        cells = [re.sub(r'<[^>]+>', '', c).strip() for c in cells]

        numbers = []
        date_str = ""
        for cell in cells:
            if re.match(r'\\d{1,2}\\.\\d{1,2}\\.\\d{4}', cell):
                date_str = cell
            elif re.match(r'^\\d{1,2}$', cell):
                num = int(cell)
                if 1 <= num <= 39:
                    numbers.append(num)

        if len(numbers) >= 7 and date_str:
            all_draws.append((date_str, sorted(numbers[:7]), numbers[7] if len(numbers) > 7 else None))

    print(f"  Total so far: {len(all_draws)} draws")

driver.quit()

print(f"\\nTotal draws: {len(all_draws)}")

# Save raw results
with open("loto_raw_draws.json", "w") as f:
    json.dump([(d, n, b) for d, n, b in all_draws], f, indent=2)
print("Saved to loto_raw_draws.json")

# Quick frequency analysis
freq = Counter()
for _, nums, _ in all_draws:
    freq.update(nums)

print("\\nTop 15 most frequent:")
for num, count in freq.most_common(15):
    print(f"  Number {num:>2}: {count} times ({count/len(all_draws)*100:.1f}%)")

print("\\nTop 10 least frequent:")
for num, count in freq.most_common()[-10:]:
    print(f"  Number {num:>2}: {count} times ({count/len(all_draws)*100:.1f}%)")
'''
    with open("loto_selenium_scraper.py", "w") as f:
        f.write(code)
    print("Saved Selenium scraper to: loto_selenium_scraper.py")
    print("Run: pip install selenium webdriver-manager && python loto_selenium_scraper.py")


if __name__ == "__main__":
    main()
