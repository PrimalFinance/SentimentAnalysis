# SentimentAnalysis

## Asset Data

---

#### [Folders]

- Storage: Holds csv files with open, high, low, close, volume data.

#### [Python Files]

- asset_data.py: File used to interface with data.

## Database

---

#### [Folders]

- AnnualData: Holds .db files of companies with their balance sheet, income statement, and cash flow statement.

#### [Python Files]

- data_base_manager.py: Interfaces with the .db files. Can add, update, and delete data from databases.

## Graphing

---

#### [Python Files]

- graphs.py: Supports graphing of multiple data points.

## Models

---

#### [Python Files]

- llm.py: Interface with ChatGPT to query chats.
- sentiment_analysis.py: Interface with a local NLP model to get analysis scores on text.

## Responses

---

Description: Holds responses from ChatGPT for further analysis.

## Scrapers

---

#### [Python Files]

- earnings_report_scraper.py: Get an earnings report through a pdf.
- fiscal_dates_scraper.py: Get the fiscal dates of a company.
- fmp_scraper.py: Using "financialmodelingprep.com" query financial statements.
- googlenews.py: Query google news for articles around specific topics, or get the latest trending stories.
- price_ranges.py: Get the price high, low, and average price of a stock within a specified period of time.
- reddit.py: Get posts from specified subreddits, or search reddit for specific terms.
- twitter.py: Get posts from certain accounts, or posts around certain topics.
