# InnerG Intel Creative Offer Builder

An installable Codex skill for graphic designers, brand designers, website designers, and creative freelancers who need to turn lead notes or audit findings into clear packages people can buy.

This is Skill 04 in the InnerG Intel creative sales toolkit. It follows Creative Client Finder, Creative Outreach Writer, and Brand Audit Snapshot by converting demand into a priced offer.

## What It Builds

- Starter, core, and premium package tiers
- Scope-controlled deliverables
- Suggested price ranges
- Client intake requirements
- CTAs for invoices, deposits, and next steps
- Upsell and maintenance paths
- CSV output for offer tracking

## Use In Codex

Paste this into Codex:

```text
Use Creative Offer Builder.

Turn this lead or audit into a sellable offer.
Create starter, core, and premium tiers with deliverables, timeline, price range, client inputs needed, CTA, and upsell path.

Lead/audit notes:
[paste notes here]
```

More examples:

```text
Use Creative Offer Builder on these restaurant leads. Turn each one into a starter, core, and premium offer.
```

```text
Use Creative Offer Builder to create a $200 starter website offer, a $500 core offer, and a monthly maintenance upsell.
```

## Install

```bash
bash scripts/install.sh
```

Or manually:

```bash
mkdir -p ~/.codex/skills
cp -R skill/creative-offer-builder ~/.codex/skills/
```

## Example Prompt

```text
Use Creative Offer Builder on these restaurant leads. Turn each one into a starter, core, and premium offer.
```

## CSV Helper

```bash
python3 skill/creative-offer-builder/scripts/build_offer.py examples/leads.csv /tmp/offers.csv
```

Expected input can include:

```text
business_name,category,design_need,suggested_offer,evidence,next_action
```

## InnerG Intel Ecosystem

1. Creative Client Finder
2. Creative Outreach Writer
3. Brand Audit Snapshot
4. Creative Offer Builder
5. Creative Follow-Up Tracker
