# BloomScrapy

Web Crawler with Bloom Filter for Duplicate URL Filtering

## Overview

This project is a simple web crawler implemented in Python. It uses a custom Bloom filter to track visited URLs, ensuring that each URL is only visited once. This helps avoid duplicate requests, saving bandwidth and improving efficiency.

### Features

- **Bloom Filter for Duplicate URL Detection**: Efficiently tracks visited URLs with minimal memory usage.
- **Domain-Specific Crawling**: Restricts crawling to the same domain as the seed URL.
- **Politeness Delay**: Adds a delay between requests to avoid overwhelming servers.

## Requirements

- Python 3.7+
- `requests` library for HTTP requests
- `beautifulsoup4` library for parsing HTML

### Installing Dependencies

Install required packages by running:

```bash
pip install -r requirements.txt
```

## Setup

1. Clone the repository.
2. Ensure the dependencies are installed using the command above.
3. Set up your environment by creating a virtual environment (optional but recommended).

## Usage

1. Modify the `seed_url` variable in `crawler.py` to specify your starting URL.
2. Run the crawler using:

   ```bash
   python crawler.py
   ```

The crawler will begin at the `seed_url` and will display URLs as they are visited.

## Project Structure

- **`bloom_filter.py`**: Contains the custom Bloom filter implementation.
- **`crawler.py`**: The main crawler script that initializes the Bloom filter and manages crawling.

## How It Works

1. **Bloom Filter**: This filter uses multiple hash functions to map each visited URL to a bit array, enabling efficient duplicate detection.
2. **Web Crawling**: The crawler starts at a seed URL, fetches links within the same domain, and visits each unique link.

## Example

Here’s how to run the crawler on a sample URL:

```python
seed_url = "https://example.com"
```

Run:

```bash
python crawler.py
```

The crawler will display each URL it visits and skip any duplicates.

## Contributing

Feel free to contribute by submitting a pull request or opening an issue for bug fixes, feature requests, or improvements.

## License

This project is licensed under the MIT License.
