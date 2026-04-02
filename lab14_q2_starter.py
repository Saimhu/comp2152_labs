import urllib.request
import urllib.error

REQUIRED_HEADERS = [
    "X-Frame-Options",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "Strict-Transport-Security"
]

HEADER_EXPLANATIONS = {
    "X-Frame-Options": "Protects against clickjacking attacks.",
    "Content-Security-Policy": "Helps prevent XSS and content injection attacks.",
    "X-Content-Type-Options": "Prevents MIME-type sniffing.",
    "Strict-Transport-Security": "Forces browsers to use HTTPS."
}


def check_headers(url):
    """
    Check one URL for each required security header.
    Return a dictionary of header -> present/missing.
    """
    results = {}

    try:
        with urllib.request.urlopen(url) as response:
            headers = dict(response.headers)

            for header in REQUIRED_HEADERS:
                results[header] = header in headers

    except urllib.error.HTTPError as e:
        headers = dict(e.headers)
        for header in REQUIRED_HEADERS:
            results[header] = header in headers

    except urllib.error.URLError:
        for header in REQUIRED_HEADERS:
            results[header] = False

    return results


def generate_report(url, results):
    """
    Print a readable report for the checked URL.
    """
    print(f"\nSecurity Header Report for: {url}")

    for header, is_present in results.items():
        if is_present:
            print(f"✓ {header} is present")
        else:
            print(f"✗ {header} is missing - {HEADER_EXPLANATIONS[header]}")


if __name__ == "__main__":
    urls = [
        "https://example.com",
        "https://jsonplaceholder.typicode.com"
    ]

    for url in urls:
        result = check_headers(url)
        generate_report(url, result)