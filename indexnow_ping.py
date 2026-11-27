#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de notificación automática a IndexNow para padelgree.com.
Notifica al instante a Bing, DuckDuckGo, Copilot, ChatGPT Search y Yandex
cualquier URL nueva o actualizada del sitemap.xml.

Uso: python padelgree-web/indexnow_ping.py [--dry-run]
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

HOST = "padelgree.com"
KEY = "e7f4b9c21d8a4f6c9a3e5b2d7c1f8a42"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITEMAP_FILE = os.path.join(BASE_DIR, "sitemap.xml")


def extraer_urls_sitemap(sitemap_path: str, max_urls: int = 1000) -> list[str]:
    if not os.path.exists(sitemap_path):
        return [f"https://{HOST}/", f"https://{HOST}/en/", f"https://{HOST}/blog/"]
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()
    urls = re.findall(r"<loc>(https://padelgree\.com/[^<]*)</loc>", content)
    # Deduplicate preserving order
    seen = set()
    unique = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            unique.append(u)
    return unique[:max_urls]


def notificar_indexnow(dry_run: bool = False):
    urls = extraer_urls_sitemap(SITEMAP_FILE)
    print(f"Preparando ping a IndexNow con {len(urls)} URLs de {HOST}...")

    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }

    if dry_run:
        print("Modo --dry-run activado. No se envían peticiones HTTP.")
        print(f"  Key Location: {KEY_LOCATION}")
        print(f"  Primeras 5 URLs: {urls[:5]}")
        return

    json_data = json.dumps(payload).encode("utf-8")

    for endpoint in ENDPOINTS:
        try:
            req = urllib.request.Request(
                endpoint,
                data=json_data,
                headers={"Content-Type": "application/json; charset=utf-8"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                print(f"[OK] Notificado {endpoint} -> HTTP {resp.status}")
        except urllib.error.HTTPError as e:
            if e.code in (200, 202):
                print(f"[OK] Notificado {endpoint} -> HTTP {e.code}")
            else:
                print(f"[WARN] {endpoint} -> HTTP {e.code}: {e.reason}")
        except Exception as ex:
            print(f"[WARN] Error conectando con {endpoint}: {ex}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Notificación a IndexNow para padelgree.com")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    notificar_indexnow(dry_run=args.dry_run)
