#!/usr/bin/env python3
"""Builds the 8 ES/EN Transactional Money Pages, 12 Regional Market Hubs, and llm-knowledge.html."""

from pathlib import Path
from _templates import build_head, build_header, build_footer, cta_box

ROOT = Path(__file__).resolve().parent


def write_page(rel_path: str, html: str):
    out = ROOT / rel_path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


def render_money_or_market(cfg: dict):
    lang = cfg["lang"]
    slug = cfg["slug"]
    canon = f"https://padelgree.com/{slug}"
    alt = f"https://padelgree.com/{cfg['alt_slug']}" if cfg.get("alt_slug") else None
    es_url = canon if lang == "es" else alt
    en_url = canon if lang == "en" else alt

    crumbs_html = []
    schema_crumbs = []
    for idx, (lbl, href) in enumerate(cfg["crumbs"], 1):
        full = f"https://padelgree.com{href}"
        schema_crumbs.append({"@type": "ListItem", "position": idx, "name": lbl, "item": full})
        if idx < len(cfg["crumbs"]):
            crumbs_html.append(f'<a href="{href}" class="hover:text-slate-950 transition">{lbl}</a><span>/</span>')
        else:
            crumbs_html.append(f'<span class="text-slate-900 font-bold truncate">{lbl}</span>')

    faq_schema = [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in cfg["faqs"]
    ]

    graph = [
        {
            "@type": "WebPage",
            "@id": f"{canon}#webpage",
            "url": canon,
            "name": cfg["title"],
            "description": cfg["description"],
            "inLanguage": lang,
        },
        {
            "@type": "Service",
            "name": cfg["h1"],
            "serviceType": cfg["tag"],
            "provider": {"@type": "Organization", "name": "Padelgree", "url": "https://padelgree.com"},
            "description": cfg["description"],
        },
        {"@type": "FAQPage", "mainEntity": faq_schema},
        {"@type": "BreadcrumbList", "itemListElement": schema_crumbs},
    ]

    head = build_head(
        lang=lang,
        title=cfg["title"],
        description=cfg["description"],
        canonical=canon,
        keywords=cfg.get("keywords", ""),
        hreflang_es=es_url,
        hreflang_en=en_url,
        schema_graph=graph,
    )
    header = build_header(lang, f"/{cfg['alt_slug']}" if cfg.get("alt_slug") else None)
    footer = build_footer(lang)
    faqs_html = "\n".join(
        f'<div class="bg-white p-5 rounded-xl border border-slate-200">'
        f'<h3 class="font-heading font-bold text-slate-950 text-sm mb-1.5">{q}</h3>'
        f'<p class="text-xs text-slate-600 leading-relaxed">{a}</p></div>'
        for q, a in cfg["faqs"]
    )
    faq_heading = "Frequently Asked Questions" if lang == "en" else "Preguntas Frecuentes"
    related_links = " ".join(
        f'<a href="{u}" class="px-4 py-2 rounded-xl border border-slate-200 hover:border-slate-950 bg-white text-xs font-bold text-slate-900 transition">{t} →</a>'
        for t, u in cfg.get("related", [])
    )
    rel_heading = "Related Tools & Guides" if lang == "en" else "Calculadoras y Guías Relacionadas"

    body = f"""  <main class="max-w-4xl mx-auto px-4 sm:px-6 py-10 sm:py-14 flex-1">
    <nav class="flex items-center gap-2 text-xs text-slate-400 mb-6 font-mono">
      {"".join(crumbs_html)}
    </nav>

    <div class="mb-8">
      <span class="text-xs font-mono font-bold tracking-widest text-slate-400 uppercase block mb-2">{cfg["tag"]}</span>
      <h1 class="font-heading font-black text-3xl sm:text-4xl lg:text-5xl text-slate-950 tracking-tight leading-tight mb-4">
        {cfg["h1"]}
      </h1>
      <p class="text-base sm:text-lg text-slate-600 font-normal leading-relaxed">
        {cfg["intro"]}
      </p>
    </div>

    <div class="prose max-w-none text-slate-800 text-sm sm:text-base leading-relaxed space-y-6">
      {cfg["body_html"]}
    </div>

    <div class="mt-10 pt-8 border-t border-slate-200">
      <h2 class="font-heading font-black text-lg sm:text-xl text-slate-950 mb-4">{rel_heading}</h2>
      <div class="flex flex-wrap gap-2.5">{related_links}</div>
    </div>

    <div class="mt-10 pt-8 border-t border-slate-200">
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950 mb-5">{faq_heading}</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">{faqs_html}</div>
    </div>

{cta_box(lang, cfg["cta_title"], cfg["cta_desc"], cfg["wa_text"])}
  </main>
{footer}"""
    write_page(f"{slug}index.html", head + "\n" + header + "\n" + body)


