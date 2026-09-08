# Browser boundaries

## Origins versus paths

For ordinary HTTP(S) URLs, compare scheme, hostname, and effective port. Path and query changes
do not create a new origin. `https://lab.invalid/a` and `https://LAB.invalid:443/b` therefore match;
switching to HTTP or port 8443 does not. `python origins.py` prints `True`, then `False`.

The helper intentionally accepts only a narrow URL subset. It does not model opaque origins,
file URLs, IDNs, IPv6, browser URL recovery, redirects, or site computation. Do not use it as an
SSRF filter or authorization boundary. All domain names are synthetic and no URL is fetched.

## Separate the controls

| Control | Main question | What it does not establish |
| --- | --- | --- |
| Same-origin policy | May a script read this other origin's response? | That a request cannot be sent |
| CORS | Which other origins may read an opted-in response? | User authentication or permission to mutate data |
| CSRF token | Does this state-changing request carry session-bound intent evidence? | That the page has no XSS |
| Output encoding | Is untrusted text kept out of executable markup? | Access authorization |
| HttpOnly cookie | Can JavaScript read this cookie value? | That injected script cannot make same-origin requests |
| SameSite cookie | When is a cookie attached across sites? | A complete request-intent policy |

## Exercise

A form can submit without JavaScript reading the response. Explain why a read restriction alone
does not protect a state-changing handler. Then distinguish a site from an origin: sibling hosts
can be same-site while still being different origins. The helper tests origins only.

Reference: [MDN same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy).
