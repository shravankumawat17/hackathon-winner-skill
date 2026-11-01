#!/usr/bin/env python3
"""LLM cost, free-tier headroom, and demo-day burst check.

  cost_estimate.py --reqs-per-day 500 --in-tokens 1500 --out-tokens 400 \
      --price-in 0.15 --price-out 0.60 --days 3
  cost_estimate.py --provider groq --burst-users 30 --reqs-per-user 6 --window-min 10
  cost_estimate.py --list

Prices are USD per 1M tokens (look them up on the official pricing page first).
Free-tier numbers come from assets/data/free_tiers.json: a dated SNAPSHOT. Verify before use.
"""
import argparse, json, os
from datetime import date, datetime

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "data", "free_tiers.json")
STALE_DAYS = 30


def load():
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--list", action="store_true")
    p.add_argument("--provider")
    p.add_argument("--reqs-per-day", type=float, default=0)
    p.add_argument("--in-tokens", type=float, default=0)
    p.add_argument("--out-tokens", type=float, default=0)
    p.add_argument("--price-in", type=float, default=0.0, help="USD per 1M input tokens")
    p.add_argument("--price-out", type=float, default=0.0, help="USD per 1M output tokens")
    p.add_argument("--days", type=float, default=1)
    p.add_argument("--cache-hit", type=float, default=0.0, help="0-1 share of requests served from cache")
    p.add_argument("--burst-users", type=float, default=0)
    p.add_argument("--reqs-per-user", type=float, default=0)
    p.add_argument("--window-min", type=float, default=10)
    a = p.parse_args()
    d = load()
    snap = datetime.strptime(d["snapshot_date"], "%Y-%m-%d").date()
    age = (date.today() - snap).days
    print(f"[snapshot {d['snapshot_date']}, {age} days old] " + ("STALE: re-verify everything on official pages." if age > STALE_DAYS else "still verify limits on official pages before relying on them."))

    if a.list:
        for k, v in d["providers"].items():
            print(f"- {k}: RPM={v.get('rpm')} RPD={v.get('rpd')} confidence={v.get('confidence')} :: {v.get('notes')}")
        return

    paid_reqs = a.reqs_per_day * a.days * (1 - a.cache_hit)
    cost = paid_reqs * (a.in_tokens * a.price_in + a.out_tokens * a.price_out) / 1_000_000
    if a.reqs_per_day:
        print(f"Requests (after cache): {paid_reqs:,.0f} over {a.days:g} day(s)")
        print(f"Token volume: in {paid_reqs*a.in_tokens:,.0f} / out {paid_reqs*a.out_tokens:,.0f}")
        print(f"Estimated paid cost: ${cost:,.2f}  (cost per request ${cost/max(paid_reqs,1):.5f})")

    if a.provider:
        v = d["providers"].get(a.provider)
        if not v:
            print(f"unknown provider '{a.provider}'. use --list")
            return
        print(f"\nProvider {a.provider} (confidence {v.get('confidence')}): {v.get('notes')}")
        rpd, rpm = v.get("rpd"), v.get("rpm")
        if a.reqs_per_day and rpd:
            print(f"Daily headroom: {a.reqs_per_day*(1-a.cache_hit):,.0f} of {rpd:,} RPD -> " + ("OK" if a.reqs_per_day*(1-a.cache_hit) <= rpd else "EXCEEDS: cache, route to second provider, or replay mode"))
        if a.burst_users and a.reqs_per_user:
            need = a.burst_users * a.reqs_per_user / max(a.window_min, 1) * (1 - a.cache_hit)
            print(f"Burst: {need:.1f} req/min needed" + (f" vs {rpm} RPM limit -> " + ("OK" if need <= rpm else "EXCEEDS: queue + fallback chain + cached demo mode") if rpm else " (RPM not published: check console)"))
            total = a.burst_users * a.reqs_per_user * (1 - a.cache_hit)
            if rpd:
                print(f"Burst total {total:,.0f} requests vs {rpd:,} RPD -> " + ("OK" if total <= rpd else "EXCEEDS"))
        for s in v.get("sources", []):
            print(f"source: {s}")


if __name__ == "__main__":
    main()