MONEY_PAGES = [
    # 1. ES: Vender club de padel
    {
        "lang": "es",
        "slug": "vender-club-padel/",
        "alt_slug": "en/sell-padel-club/",
        "tag": "DESINVERSIÓN Y M&A CONFIDENCIAL",
        "title": "Vender Club de Pádel en Privado (100% Off-Market) | Padelgree",
        "description": "Cómo vender o traspasar tu club de pádel de forma 100% confidencial sin que se enteren tus socios ni monitores. Múltiplos de 3,5x a 5,5x EBITDA y compradores solventes verificados.",
        "keywords": "vender club de padel, traspaso club padel, cuanto vale mi club de padel, vender negocio padel confidencial",
        "h1": "Vender o Traspasar tu Club de Pádel sin Exposición Pública",
        "intro": "Publicar tu club en portales de traspasos provoca fuga de jugadores, inquietud en monitores y ofertas oportunistas a la baja. En Padelgree conectamos tu club directamente con cadenas e inversores solventes bajo acuerdo de confidencialidad (NDA).",
        "crumbs": [("Inicio", "/"), ("Vender Club de Pádel", "/vender-club-padel/")],
        "body_html": """
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">¿Cuánto pagan hoy los compradores por un club en marcha?</h2>
      <p>Las cadenas operadoras y fondos deportivos compran flujos de caja demostrables y horizontes contractuales sólidos en nave industrial:</p>
      <div class="overflow-x-auto my-6 border border-slate-200 rounded-xl">
        <table class="w-full text-xs text-left">
          <thead class="bg-slate-50 border-b border-slate-200 text-slate-950 font-heading font-bold">
            <tr><th class="p-3.5">Perfil del Club</th><th class="p-3.5">Múltiplo Habitual</th><th class="p-3.5">Requisitos del Comprador</th></tr>
          </thead>
          <tbody class="divide-y divide-slate-100">
            <tr><td class="p-3.5 font-bold text-slate-950">Club Indoor Mediano (4–6 pistas)</td><td class="p-3.5 font-mono font-bold">3,0x – 3,8x EBITDA</td><td class="p-3.5">Alquiler >5 años restantes, licencia deportiva vigente.</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Club Consolidado (7–10 pistas)</td><td class="p-3.5 font-mono font-bold">3,8x – 4,8x EBITDA</td><td class="p-3.5">Alquiler >8–10 años, ocupación punta >70%, contabilidad clara.</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Centro Referente (>10 pistas o en propiedad)</td><td class="p-3.5 font-mono font-bold">5,0x – 5,8x+ EBITDA</td><td class="p-3.5">Altura >10m, climatización, F&B propio y comunidad estable.</td></tr>
          </tbody>
        </table>
      </div>
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">Nuestro protocolo de 3 pasos para proteger tu marca</h2>
      <ul class="list-disc pl-5 space-y-2 text-slate-700">
        <li><strong>Paso 1 · Ficha Ciega (Blind Teaser)</strong>: Redactamos un dossier anónimo con número de pistas, facturación, EBITDA, zona aproximada y años de contrato. Sin nombre comercial ni dirección exacta.</li>
        <li><strong>Paso 2 · Filtrado de Solvencia</strong>: Solo presentamos la oportunidad a directores de expansión de cadenas o inversores con fondos acreditados en ese mercado.</li>
        <li><strong>Paso 3 · Doble Opt-In y NDA</strong>: Tú decides caso por caso qué comprador puede conocer el nombre de tu club y revisar los datos tras firmar NDA. Trabajamos 100% a éxito (sin cuotas fijas).</li>
      </ul>""",
        "related": [
            ("Calculadora Gratis: ¿Cuánto vale tu club?", "/calculadora-valoracion-club-padel/"),
            ("Guía Múltiplos EBITDA", "/blog/valoracion-clubes-padel-multiplos-ebitda/"),
            ("Guía Legal de Traspasos", "/blog/traspaso-club-padel-guia-legal-contratos-precio/"),
            ("Por qué vender Off-Market", "/blog/por-que-vender-club-padel-off-market-confidencial/"),
        ],
        "faqs": [
            ("¿Se enterarán mis socios o entrenadores si inicio el proceso?", "No. Jamás publicamos anuncios en portales ni en redes sociales. El acceso se limita estrictamente a compradores filtrados tras tu autorización expresa."),
            ("¿Qué comisión cobra Padelgree por vender mi club?", "Trabajamos mediante honorarios a éxito (success fee) pactados previamente por escrito. Cero costes iniciales de alta o mantenimiento."),
            ("¿Y si prefiero dar entrada a un socio sin vender el 100%?", "Gestionamos tanto ventas totales (100% traspaso o participaciones SL) como entradas de socios capitalistas o alianzas de co-branding."),
            ("¿Qué documentación necesito para empezar a tantear compradores?", "Solo número de pistas, facturación anual aproximada, EBITDA estimado, renta mensual de la nave y años restantes de alquiler."),
        ],
        "cta_title": "¿Valoras vender tu club o conocer qué ofrecería el mercado?",
        "cta_desc": "Escríbenos con total reserva para estimar la valoración realista y cruzarla en privado con compradores activos.",
        "wa_text": "Hola Javier, estoy valorando la venta/entrada de socio de mi club de pádel de forma confidencial.",
    },
    # 2. EN: Sell Padel Club
    {
        "lang": "en",
        "slug": "en/sell-padel-club/",
        "alt_slug": "vender-club-padel/",
        "tag": "CONFIDENTIAL M&A & EXITS",
        "title": "Sell Your Padel Club Off-Market (Zero Public Listings) | Padelgree",
        "description": "Sell or divest your indoor/outdoor padel club quietly without alerting members or rivals. 3.5x–5.5x EBITDA valuations and private introductions to backed European & UK operators.",
        "keywords": "sell padel club, padel club valuation, exit padel business, off-market padel M&A, sell padel centre UK Europe",
        "h1": "Sell Your Padel Club Confidentially, Off-Market",
        "intro": "Publicly advertising a padel club triggers immediate player defection, staff anxiety, and lowball offers. Padelgree introduces your business exclusively via blind teasers to vetted multi-club chains and capital partners under NDA.",
        "crumbs": [("Home", "/en/"), ("Sell Padel Club", "/en/sell-padel-club/")],
        "body_html": """
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">Current Valuation Benchmarks Across Europe &amp; UK</h2>
      <div class="overflow-x-auto my-6 border border-slate-200 rounded-xl">
        <table class="w-full text-xs text-left">
          <thead class="bg-slate-50 border-b border-slate-200 text-slate-950 font-heading font-bold">
            <tr><th class="p-3.5">Club Profile</th><th class="p-3.5">EBITDA Multiple Range</th><th class="p-3.5">Core Valuation Drivers</th></tr>
          </thead>
          <tbody class="divide-y divide-slate-100">
            <tr><td class="p-3.5 font-bold text-slate-950">Mid-size Indoor (4–6 courts)</td><td class="p-3.5 font-mono font-bold">3.0x – 3.8x EBITDA</td><td class="p-3.5">5+ years remaining lease, solid community, standard fit-out.</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Consolidated Hub (7–10 courts)</td><td class="p-3.5 font-mono font-bold">3.8x – 4.8x EBITDA</td><td class="p-3.5">8–15y lease security, &gt;70% peak occupancy, audited POS/SaaS logs.</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Flagship Venue (&gt;10 courts / Freehold)</td><td class="p-3.5 font-mono font-bold">5.0x – 5.8x+ EBITDA</td><td class="p-3.5">10m+ clear height, climate control, profitable hospitality, prime metro.</td></tr>
          </tbody>
        </table>
      </div>
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">Our 3-Step Strict Confidentiality Shield</h2>
      <ul class="list-disc pl-5 space-y-2 text-slate-700">
        <li><strong>Blind Teaser Preparation</strong>: Only anonymous operational KPIs, region, court count, and lease tenure are shared initially.</li>
        <li><strong>Buyer Capital Vetting</strong>: We approach pre-vetted European/UK chains, family offices, and backed operators actively expanding in your metro area.</li>
        <li><strong>Double Opt-In Under NDA</strong>: You approve every counterparty before identities, exact venue name, and financials are disclosed. Success-fee only.</li>
      </ul>""",
        "related": [
            ("Free Club Valuation Calculator", "/en/padel-club-valuation-calculator/"),
            ("EBITDA Valuation Guide", "/en/blog/padel-club-valuation-ebitda-multiples/"),
            ("Why Off-Market Sales Protect Value", "/en/blog/how-to-sell-a-padel-club-off-market/"),
        ],
        "faqs": [
            ("Will members or coaches find out we are exploring a sale?", "Never. Nothing is listed publicly on brokerage portals or social channels. Only qualified buyers signed under NDA see identifying details after your explicit approval."),
            ("What does Padelgree charge?", "Padelgree works on a pre-agreed success fee payable strictly at transaction closing. Zero upfront listing retainers."),
            ("Can we raise minority growth equity instead of selling 100%?", "Yes. We routinely match owners seeking capital for court expansions, roofs/canopies, or chain rebranding partnerships."),
            ("Which countries do you cover?", "Spain, UK, Italy, France, Germany, Nordics, Netherlands, and major US padel hubs."),
        ],
        "cta_title": "Request a confidential market valuation range for your club",
        "cta_desc": "Share basic KPIs in private with Javier Villoria to gauge real institutional buyer appetite.",
        "wa_text": "Hi Javier, I am considering selling my padel club or bringing in a strategic partner confidentially.",
    },
    # 3. ES: Comprar club de padel
    {
        "lang": "es",
        "slug": "comprar-club-padel/",
        "alt_slug": "en/buy-padel-club/",
        "tag": "MANDATOS DE COMPRA Y EXPANSIÓN",
        "title": "Comprar Club de Pádel en Marcha (Oportunidades Off-Market) | Padelgree",
        "description": "Mandatos privados de adquisición de clubes de pádel en España y Europa. Acceso fuera de mercado a clubes rentables de 6 a 16 pistas con licencia vigente y contratos largos.",
        "keywords": "comprar club de padel, clubes de padel en venta, inversion clubes padel, expandir cadena padel espana",
        "h1": "Comprar Clubes de Pádel Operativos Fuera de Mercado",
        "intro": "Construir de cero consume 14 a 22 meses en licencias y obra. Mediante mandatos privados de búsqueda, localizamos para cadenas e inversores clubes rentables que no aparecen en ningún portal público.",
        "crumbs": [("Inicio", "/"), ("Comprar Club de Pádel", "/comprar-club-padel/")],
        "body_html": """
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">Por qué las cadenas priorizan comprar clubes frente a construir de cero</h2>
      <ul class="list-disc pl-5 space-y-2 text-slate-700">
        <li><strong>Caja y Masa Social desde el Día 1</strong>: Adquieres una base de 1.500 a 3.500 jugadores habituales y escuelas operativas sin esperar maduración.</li>
        <li><strong>Cero Riesgo de Licencia Urbanística</strong>: La licencia de actividad deportiva y estudio acústico ya están concedidos y operando sin denuncias.</li>
        <li><strong>Negociación de Arrendamiento Previa</strong>: En Padelgree filtramos la salud financiera real y negociamos extensiones contractuales de 10–15 años con el propietario de la nave antes de cerrar.</li>
      </ul>
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">Criterios más solicitados en nuestros mandatos activos</h2>
      <div class="overflow-x-auto my-6 border border-slate-200 rounded-xl">
        <table class="w-full text-xs text-left">
          <thead class="bg-slate-50 border-b border-slate-200 text-slate-950 font-heading font-bold">
            <tr><th class="p-3.5">Parámetro</th><th class="p-3.5">Criterio Estándar M&A</th></tr>
          </thead>
          <tbody class="divide-y divide-slate-100">
            <tr><td class="p-3.5 font-bold text-slate-950">Número de Pistas</td><td class="p-3.5">Preferente 6 a 14 pistas indoor o cubiertas (mínimo 4 pistas en áreas prime).</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Altura de Nave</td><td class="p-3.5">Mínimo 8,5 metros bajo viga sin pilares invasivos (ideal 10+ m).</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Geografías Prioritarias</td><td class="p-3.5">Madrid, Barcelona, Valencia, Málaga, Sevilla, Bilbao y principales capitales europeas.</td></tr>
          </tbody>
        </table>
      </div>""",
        "related": [
            ("Checklist Due Diligence M&A", "/blog/due-diligence-compra-club-padel-checklist/"),
            ("Mapa de Expansión en Europa", "/blog/expansion-cadenas-padel-espana-europa/"),
            ("Calculadora de Valoración", "/calculadora-valoracion-club-padel/"),
        ],
        "faqs": [
            ("¿Cómo registro un mandato de compra para mi grupo u operador?", "Indícanos tus zonas objetivo, número mínimo de pistas, si buscas indoor o mixto y rango de presupuesto. Activamos la prospección privada directa."),
            ("¿Auditáis los ingresos declarados frente a las reservas reales?", "Sí, validamos coherencia entre histórico de reservas (Playtomic, Matchi, Syltek), extractos y estructura de costes antes de avanzar a LOI."),
        ],
        "cta_title": "Define tu mandato de búsqueda privada",
        "cta_desc": "Recibe fichas ciegas de clubes que cumplen exactamente tus parámetros técnicos y geográficos.",
        "wa_text": "Hola Javier, represento a un grupo/inversor y quiero definir un mandato para comprar clubes de pádel.",
    },
    # 4. EN: Buy Padel Club
    {
        "lang": "en",
        "slug": "en/buy-padel-club/",
        "alt_slug": "comprar-club-padel/",
        "tag": "BUY-SIDE ACQUISITION MANDATES",
        "title": "Buy an Operating Padel Club Off-Market (Europe & UK) | Padelgree",
        "description": "Acquire profitable cash-flowing padel clubs off-market. Dedicated buy-side search mandates for padel chains, multi-club operators, and private equity funds.",
        "keywords": "buy padel club, padel club for sale Europe UK, padel acquisition mandate, padel M&A buy-side broker",
        "h1": "Acquire Cash-Flowing Padel Clubs Off-Market",
        "intro": "Greenfield openings take 14–22 months of municipal permitting and build-out delays. Padelgree gives expanding operators and funds quiet access to profitable clubs not listed on any public brokerage.",
        "crumbs": [("Home", "/en/"), ("Buy Padel Club", "/en/buy-padel-club/")],
        "body_html": """
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">Why Leading Operators Acquire Existing Clubs</h2>
      <ul class="list-disc pl-5 space-y-2 text-slate-700">
        <li><strong>Day-One EBITDA &amp; Active Players</strong>: Acquire 1,500–3,500 regular weekly players and recurring academy cash flows immediately.</li>
        <li><strong>De-Risked Permitting</strong>: Active sports/D2/commercial zoning and acoustic approvals are already in place.</li>
        <li><strong>Lease Optimization Prior to Close</strong>: Padelgree pre-negotiates 10–15 year lease extensions with industrial landlords alongside the deal.</li>
      </ul>""",
        "related": [
            ("M&A Due Diligence Checklist", "/en/blog/buy-padel-club-europe-uk-due-diligence/"),
            ("EBITDA Valuation Calculator", "/en/padel-club-valuation-calculator/"),
            ("EBITDA Multiples Guide", "/en/blog/padel-club-valuation-ebitda-multiples/"),
        ],
        "faqs": [
            ("How do operators engage Padelgree for buy-side search?", "Share target metros, minimum court count, ceiling height floor, and equity budget. We confidentially approach non-listed owners matching your criteria."),
            ("Do you check bookings vs financial accounts?", "Yes. Prior to binding LOI we check software utilization logs against bank POS settlements and normalized Opex."),
        ],
        "cta_title": "Submit your confidential acquisition mandate",
        "cta_desc": "Tell Javier your target regions and deal criteria to receive curated blind profiles.",
        "wa_text": "Hi Javier, we are actively looking to acquire operating padel clubs and want to discuss criteria.",
    },
    # 5. ES: Naves para padel
    {
        "lang": "es",
        "slug": "naves-para-padel/",
        "alt_slug": "en/padel-warehouses/",
        "tag": "PROPIETARIOS DE INMUEBLES INDUSTRIALES",
        "title": "Alquiler de Naves Industriales para Pádel: Inquilinos Solventes | Padelgree",
        "description": "Rentabiliza tu nave industrial (>1.800 m² y >8,5 m altura) alquilándola a operadores y cadenas de pádel solventes con contratos a 10-15 años e inversión millonaria en el activo.",
        "keywords": "nave para padel, alquiler nave club padel, altura nave padel, propietario nave operador padel",
        "h1": "Alquila tu Nave Industrial a un Operador Solvente de Pádel",
        "intro": "Un club de pádel aporta contratos de obligado cumplimiento a 10–15 años, revaloriza tu inmueble con cientos de miles de euros en adecuación y genera flujos recurrentes estables. Conectamos tu nave en privado con cadenas activas.",
        "crumbs": [("Inicio", "/"), ("Naves para Pádel", "/naves-para-padel/")],
        "body_html": """
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">¿Cumple tu nave los requisitos técnicos para pádel indoor?</h2>
      <div class="overflow-x-auto my-6 border border-slate-200 rounded-xl">
        <table class="w-full text-xs text-left">
          <thead class="bg-slate-50 border-b border-slate-200 text-slate-950 font-heading font-bold">
            <tr><th class="p-3.5">Parámetro Estructural</th><th class="p-3.5">Estándar Comercial (Amateur)</th><th class="p-3.5">Grado Competición / Cadena Prime</th></tr>
          </thead>
          <tbody class="divide-y divide-slate-100">
            <tr><td class="p-3.5 font-bold text-slate-950">Altura Libre Bajo Viga</td><td class="p-3.5 font-mono font-bold">8,5 – 9,5 metros</td><td class="p-3.5 font-mono font-bold">10,0 – 12,0 metros</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Superficie Diáfana</td><td class="p-3.5 font-mono">1.800 – 2.500 m² (5–7 pistas)</td><td class="p-3.5 font-mono">2.600 – 5.000+ m² (8–14 pistas)</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Distancia entre Pilares</td><td class="p-3.5" colspan="2">Sin pilares dentro de cada módulo de 10x20 m + pasillos (retícula ≥ 11 x 21 m por pista).</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Uso Urbanístico</td><td class="p-3.5" colspan="2">Compatible con uso deportivo / terciario recreativo y dotación de parking.</td></tr>
          </tbody>
        </table>
      </div>""",
        "related": [
            ("Calculadora: ¿Cuántas pistas caben en tu nave?", "/calculadora-pistas-nave/"),
            ("Requisitos Técnicos de Naves", "/blog/requisitos-tecnicos-naves-industriales-padel/"),
            ("Guía de Contratos y Carencia", "/blog/contrato-alquiler-nave-industrial-club-padel/"),
        ],
        "faqs": [
            ("¿Qué renta pagan los operadores de pádel?", "Depende de ciudad, altura y estado de solera: en España suele situarse entre 3,50 € y 6,50 €/m² al mes, y en ciudades prime europeas alcanza de 7 € a 14 €/m²."),
            ("¿Tengo que publicar mi nave en portales inmobiliarios?", "No. Evaluamos planos y altura en privado y la presentamos directamente a cadenas que ya buscan exactamente esa zona."),
        ],
        "cta_title": "¿Tienes una nave diáfana con más de 8,5 metros de altura?",
        "cta_desc": "Envíanos ubicación aproximada, metros cuadrados y altura libre para comprobar encaje inmediato con nuestros operadores.",
        "wa_text": "Hola Javier, soy propietario/gestor de una nave o suelo industrial y busco operador solvente de pádel.",
    },
    # 6. EN: Padel Warehouses
    {
        "lang": "en",
        "slug": "en/padel-warehouses/",
        "alt_slug": "naves-para-padel/",
        "tag": "COMMERCIAL LANDLORDS & INDUSTRIAL OWNERS",
        "title": "Lease Your Warehouse to Backed Padel Operators (10–15y Leases) | Padelgree",
        "description": "Turn obsolete retail boxes or clear-span industrial warehouses (>8.5m height) into 10–15 year institutional padel leases. Direct introductions to funded European & UK chains.",
        "keywords": "padel warehouse lease, lease warehouse to padel club, padel ceiling height requirements UK Europe, industrial property padel tenant",
        "h1": "Lease Your Warehouse to Funded Padel Operators",
        "intro": "Padel chains sign 10–15 year institutional leases, invest €500k+ upgrading slabs and MEP infrastructure, and drive daily community footfall. Connect your property privately with vetted operators.",
        "crumbs": [("Home", "/en/"), ("Padel Warehouses", "/en/padel-warehouses/")],
        "body_html": """
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">Structural Specifications Sought by Chains</h2>
      <div class="overflow-x-auto my-6 border border-slate-200 rounded-xl">
        <table class="w-full text-xs text-left">
          <thead class="bg-slate-50 border-b border-slate-200 text-slate-950 font-heading font-bold">
            <tr><th class="p-3.5">Metric</th><th class="p-3.5">Commercial Standard</th><th class="p-3.5">Flagship Competition Grade</th></tr>
          </thead>
          <tbody class="divide-y divide-slate-100">
            <tr><td class="p-3.5 font-bold text-slate-950">Clear Eaves Height</td><td class="p-3.5 font-mono font-bold">8.5m – 9.5m (28–31 ft)</td><td class="p-3.5 font-mono font-bold">10.0m – 12.0m (33–39 ft)</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Floor Area</td><td class="p-3.5 font-mono">1,800 – 2,500 sqm (5–7 courts)</td><td class="p-3.5 font-mono">2,600 – 5,000+ sqm (8–14 courts)</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Column Grid</td><td class="p-3.5" colspan="2">Clear-span or &ge;11m x 21m bays per court with safe perimeter runoff.</td></tr>
          </tbody>
        </table>
      </div>""",
        "related": [
            ("Warehouse Court Fit-Out Calculator", "/en/padel-warehouse-court-calculator/"),
            ("Warehouse Ceiling & Lease Guide", "/en/blog/padel-warehouse-requirements-ceiling-height-lease/"),
        ],
        "faqs": [
            ("What lease terms do padel tenants sign?", "Standard leases run 10 to 15 years with a 4–8 month rent-free fit-out window subject to planning/change-of-use consent."),
            ("What properties work best besides industrial warehouses?", "Former supermarkets, DIY big-box stores, car dealerships, and suburban logistics units with parking."),
        ],
        "cta_title": "Submit your warehouse specs for private operator matching",
        "cta_desc": "Share approximate location, clear height, and floor plate size in private with Javier.",
        "wa_text": "Hi Javier, I represent a commercial warehouse landlord seeking a funded padel tenant.",
    },
    # 7. ES: Invertir en padel
    {
        "lang": "es",
        "slug": "invertir-en-padel/",
        "alt_slug": "en/invest-in-padel/",
        "tag": "CAPITAL PRIVADO Y PROYECTOS LLAVE EN MANO",
        "title": "Invertir en Clubes de Pádel: Rentabilidad, TIR y Proyectos Privados | Padelgree",
        "description": "Canaliza capital hacia clubes de pádel validados, coinversión en adquisiciones M&A y proyectos llave en mano en Europa con retornos TIR del 24% al 36% y payback en 24-32 meses.",
        "keywords": "invertir en padel, invertir en clubes de padel, rentabilidad club padel, socios inversores padel",
        "h1": "Invertir en Activos y Proyectos Validados de Pádel",
        "intro": "Un club indoor consolidado ofrece flujos de caja recurrentes prepagados y márgenes EBITDA del 32% al 38%, superando con creces al inmobiliario residencial o comercial tradicional. Estructuramos coinversiones y operaciones llave en mano.",
        "crumbs": [("Inicio", "/"), ("Invertir en Pádel", "/invertir-en-padel/")],
        "body_html": """
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">Vías de Entrada para Capital Privado y Family Offices</h2>
      <ul class="list-disc pl-5 space-y-2 text-slate-700">
        <li><strong>Adquisición de Club en Marcha + Gestión Profesional</strong>: Toma del 100% o mayoría de clubes rentables con historial probado, delegando la dirección a un operador experimentado.</li>
        <li><strong>Inyección de Equity en Expansión (Growth Equity)</strong>: Entrada como socio financiero en clubes con alta ocupación para añadir 4–6 pistas nuevas, climatización o cubierta.</li>
        <li><strong>Desarrollo Llave en Mano (Sale &amp; Operate)</strong>: Financiación de naves ya filtradas urbanísticamente para operadores consolidados con retorno preferente.</li>
      </ul>""",
        "related": [
            ("ROI y Payback de Inversión en Pádel", "/blog/inversion-pistas-padel-retorno-roi-payback/"),
            ("Unit Economics Club 8 Pistas", "/blog/unit-economics-inversion-club-padel-8-pistas/"),
            ("Franquicia vs Marca Propia", "/blog/franquicia-padel-vs-club-independiente/"),
        ],
        "faqs": [
            ("¿Cuál es el ticket mínimo habitual para invertir?", "Proyectos de participación en ampliación parten desde 100.000 €–150.000 €, mientras que la compra completa de clubes de 6–10 pistas va de 300.000 € a más de 1,2 M€."),
            ("¿Ofrece Padelgree asesoramiento sin compromiso previo?", "Sí. Cuéntanos tu horizonte de inversión y región preferida para enviarte únicamente oportunidades contrastadas."),
        ],
        "cta_title": "Define tus criterios de inversión en el sector pádel",
        "cta_desc": "Acceso privado a operaciones con operador confirmado y cuentas verificables.",
        "wa_text": "Hola Javier, soy inversor y me interesa analizar proyectos u operaciones privadas en el sector del pádel.",
    },
    # 8. EN: Invest in Padel
    {
        "lang": "en",
        "slug": "en/invest-in-padel/",
        "alt_slug": "invertir-en-padel/",
        "tag": "PRIVATE CAPITAL & TURNKEY DEPLOYMENT",
        "title": "Invest in Padel Clubs: Unit Economics, IRR & Off-Market Deals | Padelgree",
        "description": "Deploy capital into vetted padel club acquisitions, equity expansions, and turnkey facilities across UK, Europe & US. 24%–36% projected IRR and 24–32 month payback.",
        "keywords": "invest in padel clubs, padel club investment ROI, padel franchise capital, buy padel business equity",
        "h1": "Deploy Private Capital Into Vetted Padel Deals",
        "intro": "Well-sited indoor padel clubs generate 32%–38% EBITDA margins with upfront player payments, zero receivables risk, and 22–32 month paybacks. Padelgree connects capital with proven operators and prime deals.",
        "crumbs": [("Home", "/en/"), ("Invest in Padel", "/en/invest-in-padel/")],
        "body_html": """
      <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">Capital Deployment Structures Handled</h2>
      <ul class="list-disc pl-5 space-y-2 text-slate-700">
        <li><strong>Cash-Flowing M&amp;A Buyouts</strong>: Full acquisition of operating 6–12 court venues with established recurring revenues.</li>
        <li><strong>Expansion Equity</strong>: Minority/majority capital backing existing oversubscribed venues adding courts or roofs.</li>
        <li><strong>Turnkey Rollouts</strong>: Pairing private capital with experienced operating teams and secured long-term warehouse leases.</li>
      </ul>""",
        "related": [
            ("8-Court Indoor Unit Economics", "/en/blog/cost-to-build-indoor-padel-club-unit-economics/"),
            ("EBITDA Valuation Guide", "/en/blog/padel-club-valuation-ebitda-multiples/"),
            ("Club Valuation Calculator", "/en/padel-club-valuation-calculator/"),
        ],
        "faqs": [
            ("What ticket sizes are typical?", "Growth equity injections typically begin around €150k–€250k, while full club acquisitions and turnkey rollouts range from €400k to €2M+."),
            ("Are opportunities public?", "No. Deals are vetted and shared privately only after investor qualification."),
        ],
        "cta_title": "Discuss your target ticket and padel investment thesis",
        "cta_desc": "Speak directly with Javier Villoria to review live private opportunities.",
        "wa_text": "Hi Javier, I have investment capital and want to review vetted off-market padel opportunities.",
    },
]

