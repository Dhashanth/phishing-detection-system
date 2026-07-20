PROJECT_NAME = "Phishing Detection System"


import re
from datetime import datetime
from urllib.parse import urlparse

BRAND_WORDS = [
    "paypal",
    "microsoft",
    "google",
    "apple",
    "facebook",
    "instagram",
    "amazon",
    "bank",
    "office365",
    "github"
]
SUSPICIOUS_TLDS = {"zip", "mov", "top", "xyz", "click", "country"}

def analyze(payload):
    url = payload.get("url", "")
    parsed = urlparse(url if "://" in url else "http://" + url)
    host = parsed.netloc.lower()
    path = parsed.path.lower()
    features = {
        "host_length": len(host),
        "has_ip_host": bool(re.match(r"^\d+\.\d+\.\d+\.\d+$", host)),
        "brand_impersonation": any(word in host and not host.endswith(word + ".com") for word in BRAND_WORDS),
        "many_subdomains": host.count(".") >= 3,
        "suspicious_tld": host.split(".")[-1] in SUSPICIOUS_TLDS,
        "credential_path": any(word in (host + path) for word in [
    "login",
    "verify",
    "secure",
    "account",
    "update",
    "password",
    "signin",
    "confirm"
]),
        "contains_at": "@" in url,
        "long_url": len(url) > 90
    }
    weights = {
        "has_ip_host": 22, "brand_impersonation": 24, "many_subdomains": 12,
        "suspicious_tld": 18, "credential_path": 10, "contains_at": 12, "long_url": 8
    }
    score = sum(weights[key] for key, value in features.items() if value and key in weights)
    verdict = "phishing" if score >= 45 else "suspicious" if score >= 20 else "benign"
    return {
        "url": url,
        "features": features,
        "verdict": verdict,
        "score": min(100, score),
        "generated_at": datetime.utcnow().isoformat() + "Z"
    }

