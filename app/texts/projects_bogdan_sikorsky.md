# WebRiderAsync

WebRiderAsync is an asynchronous utility designed for very simple and highly tunable handling of large volumes of web requests. 

It leverages Python's `aiohttp` for asynchronous HTTP requests, making it capable of achieving high performance by processing multiple requests in parallel. This utility could be useful both for working with APIs and web scraping.

### Key Features:

- **Simple Setup**: Unlike complex frameworks like Scrapy, WebRiderAsync requires no in-depth knowledge of asynchronous programming or framework-specific structures. All settings are handled via class initialization, offering flexibility with minimal overhead.

- **Asynchronous by Design**: Designed to process multiple requests in parallel, WebRiderAsync leverages Python’s `asyncio` and `aiohttp` to maximize performance without requiring users to write asynchronous code themselves.

- **User-Friendly**: There’s no need to understand `asyncio` or `aiohttp`. Simply pass a list of URLs to the `request()` function, and WebRiderAsync will handle the rest.

### Why WebRiderAsync?

Compared to frameworks like Scrapy, WebRiderAsync is straightforward and ideal for users who want the power of asynchronous requests without the need for a deep dive into project structures or complex configurations. It’s perfect for both beginners and advanced users who need rapid, customizable scraping or API requests.

### Installation

You can install the latest version of WebRiderAsync using pip:

```shell
pip install webrider-async
```

Check out the [PyPI page](https://pypi.org/project/webrider-async/) for the latest version and updates.

### Usage Examples:

Find detailed [examples](https://github.com/bogdan-sikorsky/webrider_async/tree/main/examples) and usage scenarios in the [GitHub repository](https://github.com/bogdan-sikorsky/webrider_async).