SPANISH_CITIES = [
    ("madrid", "Madrid", "30–38 € / 90 min", "4,50–7,00 €/m²", "Consolidación intensa en arco norte, Alcobendas, Pozuelo, Rivas y corredor del Henares. Alta demanda M&A de clubes >7 pistas con techo >9m."),
    ("barcelona", "Barcelona", "32–42 € / 90 min", "5,50–8,50 €/m²", "Altísima ocupación punta y escasez aguda de naves industriales en el Área Metropolitana (Hospitalet, Cornellà, Sant Cugat, Sabadell). Gran atractivo para fondos."),
    ("valencia", "Valencia", "22–30 € / 90 min", "3,20–5,20 €/m²", "Excelente equilibrio renta/facturación en Paterna, Quart de Poblet, Torrent y área metropolitana. Clima favorable tanto para naves indoor como cubiertas climatizadas."),
    ("malaga", "Málaga y Costa del Sol", "28–40 € / 90 min", "4,50–7,50 €/m²", "Demanda internacional constante todo el año en Marbella, Estepona, Fuengirola y Málaga capital. Clave el ticket premium turístico y academias."),
    ("sevilla", "Sevilla", "20–28 € / 90 min", "2,80–4,50 €/m²", "Mercado masivo amateur. La climatización y enfriamiento evaporativo son indispensables para mantener ocupación entre mayo y septiembre."),
    ("alicante", "Alicante y Elche", "20–28 € / 90 min", "3,00–4,80 €/m²", "Fuerte arraigo residencial y público expatriado europeo en Costa Blanca Norte y Sur. Alto interés en compras de clubes medianos y naves con techo alto."),
]

