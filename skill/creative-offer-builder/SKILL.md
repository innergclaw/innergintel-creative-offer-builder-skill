---
name: creative-offer-builder
description: Use when packaging graphic design, branding, flyer, website, Canva, social media, or local-business creative services into clear sellable offers. Turns lead notes, audit findings, service ideas, client needs, budgets, and outreach context into tiered packages, scope, deliverables, pricing suggestions, CTA copy, proposal language, and upsell paths for designers and creative freelancers.
---

# Creative Offer Builder

Use this skill to turn a creative opportunity into an offer someone can understand and buy. Prioritize clarity, scope control, and practical next steps.

## Workflow

1. Identify the buyer type: local business owner, creator, event host, restaurant, salon, gym, boutique, nonprofit, startup, or existing client.
2. Identify the problem from the lead or audit: weak logo, outdated flyers, no website, inconsistent Instagram, missing booking CTA, unclear promo, poor menu design, or no launch assets.
3. Choose one offer structure:
   - **Starter**: low-friction entry offer for quick trust.
   - **Core**: main recommended package.
   - **Premium**: deeper package with more assets, revisions, speed, or recurring support.
4. Define scope tightly: deliverables, revision count, timeline, client inputs needed, and what is not included.
5. Write the CTA: simple payment/deposit step plus what happens after payment.
6. Add optional upsells only when they fit the client.

## Output Format

For chat output, use:

- Offer name
- Best-fit client
- Client problem
- Package tiers
- Included deliverables
- Timeline
- Client needs to provide
- Suggested price range
- CTA
- Upsell / maintenance path

For CSV output, use these columns:

```text
business_name,offer_name,buyer_type,problem,starter_offer,core_offer,premium_offer,deliverables,timeline,price_range,client_inputs,cta,upsell,next_action
```

## Pricing Guidance

Keep pricing grounded in scope and client urgency. Do not promise exact pricing unless the user provides it.

- Flyer / promo graphic: $50-$200
- Logo refresh: $150-$500
- Logo + basic brand kit: $300-$1,000
- Landing page / starter website: $200-$1,500
- Monthly content or maintenance: $50-$500/month
- Rush delivery: add 25%-50% when appropriate

Use “starting at” language when scope is unclear.

## Scope Rules

- Avoid vague deliverables like “branding package” without listing what is included.
- Keep revision limits explicit.
- Separate design work from printing, ad spend, copywriting, hosting, and domain fees unless included.
- If the buyer paid already, include an intake step before work begins.
- If the buyer is cold, lead with the quick win before the full package.

## Bundled Resources

- Use `scripts/build_offer.py` to turn lead CSV rows into offer rows.
- Read `references/offer-patterns.md` when choosing package structures, pricing anchors, and upsells.
