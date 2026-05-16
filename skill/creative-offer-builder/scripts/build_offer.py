#!/usr/bin/env python3
import csv
import sys


FIELDS = [
    "business_name",
    "offer_name",
    "buyer_type",
    "problem",
    "starter_offer",
    "core_offer",
    "premium_offer",
    "deliverables",
    "timeline",
    "price_range",
    "client_inputs",
    "cta",
    "upsell",
    "next_action",
]


def value(row, *keys):
    for key in keys:
        if row.get(key):
            return row[key].strip()
    return ""


def infer_offer(row):
    business = value(row, "business_name", "name") or "Client"
    category = value(row, "category", "buyer_type") or "local business"
    need = value(row, "design_need", "problem", "opportunity") or "clearer visual presence"
    suggested = value(row, "suggested_offer", "offer")

    lower = f"{need} {suggested}".lower()
    if "website" in lower or "landing" in lower:
        offer_name = "Starter Website Build"
        starter = "One-page landing page with contact CTA"
        core = "Starter website with sections, inquiry form, and mobile polish"
        premium = "Website plus domain setup, intake flow, SEO basics, and 30-day support"
        deliverables = "Responsive page, CTA section, contact/intake form, launch checklist"
        timeline = "3-7 business days"
        price = "Starting at $200-$1,500"
        upsell = "Monthly maintenance"
    elif "flyer" in lower or "promo" in lower or "event" in lower:
        offer_name = "Promo Graphics Pack"
        starter = "One flyer design"
        core = "Flyer plus Instagram post and story versions"
        premium = "Full promo pack with captions, resize set, and event banner"
        deliverables = "Flyer, social versions, export files"
        timeline = "1-3 business days"
        price = "Starting at $50-$300"
        upsell = "Monthly content pack"
    elif "logo" in lower or "brand" in lower:
        offer_name = "Logo + Mini Brand Kit"
        starter = "Logo cleanup or simple concept"
        core = "Logo, color palette, type direction, and social avatar"
        premium = "Logo suite, mini brand guide, and launch graphics"
        deliverables = "Logo files, color palette, brand notes, social assets"
        timeline = "3-5 business days"
        price = "Starting at $150-$1,000"
        upsell = "Website or social template kit"
    else:
        offer_name = "Creative Refresh Package"
        starter = "One priority design fix"
        core = "Visual refresh for the main customer-facing assets"
        premium = "Brand cleanup plus campaign assets and handoff guide"
        deliverables = "Design assets, export files, basic usage notes"
        timeline = "2-5 business days"
        price = "Starting at $100-$750"
        upsell = "Brand audit snapshot"

    return {
        "business_name": business,
        "offer_name": offer_name,
        "buyer_type": category,
        "problem": need,
        "starter_offer": starter,
        "core_offer": core,
        "premium_offer": premium,
        "deliverables": deliverables,
        "timeline": timeline,
        "price_range": price,
        "client_inputs": "Brand name, deadline, wording, colors/style, references, files",
        "cta": "Reply with the package you want and I will send the invoice and intake.",
        "upsell": upsell,
        "next_action": value(row, "next_action") or "Send offer",
    }


def main():
    if len(sys.argv) != 3:
        print("Usage: build_offer.py input.csv output.csv", file=sys.stderr)
        return 2

    with open(sys.argv[1], newline="", encoding="utf-8") as src:
        rows = list(csv.DictReader(src))

    with open(sys.argv[2], "w", newline="", encoding="utf-8") as dst:
        writer = csv.DictWriter(dst, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(infer_offer(row))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