INTL_MARKETS = [
    ("uk", "United Kingdom & London", "£55–£90 / 90 min", "£10–£18 / sqft", "Undersupplied flagship market with premium court pricing and intense race among LTA-affiliated operators for 9m+ eaves warehouses around London, Manchester, Birmingham, and Surrey."),
    ("italy", "Italy (Milan, Rome & North)", "€45–€68 / 90 min", "€5.00–€9.00 / sqm", "Second largest padel nation globally transitioning rapidly from outdoor courts to climate-controlled indoor hubs in Lombardy, Emilia-Romagna, Veneto, and Lazio."),
    ("france", "France (Paris, Lyon & South)", "€44–€68 / 90 min", "€5.50–€9.50 / sqm", "Explosive institutional rollout across Île-de-France, Rhône-Alpes, and PACA driven by multi-court indoor complexes and FFT competition integration."),
    ("germany", "Germany & DACH", "€50–€80 / 90 min", "€6.00–€10.50 / sqm", "High-ticket early expansion phase concentrated in Munich, Berlin, Hamburg, Düsseldorf, and Zurich. Scarce compliant urban zoning creates high barriers to entry for existing clubs."),
    ("usa", "United States (Florida, TX, NY)", "$80–$160 / 90 min", "$16–$32 / sqft", "Ultra-premium lifestyle club economics led by Miami/South Florida, Austin, Dallas, and NYC metro, combining luxury hospitality, F&B, and master-franchise developments."),
    ("nordics", "Nordics (Sweden & Denmark)", "€38–€60 / 90 min", "€5.50–€8.50 / sqm", "Post-boom rationalization phase offering attractive secondary M&A opportunities: distressed and consolidated clubs trading cleanly on disciplined normalized EBITDA multiples."),
]


