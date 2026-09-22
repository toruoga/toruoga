"""Shared helpers for the historical-recognition corpus pipeline."""
import hashlib
import re
import time
import urllib.request
import urllib.robotparser as robotparser
from pathlib import Path
from urllib.parse import urlparse

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]


def load_config(path: str | Path = None) -> dict:
    path = Path(path) if path else REPO_ROOT / "config.yaml"
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def data_path(cfg: dict, key: str, *parts: str) -> Path:
    p = REPO_ROOT / cfg["paths"][key]
    for part in parts:
        p = p / part
    p.parent.mkdir(parents=True, exist_ok=True) if p.suffix else p.mkdir(parents=True, exist_ok=True)
    return p


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()


def normalized_title(title: str) -> str:
    t = title.lower().strip()
    t = re.sub(r"[^a-z0-9\s]", "", t)
    t = re.sub(r"\s+", " ", t)
    return t


def deterministic_filename(url: str) -> str:
    """Deterministic, collision-resistant filename derived from a URL."""
    parsed = urlparse(url)
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", parsed.path).strip("_") or "index"
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    return f"{slug[:80]}_{digest}"


def is_allowed_by_robots(url: str, user_agent: str, timeout: int = 10) -> bool:
    """Best-effort robots.txt check. Fails closed (returns False) only on a
    definitive Disallow; network errors fetching robots.txt do NOT block the
    crawl (treated as robots.txt absent), matching common crawler practice,
    but every fetch still goes through rate limiting in 02_download_pages.py.
    """
    parsed = urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    try:
        # RobotFileParser.read() calls urlopen() with no timeout, which can
        # hang indefinitely against a flaky host (observed against
        # mfa.gov.cn/pa.go.kr); fetch with an explicit timeout instead.
        with urllib.request.urlopen(robots_url, timeout=timeout) as resp:
            lines = resp.read().decode("utf-8", errors="ignore").splitlines()
        rp.parse(lines)
    except Exception:
        return True
    try:
        return rp.can_fetch(user_agent, url)
    except Exception:
        return True


def polite_sleep(seconds: float):
    time.sleep(seconds)


KNOWN_INSTITUTIONS = {
    "japan.kantei.go.jp": ("Prime Minister's Office of Japan (Kantei)", "japan"),
    "www.kantei.go.jp": ("Prime Minister's Office of Japan (Kantei)", "japan"),
    "www.mofa.go.jp": ("Ministry of Foreign Affairs of Japan", "japan"),
    "eng.president.go.kr": ("Office of the President, Republic of Korea", "korea"),
    "en.president.go.kr": ("Office of the President, Republic of Korea", "korea"),
    "english.president.go.kr": ("Office of the President, Republic of Korea", "korea"),
    "english1.president.go.kr": ("Office of the President, Republic of Korea", "korea"),
    "www.president.go.kr": ("Office of the President, Republic of Korea", "korea"),
    "www.mofa.go.kr": ("Ministry of Foreign Affairs, Republic of Korea", "korea"),
    # National Archives of Korea's official web-archiving service (WARP-equivalent):
    # eng.president.go.kr / english1.president.go.kr were retired when the
    # presidential administration changed (2022, 2025) and are DNS-dead; their
    # content is preserved verbatim here under /<ordinal>th/<original-host>/<path>.
    "webarchives.pa.go.kr": ("Office of the President, Republic of Korea (via National Archives of Korea web archive)", "korea"),
    "english.www.gov.cn": ("State Council of the People's Republic of China", "china"),
    "www.gov.cn": ("State Council of the People's Republic of China", "china"),
    "www.mfa.gov.cn": ("Ministry of Foreign Affairs of the People's Republic of China", "china"),
    "www.fmprc.gov.cn": ("Ministry of Foreign Affairs of the People's Republic of China", "china"),
}


def institution_for_url(url: str):
    netloc = urlparse(url).netloc
    return KNOWN_INSTITUTIONS.get(netloc, (None, None))
