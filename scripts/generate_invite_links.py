#!/usr/bin/env python3
"""
Generate encrypted invitation links (AES-GCM, no JSON lookup needed).

Usage examples:
  python scripts/generate_invite_links.py --base-url "https://ruvindharani.live/" --secret "YOUR_32_CHAR_SECRET_KEY_HERE__1234" --name "John Doe"
  python scripts/generate_invite_links.py --base-url "https://ruvindharani.live/" --secret "YOUR_32_CHAR_SECRET_KEY_HERE__1234" --input guests.txt

Input file format:
  One guest name per line.
"""

from __future__ import annotations

import argparse
import base64
import secrets
import sys
from pathlib import Path
from urllib.parse import urlencode, urlsplit, urlunsplit

from Crypto.Cipher import AES


def b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("utf-8").rstrip("=")


def encrypt_name(name: str, secret_key: str) -> str:
    key = secret_key.encode("utf-8")
    if len(key) != 32:
        raise ValueError("Secret key must be exactly 32 bytes/chars.")

    iv = secrets.token_bytes(12)  # 96-bit nonce for GCM
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    ciphertext, tag = cipher.encrypt_and_digest(name.encode("utf-8"))
    return f"{b64url_encode(iv)}.{b64url_encode(ciphertext + tag)}"


def build_link(base_url: str, token: str) -> str:
    parts = urlsplit(base_url)
    query = urlencode({"guest": token})
    return urlunsplit((parts.scheme, parts.netloc, parts.path, query, parts.fragment))


def read_names(path: Path) -> list[str]:
    names: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        name = raw.strip()
        if name:
            names.append(name)
    return names


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate encrypted invite links.")
    parser.add_argument("--base-url", required=True, help="Site URL, e.g. https://ruvindharani.live/")
    parser.add_argument("--secret", required=True, help="Exact 32-char secret key.")
    parser.add_argument("--name", help="Single guest name.")
    parser.add_argument("--input", help="Path to text file with one guest name per line.")
    args = parser.parse_args()

    if not args.name and not args.input:
        parser.error("Provide either --name or --input.")

    if args.name and args.input:
        parser.error("Use only one of --name or --input.")

    try:
        if args.name:
            token = encrypt_name(args.name, args.secret)
            print(build_link(args.base_url, token))
            return 0

        names = read_names(Path(args.input))
        if not names:
            print("No names found in input file.", file=sys.stderr)
            return 1

        for name in names:
            token = encrypt_name(name, args.secret)
            print(f"{name}\t{build_link(args.base_url, token)}")
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