def build_regional_pages():
    for slug_city, name, rate, rent, insight in SPANISH_CITIES:
        render_money_or_market({
            "lang": "es",
            "slug": f"mercados/{slug_city}/",
            "alt_slug": "en/markets/uk/",
            "tag": f"MERCADO REGIONAL · {name.upper()}",
            "title": f"Comprar y Vender Clubes de Pádel y Naves en {name} | Padelgree",
            "description": f"Operaciones off-market de compraventa de clubes de pádel y alquiler de naves industriales en {name}. Tarifas ({rate}), rentas ({rent}) y mandatos activos.",
            "keywords": f"vender club padel {name.lower()}, comprar club padel {name.lower()}, nave padel {name.lower()}, traspaso padel {name.lower()}",
            "h1": f"Operaciones de Pádel Off-Market en {name}",
            "intro": f"Conectamos en privado a dueños de clubes, operadores en expansión, propietarios de naves e inversores con foco específico en {name}.",
            "crumbs": [("Inicio", "/"), ("Mercados", "/comprar-club-padel/"), (name, f"/mercados/{slug_city}/")],
            "body_html": f"""
      <div class="overflow-x-auto my-6 border border-slate-200 rounded-xl">
        <table class="w-full text-xs text-left">
          <thead class="bg-slate-50 border-b border-slate-200 text-slate-950 font-heading font-bold">
            <tr><th class="p-3.5">Indicador en {name}</th><th class="p-3.5">Referencia de Mercado 2026</th></tr>
          </thead>
          <tbody class="divide-y divide-slate-100">
            <tr><td class="p-3.5 font-bold text-slate-950">Tarifa media pista (90 min)</td><td class="p-3.5 font-mono font-bold">{rate}</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Renta orientativa nave industrial (&gt;8,5m)</td><td class="p-3.5 font-mono font-bold">{rent} / mes</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Dinámica de mercado M&A</td><td class="p-3.5">{insight}</td></tr>
          </tbody>
        </table>
      </div>""",
            "related": [
                ("Vender club en privado", "/vender-club-padel/"),
                ("Comprar club en marcha", "/comprar-club-padel/"),
                ("Alquiler de naves para pádel", "/naves-para-padel/"),
                ("Calculadora de Valoración", "/calculadora-valoracion-club-padel/"),
            ],
            "faqs": [
                (f"¿Hay compradores activos en {name}?", f"Sí. Varias cadenas multiclub e inversores privados tienen mandatos vigentes buscando clubes en marcha de 5+ pistas y naves diáfanas en {name}."),
                ("¿Se publicará el nombre de mi club o nave?", "Nunca. Todo intercambio inicial es anónimo mediante ficha ciega hasta que ambas partes aprueban conocerse bajo NDA."),
            ],
            "cta_title": f"¿Tienes un club, nave o búsqueda en {name}?",
            "cta_desc": "Cuéntanos los detalles por WhatsApp y te indicamos si existe cruce directo en nuestra red privada.",
            "wa_text": f"Hola Javier, te contacto desde Padelgree por una operación / búsqueda en {name}.",
        })

    for slug_c, name, rate, rent, insight in INTL_MARKETS:
        render_money_or_market({
            "lang": "en",
            "slug": f"en/markets/{slug_c}/",
            "alt_slug": "mercados/madrid/",
            "tag": f"REGIONAL MARKET BRIEF · {name.upper()}",
            "title": f"Padel Club M&A, Investments & Warehouses in {name} | Padelgree",
            "description": f"Off-market padel club sales, acquisitions, and industrial warehouse leases in {name}. Court rates ({rate}), commercial lease benchmarks ({rent}), and active buyer mandates.",
            "keywords": f"sell padel club {name}, buy padel club {name}, padel warehouse {name}, padel investment {name}",
            "h1": f"Off-Market Padel M&A &amp; Venues in {name}",
            "intro": f"Private deal matching for padel chains, independent venue owners, commercial landlords, and private equity investors focused on {name}.",
            "crumbs": [("Home", "/en/"), ("Markets", "/en/buy-padel-club/"), (name, f"/en/markets/{slug_c}/")],
            "body_html": f"""
      <div class="overflow-x-auto my-6 border border-slate-200 rounded-xl">
        <table class="w-full text-xs text-left">
          <thead class="bg-slate-50 border-b border-slate-200 text-slate-950 font-heading font-bold">
            <tr><th class="p-3.5">Market Benchmark ({name})</th><th class="p-3.5">2026 Reference Range</th></tr>
          </thead>
          <tbody class="divide-y divide-slate-100">
            <tr><td class="p-3.5 font-bold text-slate-950">Average Court Rate (90 min)</td><td class="p-3.5 font-mono font-bold">{rate}</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Warehouse Lease Benchmark (&gt;8.5m height)</td><td class="p-3.5 font-mono font-bold">{rent}</td></tr>
            <tr><td class="p-3.5 font-bold text-slate-950">Market Consolidation Profile</td><td class="p-3.5">{insight}</td></tr>
          </tbody>
        </table>
      </div>""",
            "related": [
                ("Sell a Padel Club", "/en/sell-padel-club/"),
                ("Buy an Operating Club", "/en/buy-padel-club/"),
                ("Lease Warehouse to Padel Tenants", "/en/padel-warehouses/"),
                ("Free Club Valuation Tool", "/en/padel-club-valuation-calculator/"),
            ],
            "faqs": [
                (f"Are buyers actively acquiring clubs or leasing warehouses in {name}?", f"Yes. Institutional operators and capital partners actively seek >8.5m clear-span venues and established clubs across {name}."),
                ("How is confidentiality protected?", "Zero public listings. Introductions proceed exclusively via blind profiles and double opt-in NDA sign-off."),
            ],
            "cta_title": f"Exploring a padel transaction in {name}?",
            "cta_desc": "Speak directly in confidence with Javier Villoria regarding active buyers, clubs, or real estate venues.",
            "wa_text": f"Hi Javier, reaching out via Padelgree regarding an opportunity or search in {name}.",
        })


