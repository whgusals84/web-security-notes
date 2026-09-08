"""A narrow HTTP-origin model for study; not a browser URL parser."""

from urllib.parse import urlsplit


def origin(url: str) -> tuple[str, str, int]:
    """Return scheme, ASCII hostname, effective port for unambiguous HTTP(S) URLs.

    Restrict syntax to avoid suggesting equivalence with the WHATWG URL algorithm.
    IDNs, IPv6, opaque origins, backslashes, and control characters are out of scope.
    """
    if not url.isascii() or any(ord(char) <= 32 for char in url) or "\\" in url:
        raise ValueError("use an ASCII URL without whitespace or backslashes")
    parsed = urlsplit(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("an absolute HTTP(S) URL is required")
    if parsed.username is not None or parsed.password is not None or ":" in parsed.hostname:
        raise ValueError("userinfo and IPv6 are outside this model")
    if parsed.netloc.endswith(":"):
        raise ValueError("empty explicit port")
    port = parsed.port if parsed.port is not None else (443 if parsed.scheme == "https" else 80)
    if port == 0:
        raise ValueError("port zero is outside this model")
    return parsed.scheme, parsed.hostname, port


def same_origin(first: str, second: str) -> bool:
    """Path, query, and fragment do not participate in this HTTP origin tuple."""
    return origin(first) == origin(second)


if __name__ == "__main__":
    print(same_origin("https://lab.invalid/a", "https://LAB.invalid:443/b"))
    print(same_origin("https://lab.invalid/a", "http://lab.invalid/a"))
