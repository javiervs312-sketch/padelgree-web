#!/usr/bin/env python3
"""Builds the English Blog Hub (/en/blog/) and 5 high-intent English M&A/investment articles."""

from pathlib import Path
from _templates import build_head, build_header, build_footer, cta_box

ROOT = Path(__file__).resolve().parent

EN_ARTICLES = [
    {
        "slug": "padel-club-valuation-ebitda-multiples",
        "es_slug": "valoracion-clubes-padel-multiplos-ebitda",
        "tag": "M&A & VALUATION",
        "read": "6 min read",
        "title": "Padel Club Valuation: EBITDA Multiples, Lease Tenure & Asset Floors (2026)",
        "desc": "How institutional buyers and chains value operating padel clubs across Europe and the UK: 3.5x–5.5x normalized EBITDA multiples, lease term impact, and panoramic court replacement floors.",
        "keywords": "padel club valuation, padel club EBITDA multiple, how much is a padel club worth, sell padel club valuation",
        "intro": "As European padel shifts from founder-led facilities into multi-club institutional portfolios, valuations are governed strictly by normalized cash flow, warehouse lease duration, and asset replacement floors.",
        "body": """
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">1. Standard EBITDA Valuation Multiples</h2>
      <p>Operating indoor padel businesses in leased warehouses typically trade on a multiple of trailing twelve-month (LTM) normalized EBITDA:</p>
      <div class="overflow-x-auto my-6 border border-slate-200 rounded-xl">
        <table class="w-full text-xs text-left">
          <thead class="bg-slate-50 border-b border-slate-200 text-slate-950 font-heading font-bold">
            <tr><th class="p-3.5">Club Profile</th><th class="p-3.5">EBITDA Multiple</th><th class="p-3.5">Key Buyer Conditions</th></tr>
          </thead>
          <tbody class="divide-y divide-slate-100">
            <tr><td class="p-3.5 font-bold text-slate-950">Mid-size Club (4–6 courts)</td><td class="p-3.5 font-mono font-bold">3.0x – 3.8x EBITDA</td><td class="p-3.5">4–7y lease left, standard turf, higher owner-operator dependency.</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Consolidated Indoor (7–10 courts)</td><td class="p-3.5 font-mono font-bold">3.8x – 4.8x EBITDA</td><td class="p-3.5">8–15y lease tenure, &gt;70% peak utilization, clear POS/SaaS logs.</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Flagship Venue (&gt;10 courts / Freehold)</td><td class="p-3.5 font-mono font-bold">5.0x – 5.8x+ EBITDA</td><td class="p-3.5">10m+ eaves height, HVAC, proprietary F&amp;B margin, major metro hub.</td></tr>
          </tbody>
        </table>
      </div>
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">2. Normalized EBITDA Adjustments in Due Diligence</h2>
      <ul class="list-disc pl-5 space-y-2 text-slate-700">
        <li><strong>Market Manager Replacement Salary</strong>: Adjusting founder wages up or down to reflect hiring a full-time general club manager.</li>
        <li><strong>Deferred Capex Deductions</strong>: Discounting aged artificial turf (&gt;4 years old) or non-LED metal-halide lighting upgrades.</li>
        <li><strong>Remaining Lease Bottleneck</strong>: If under 6 years remain on the warehouse lease without extension options, buyers drop multiples steeply; Padelgree pre-negotiates 10–15y landlord extensions prior to close.</li>
      </ul>
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">3. Tangible Asset Replacement Floor</h2>
      <p>Even if a club is under-monetized operationally, installed 12mm panoramic courts carry €20,000–€32,000 per court replacement value plus €150k–€300k in amortized concrete floor slab, changing rooms, power upgrades, and active municipal sports permits.</p>""",
        "cta_title": "Test your club's estimated M&A valuation range",
        "cta_desc": "Use our interactive calculator or send basic figures to Javier in confidence for direct operator feedback.",
    },
    {
        "slug": "how-to-sell-a-padel-club-off-market",
        "es_slug": "por-que-vender-club-padel-off-market-confidencial",
        "tag": "CONFIDENTIAL EXITS",
        "read": "5 min read",
        "title": "Why You Must Sell Your Padel Club 100% Off-Market (And How Blind Teasers Protect Value)",
        "desc": "Publicly listing a padel club triggers player churn, coach defection, and lowball bids. Learn how Padelgree runs blind teaser M&A processes under strict NDA.",
        "keywords": "how to sell a padel club, sell padel club privately, off-market padel deal, padel business broker confidentiality",
        "intro": "A padel club is not an empty retail shell—its enterprise value lives in recurring weekly player communities, coaching staff loyalty, and local league momentum.",
        "body": """
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">What Breaks Value When a Club Leaks Publicly</h2>
      <ul class="list-disc pl-5 space-y-2 text-slate-700">
        <li><strong>Member &amp; Academy Churn</strong>: Players assume maintenance or coaching continuity will suffer and switch annual packs to nearby rivals within weeks.</li>
        <li><strong>Coach &amp; Staff Poaching</strong>: Top instructors are the club's moat; uncertainty triggers immediate approaches from competing clubs.</li>
        <li><strong>Predatory Pricing Signals</strong>: If a listing lingers publicly for months, buyers assume distress and discount offers by 25%–40%.</li>
      </ul>
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">The Padelgree Double Opt-In Protocol</h2>
      <p>1) Blind operational teaser with zero brand or street disclosure; 2) Pre-vetting buyer proof of funds and expansion fit; 3) Mutual NDA and seller green-light before revealing club identity.</p>""",
        "cta_title": "Explore a quiet sale or equity partner privately",
        "cta_desc": "Zero public listings, zero upfront retainers—success-fee only upon closing.",
    },
    {
        "slug": "padel-warehouse-requirements-ceiling-height-lease",
        "es_slug": "requisitos-tecnicos-naves-industriales-padel",
        "tag": "WAREHOUSES & REAL ESTATE",
        "read": "7 min read",
        "title": "Padel Warehouse Requirements: Ceiling Height, Column Grid, Slab Specs & Lease Terms",
        "desc": "Complete technical checklist for indoor padel venues: 8.5m–11m clear height, 11x21m bay spacing, 1,500 kg/sqm slab capacity, HVAC, and 10–15y commercial lease structures.",
        "keywords": "padel warehouse ceiling height, indoor padel warehouse requirements, lease warehouse padel UK Europe, padel court dimensions building",
        "intro": "Finding a compliant industrial building is the single tightest bottleneck for expanding European and UK padel operators. Here are the non-negotiable structural standards.",
        "body": """
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">Structural Specifications Matrix</h2>
      <div class="overflow-x-auto my-6 border border-slate-200 rounded-xl">
        <table class="w-full text-xs text-left">
          <thead class="bg-slate-50 border-b border-slate-200 text-slate-950 font-heading font-bold">
            <tr><th class="p-3.5">Architectural Spec</th><th class="p-3.5">Minimum Commercial</th><th class="p-3.5">Optimal / Competition Grade</th></tr>
          </thead>
          <tbody class="divide-y divide-slate-100">
            <tr><td class="p-3.5 font-bold text-slate-950">Clear Height Under Beam/Lighting</td><td class="p-3.5 font-mono font-bold">8.5m (28 ft)</td><td class="p-3.5 font-mono font-bold">10.0m – 12.0m (33–39 ft)</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Column-Free Module per Court</td><td class="p-3.5 font-mono">11m x 21m</td><td class="p-3.5 font-mono">12m x 22m+ (incl. out-of-court run)</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Total Floor Area (6–10 Courts)</td><td class="p-3.5 font-mono">1,800 sqm (19k sqft)</td><td class="p-3.5 font-mono">2,500 – 4,500 sqm (27k–48k sqft)</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Concrete Slab &amp; Flatness</td><td class="p-3.5" colspan="2">Reinforced &ge;150mm concrete, DIN 18202 tolerance (&lt;3mm/3m), load &ge;1,500 kg/sqm.</td></tr>
          </tbody>
        </table>
      </div>
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">Essential Lease Clauses for Landlords &amp; Tenants</h2>
      <ul class="list-disc pl-5 space-y-2 text-slate-700">
        <li><strong>Planning / Change-of-Use Break Clause</strong>: Conditional on obtaining municipal Class E / D2 / sports assembly consent.</li>
        <li><strong>4–8 Month Rent-Free Fit-Out</strong>: Covers architectural permitting, concrete slab leveling, HVAC, changing facilities, and court rigging.</li>
        <li><strong>10–15 Year Tenure + Assignment Clause</strong>: Essential to amortize €500k+ Capex and ensure smooth future M&amp;A share transfers.</li>
      </ul>""",
        "cta_title": "Check how many courts fit in your warehouse",
        "cta_desc": "Run our Warehouse Court Calculator or share building specs with Javier privately.",
    },
    {
        "slug": "cost-to-build-indoor-padel-club-unit-economics",
        "es_slug": "unit-economics-inversion-club-padel-8-pistas",
        "tag": "CAPEX & UNIT ECONOMICS",
        "read": "8 min read",
        "title": "Cost to Build an Indoor Padel Club: 8-Court Capex, Opex, EBITDA & IRR Breakdown",
        "desc": "Granular financial model of building and operating an 8-court indoor padel facility: €480k–€755k Capex, ancillary revenue mix, 33%–38% EBITDA margins, and 22–32 month payback.",
        "keywords": "cost to build indoor padel club, padel club unit economics, padel club ROI payback, how much does it cost to open a padel club",
        "intro": "Budgeting only the €20k–€25k court hardware is the classic rookie mistake. Court steel and glass account for barely 30%–35% of turnkey indoor club build-out costs.",
        "body": """
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">8-Court Indoor Turnkey Capex Breakdown (Leased Shell)</h2>
      <div class="overflow-x-auto my-6 border border-slate-200 rounded-xl">
        <table class="w-full text-xs text-left">
          <thead class="bg-slate-50 border-b border-slate-200 text-slate-950 font-heading font-bold">
            <tr><th class="p-3.5">Capex Line Item</th><th class="p-3.5">Estimated Cost Range (€)</th></tr>
          </thead>
          <tbody class="divide-y divide-slate-100">
            <tr><td class="p-3.5 font-bold text-slate-950">8 Panoramic Courts (12mm glass + texturized turf + LED)</td><td class="p-3.5 font-mono font-bold">€175,000 – €225,000</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Concrete Slab Leveling &amp; Civil Works</td><td class="p-3.5 font-mono font-bold">€45,000 – €85,000</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Locker Rooms, Showers, Lounge &amp; F&amp;B Fit-Out</td><td class="p-3.5 font-mono font-bold">€90,000 – €160,000</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">HVAC / HVLS Fans, Electrical Power &amp; Access Control</td><td class="p-3.5 font-mono font-bold">€80,000 – €145,000</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Engineering, Acoustic Compliance &amp; Contingency</td><td class="p-3.5 font-mono font-bold">€40,000 – €70,000</td></tr>
            <tr class="bg-slate-50 font-bold"><td class="p-3.5 text-slate-950">Total Turnkey Capex (8 Courts)</td><td class="p-3.5 font-mono text-slate-950">€480,000 – €755,000</td></tr>
          </tbody>
        </table>
      </div>
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">Operating Profitability (Year 2+ Stabilized)</h2>
      <p>With 60%–70% blended utilization (peak 90%+, off-peak 30%–45% backed by coaching academies and corporate leagues) plus F&amp;B lounge and pro-shop sales, stabilized revenue reaches <strong>€525k–€815k</strong> in Spain and <strong>€900k–€1.5M+</strong> in UK/Northern Europe, delivering <strong>33%–38% EBITDA margins</strong> and <strong>24%–36% IRR</strong>.</p>""",
        "cta_title": "Looking for turnkey opportunities or operating clubs to buy?",
        "cta_desc": "Speak with Javier to review off-market deal flow or capital deployment mandates.",
    },
    {
        "slug": "buy-padel-club-europe-uk-due-diligence",
        "es_slug": "due-diligence-compra-club-padel-checklist",
        "tag": "BUY-SIDE DUE DILIGENCE",
        "read": "7 min read",
        "title": "Buying a Padel Club in Europe or the UK: Technical, Legal & Financial Due Diligence Checklist",
        "desc": "Essential M&A verification steps before buying any padel club: reconciling booking software logs with bank settlements, lease assignment clauses, planning consents, and turf inspection.",
        "keywords": "buy padel club due diligence, audit padel club before buying, padel M&A checklist Europe UK",
        "intro": "Before signing an asset purchase or share deal for a padel business, buyers must audit four non-negotiable pillars to eliminate hidden legal and Capex liabilities.",
        "body": """
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">The 4 Pillars of Padel Club Due Diligence</h2>
      <ul class="list-disc pl-5 space-y-2 text-slate-700">
        <li><strong>1. Financial Reconciliation</strong>: Cross-verify Playtomic/Matchi/Syltek booking exports directly against bank merchant statements (Stripe/POS) to confirm actual cash utilization vs complimentary staff slots and test seasonal dips in summer months.</li>
        <li><strong>2. Urban Zoning &amp; Acoustic Permits</strong>: Verify active municipal sports operating license and noise compliance certificates near any residential boundaries.</li>
        <li><strong>3. Landlord Assignment &amp; Remaining Tenure</strong>: Confirm written landlord consent, rent indexation caps, and at least 8–10+ remaining years.</li>
        <li><strong>4. Hardware &amp; Turf Inspection</strong>: Measure LED lux levels (&gt;400 lux uniform), check glass thickness (10mm vs 12mm), concrete slab cracks, and turf filament wear (replacing turf costs €3.5k–€4.5k/court).</li>
      </ul>""",
        "cta_title": "Engage Padelgree on buy-side vetting & deal origination",
        "cta_desc": "Access non-public clubs already screened for lease tenure, ceiling height, and clean accounts.",
    },
]