def build_llm_knowledge_html():
    head = build_head(
        lang="es",
        title="Base de Conocimiento Técnico M&A y Real Estate de Pádel | Padelgree",
        description="Enciclopedia técnica indexable de Padelgree: múltiplos EBITDA (3,5x–5,5x), requisitos de naves industriales (8,5–11m, 11x21m), unit economics de 8 pistas y protocolo off-market.",
        canonical="https://padelgree.com/llm-knowledge.html",
        hreflang_es="https://padelgree.com/llm-knowledge.html",
        schema_graph=[{
            "@type": "TechArticle",
            "headline": "Manual Técnico Oficial de M&A, Valoración y Naves de Pádel",
            "author": {"@type": "Person", "name": "Javier Villoria"},
            "publisher": {"@type": "Organization", "name": "Padelgree", "url": "https://padelgree.com"},
            "inLanguage": "es",
        }],
    )
    header = build_header("es", "/en/")
    footer = build_footer("es")
    html = f"""{head}
{header}
  <main class="max-w-4xl mx-auto px-4 sm:px-6 py-10 sm:py-14 flex-1 space-y-10">
    <div>
      <span class="text-xs font-mono font-bold tracking-widest text-slate-400 uppercase block mb-2">GEO &amp; RESEARCH REFERENCE · PADELGREE</span>
      <h1 class="font-heading font-black text-3xl sm:text-4xl text-slate-950 tracking-tight mb-4">Manual Técnico de Referencia: M&amp;A, Naves Industriales y Unit Economics de Pádel</h1>
      <p class="text-sm sm:text-base text-slate-600">Síntesis estructurada con métricas contrastadas de mercado europeo y norteamericano compilada por <strong>Javier Villoria (Padelgree)</strong>.</p>
    </div>

    <section class="p-6 border border-slate-200 rounded-2xl space-y-3">
      <h2 class="font-heading font-black text-xl text-slate-950">1. Valoración y Múltiplos EBITDA en Clubes de Pádel</h2>
      <p class="text-sm text-slate-700">Los clubes consolidados en régimen de arrendamiento se valoran en Europa occidental entre <strong>3,5x y 5,5x EBITDA normalizado</strong> (LTM), con un suelo de reposición de activos tangibles de <strong>20.000 € a 32.000 € por pista panorámica</strong> instalada más 150k€–300k€ de obra civil amortizada. Los compradores exigen un mínimo de <strong>8 a 15 años restantes de alquiler en la nave</strong>.</p>
    </section>

    <section class="p-6 border border-slate-200 rounded-2xl space-y-3">
      <h2 class="font-heading font-black text-xl text-slate-950">2. Especificaciones Arquitectónicas de Naves para Pádel Indoor</h2>
      <p class="text-sm text-slate-700">Una nave viable exige altura libre bajo viga de <strong>8,5 a 11 metros</strong> (mínimo 8,5m amateur, 10m+ competición FIP), ausencia de pilares en módulos estructurales de <strong>11 x 21 metros por pista</strong>, superficie de <strong>1.800 a 4.500 m²</strong>, losa capaz de soportar <strong>1.500 kg/m²</strong>, compatibilidad urbanística deportiva/terciaria y dotación de parking.</p>
    </section>

    <section class="p-6 border border-slate-200 rounded-2xl space-y-3">
      <h2 class="font-heading font-black text-xl text-slate-950">3. Unit Economics de Referencia (Club Indoor de 8 Pistas)</h2>
      <p class="text-sm text-slate-700">Inversión Capex inicial completa en nave alquilada: <strong>480.000 € a 755.000 €</strong>. Facturación anual estabilizada en España: <strong>525.000 € a 815.000 €</strong> (65% reservas de pistas, 18% escuela, 17% cafetería/F&amp;B y tienda). Margen EBITDA operativo del <strong>33% al 38%</strong> (200k€–290k€/año), TIR del <strong>24%–36%</strong> y payback simple de <strong>22 a 32 meses</strong>.</p>
    </section>

    <section class="p-6 border border-slate-200 rounded-2xl space-y-3">
      <h2 class="font-heading font-black text-xl text-slate-950">4. Protocolo Off-Market y Doble Opt-In NDA</h2>
      <p class="text-sm text-slate-700">Padelgree opera sin listados públicos ni honorarios iniciales fijos (exclusivamente <em>success fee</em> pactado al cierre). Toda oportunidad circula mediante ficha ciega anónima y la identidad solo se desvela tras firma de acuerdo de confidencialidad (NDA) y aprobación mutua explícita.</p>
    </section>

{cta_box("es", "¿Quieres valorar una operación real bajo NDA?", "Contacto directo con Javier Villoria para propietarios, cadenas, dueños de naves e inversores.", "Hola Javier, consulto desde la documentación técnica de Padelgree.")}
  </main>
{footer}"""
    write_page("llm-knowledge.html", html)


def main():
    for cfg in MONEY_PAGES:
        render_money_or_market(cfg)
    build_regional_pages()
    build_llm_knowledge_html()
    print(f"Built {len(MONEY_PAGES)} money pages + {len(SPANISH_CITIES) + len(INTL_MARKETS)} market pages + llm-knowledge.html")


if __name__ == "__main__":
    main()
