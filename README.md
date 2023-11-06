# Badminton Statistics Crawling Tool

This tool is designed to scrape badminton statistics from the [bwfbadminton.com](https://bwfbadminton.com/calendar/) website. It uses the Scrapy framework to crawl the website and retrieve information about badminton tournament results.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Output](#output)
- [Contributing](#contributing)

## Requirements

Before running the crawling tool, make sure you have the following requirements installed on your system:

- Python 3.x
- Scrapy
- Requests

You also need a valid ScrapeOps API key to fetch user agents for web scraping. You can obtain an API key by signing up at [ScrapeOps](https://www.scrapeops.io/).

## Installation

1. Clone the project repository to your local machine:

```shell
git clone https://github.com/HoVanThanh1504/CrawlBadmintonData.git
```

2. Change to the project directory:

```shell
cd CrawlBadmintonData
```

3. Install the required Python packages using `pip`:

```shell
pip install -r requirements.txt
```

## Usage

To use the badminton statistics crawling tool, follow these steps:

1. Make sure you have installed the required packages and have a valid ScrapeOps API key.

2. Edit the ScrapeOps API key in the `crawler.py` file:

```python
SCRAPEOPS_API_KEY = 'your-api-key-here'
```

3. Run the Scrapy spider by executing the following command from the project directory:

```shell
scrapy crawl craw_badminton_stat -o [filename].json
```

The spider will start crawling the specified URLs on the bwfbadminton.com website and retrieve badminton statistics.

## Configuration

- The `start_urls` list in the `craw_badminton_stat.py` file contains the URLs that the spider will start crawling. You can modify this list to add or remove URLs based on your specific requirements.

- You can customize the fields you want to scrape by updating the XPath expressions in the `parse_info` and `parse_other_info` functions in the `craw_badminton_stat.py` file.

## Output

The crawling tool will output the scraped data as a JSON file. You can find the output file in the project directory with a name like `tournament_dataset.json`. The JSON file will contain the extracted badminton statistics, including match scores, player details, and head-to-head statistics.

## Contributing

If you want to contribute to this project or have suggestions for improvements, feel free to fork the repository, make your changes, and submit a pull request.