def main():
    # 1. Build each EN article
    for art in EN_ARTICLES:
        slug = f"en/blog/{art['slug']}/"
        canon = f"https://padelgree.com/{slug}"
        es_canon = f"https://padelgree.com/blog/{art['es_slug']}/"

        graph = [
            {
                "@type": "BlogPosting",
                "mainEntityOfPage": {"@type": "WebPage", "@id": canon},
                "headline": art["title"],
                "description": art["desc"],
                "author": {"@type": "Person", "name": "Javier Villoria", "url": "https://www.linkedin.com/in/javier-villoria-soleto-606737298/"},
                "publisher": {"@type": "Organization", "name": "Padelgree", "url": "https://padelgree.com"},
                "inLanguage": "en",
                "datePublished": "2026-11-27",
                "dateModified": "2026-11-27",
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://padelgree.com/en/"},
                    {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://padelgree.com/en/blog/"},
                    {"@type": "ListItem", "position": 3, "name": art["tag"], "item": canon},
                ],
            },
        ]

        head = build_head(
            lang="en",
            title=f"{art['title']} | Padelgree",
            description=art["desc"],
            canonical=canon,
            keywords=art["keywords"],
            og_type="article",
            hreflang_es=es_canon,
            hreflang_en=canon,
            schema_graph=graph,
        )
        header = build_header("en", f"/blog/{art['es_slug']}/")
        footer = build_footer("en")
        rel_cards = " ".join(
            f'<a href="/en/blog/{o["slug"]}/" class="px-4 py-2 rounded-xl border border-slate-200 hover:border-slate-950 bg-white text-xs font-bold text-slate-900 transition">{o["tag"]} →</a>'
            for o in EN_ARTICLES if o["slug"] != art["slug"]
        )

        html = f"""{head}
{header}
  <article class="max-w-3xl mx-auto px-4 sm:px-6 py-10 sm:py-14 flex-1">
    <nav class="flex items-center gap-2 text-xs text-slate-400 mb-6 font-mono">
      <a href="/en/" class="hover:text-slate-950 transition">Home</a><span>/</span>
      <a href="/en/blog/" class="hover:text-slate-950 transition">Blog</a><span>/</span>
      <span class="text-slate-900 font-bold truncate">{art["tag"]}</span>
    </nav>

    <div class="mb-8">
      <div class="flex items-center gap-3 text-xs text-slate-400 font-mono mb-3">
        <span class="font-bold text-slate-900 uppercase">{art["tag"]}</span><span>·</span>
        <span>By Javier Villoria</span><span>·</span>
        <span>{art["read"]}</span>
      </div>
      <h1 class="font-heading font-black text-3xl sm:text-4xl lg:text-5xl text-slate-950 tracking-tight leading-tight mb-4">
        {art["title"]}
      </h1>
      <p class="text-base sm:text-lg text-slate-600 font-normal leading-relaxed">{art["intro"]}</p>
    </div>

    <div class="prose max-w-none text-slate-800 text-sm sm:text-base leading-relaxed space-y-6">
      {art["body"]}
    </div>

    <div class="mt-10 pt-8 border-t border-slate-200">
      <h2 class="font-heading font-black text-lg text-slate-950 mb-3">Interactive Tools &amp; Related Briefs</h2>
      <div class="flex flex-wrap gap-2">
        <a href="/en/padel-club-valuation-calculator/" class="px-4 py-2 rounded-xl border border-slate-950 bg-slate-950 text-white text-xs font-bold transition">Club Valuation Calculator →</a>
        <a href="/en/padel-warehouse-court-calculator/" class="px-4 py-2 rounded-xl border border-slate-300 hover:border-slate-950 bg-white text-xs font-bold text-slate-900 transition">Warehouse Court Calculator →</a>
        {rel_cards}
      </div>
    </div>

{cta_box("en", art["cta_title"], art["cta_desc"], f"Hi Javier, reading {art['title']} on Padelgree EN.")}
  </article>
{footer}"""
        out = ROOT / "en" / "blog" / art["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")

    # 2. Build EN Blog Hub (/en/blog/index.html)
    hub_head = build_head(
        lang="en",
        title="Padel M&A, Valuation & Real Estate Research Blog | Padelgree",
        description="Institutional guides on padel club EBITDA valuation multiples, confidential off-market sales, indoor warehouse ceiling specs, unit economics, and buy-side due diligence.",
        canonical="https://padelgree.com/en/blog/",
        hreflang_es="https://padelgree.com/blog/",
        hreflang_en="https://padelgree.com/en/blog/",
        schema_graph=[{
            "@type": "Blog",
            "@id": "https://padelgree.com/en/blog/#blog",
            "name": "Padelgree B2B Research & M&A Briefs",
            "url": "https://padelgree.com/en/blog/",
            "inLanguage": "en",
            "publisher": {"@type": "Organization", "name": "Padelgree", "url": "https://padelgree.com"},
        }],
    )
    cards_html = "\n".join(
        f"""      <a href="/en/blog/{a['slug']}/" class="group block bg-white border border-slate-300 hover:border-slate-950 rounded-2xl p-6 sm:p-7 transition-all duration-200 hover:shadow-xl hover:-translate-y-0.5 flex flex-col justify-between cursor-pointer">
        <div>
          <div class="flex items-center justify-between text-xs text-slate-400 font-mono mb-3">
            <span class="font-bold text-slate-900 uppercase">{a['tag']}</span>
            <span>{a['read']}</span>
          </div>
          <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950 group-hover:text-black leading-snug mb-3">{a['title']}</h2>
          <p class="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal mb-6">{a['desc']}</p>
        </div>
        <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs font-heading font-bold text-slate-950 group-hover:underline">
          <span>Read technical guide</span>
          <span class="w-7 h-7 rounded-full bg-slate-950 text-white flex items-center justify-center group-hover:scale-105 transition">→</span>
        </div>
      </a>"""
        for a in EN_ARTICLES
    )
    hub_html = f"""{hub_head}
{build_header("en", "/blog/")}
  <main class="w-full max-w-6xl mx-auto px-4 sm:px-6 py-10 sm:py-14 flex-1">
    <nav class="flex items-center gap-2 text-xs text-slate-400 mb-6 font-mono">
      <a href="/en/" class="hover:text-slate-950 transition">Home</a><span>/</span>
      <span class="text-slate-900 font-bold">Research &amp; Blog</span>
    </nav>

    <div class="max-w-3xl mb-12">
      <span class="text-xs font-mono font-bold tracking-widest text-slate-400 uppercase block mb-2">MARKET INTELLIGENCE &amp; M&amp;A</span>
      <h1 class="font-heading font-black text-3xl sm:text-4xl lg:text-5xl text-slate-950 tracking-tight leading-tight mb-4">
        Padel Club Economics, Valuation &amp; Off-Market Deals
      </h1>
      <p class="text-sm sm:text-base text-slate-600 font-normal leading-relaxed">
        Technical research covering European &amp; UK padel M&amp;A multiples, industrial warehouse engineering specs, turnkey unit economics, and strict off-market deal protocols by Javier Villoria.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8">
{cards_html}
    </div>

{cta_box("en", "Exploring a confidential padel deal?", "Speak directly with Javier Villoria regarding club exits, buy-side expansion mandates, or warehouse leases.", "Hi Javier, reaching out from the Padelgree EN Research Blog.")}
  </main>
{build_footer("en")}"""
    hub_out = ROOT / "en" / "blog" / "index.html"
    hub_out.parent.mkdir(parents=True, exist_ok=True)
    hub_out.write_text(hub_html, encoding="utf-8")
    print(f"Built EN Blog Hub + {len(EN_ARTICLES)} EN articles")


if __name__ == "__main__":
    main()
