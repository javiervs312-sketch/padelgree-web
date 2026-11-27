#!/usr/bin/env python3
"""
Upgrades existing ES HTML files (static CSS, OG images, internal linking mesh, SEO titles/hreflang),
compiles static purged Tailwind CSS, builds a 100% pure canonical HTML sitemap.xml, and updates llms.txt.
Idempotent: safe to re-run repeatedly.
"""

from datetime import date
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent
TODAY = "2026-11-27"

ES_EN_PAIRED_BLOGS = {
    "valoracion-clubes-padel-multiplos-ebitda": "padel-club-valuation-ebitda-multiples",
    "por-que-vender-club-padel-off-market-confidencial": "how-to-sell-a-padel-club-off-market",
    "requisitos-tecnicos-naves-industriales-padel": "padel-warehouse-requirements-ceiling-height-lease",
    "unit-economics-inversion-club-padel-8-pistas": "cost-to-build-indoor-padel-club-unit-economics",
    "due-diligence-compra-club-padel-checklist": "buy-padel-club-europe-uk-due-diligence",
}

ALL_HTML_PAIRED = {
    "/": "/en/",
    "/blog/": "/en/blog/",
    "/vender-club-padel/": "/en/sell-padel-club/",
    "/comprar-club-padel/": "/en/buy-padel-club/",
    "/naves-para-padel/": "/en/padel-warehouses/",
    "/invertir-en-padel/": "/en/invest-in-padel/",
    "/calculadora-valoracion-club-padel/": "/en/padel-club-valuation-calculator/",
    "/calculadora-pistas-nave/": "/en/padel-warehouse-court-calculator/",
    **{f"/blog/{k}/": f"/en/blog/{v}/" for k, v in ES_EN_PAIRED_BLOGS.items()},
}
EN_TO_ES_PAIRED = {v: k for k, v in ALL_HTML_PAIRED.items()}

RELATED_CLUSTERS = {
    "valoracion-clubes-padel-multiplos-ebitda": [
        ("Calculadora Valoración Club", "/calculadora-valoracion-club-padel/"),
        ("Vender Club Off-Market", "/vender-club-padel/"),
        ("Due Diligence M&A", "/blog/due-diligence-compra-club-padel-checklist/"),
        ("Traspasos de Clubes", "/blog/traspaso-club-padel-guia-legal-contratos-precio/"),
    ],
    "cuanto-cuesta-montar-un-club-de-padel-indoor": [
        ("Calculadora Pistas por Nave", "/calculadora-pistas-nave/"),
        ("Unit Economics 8 Pistas", "/blog/unit-economics-inversion-club-padel-8-pistas/"),
        ("Precio Construir Pista", "/blog/cuanto-cuesta-construir-una-pista-de-padel/"),
        ("Licencia de Apertura", "/blog/licencia-apertura-club-padel-normativa-requisitos/"),
    ],
    "cuanto-gana-un-club-de-padel-facturacion-rentabilidad": [
        ("Calculadora Valoración Club", "/calculadora-valoracion-club-padel/"),
        ("ROI y Payback", "/blog/inversion-pistas-padel-retorno-roi-payback/"),
        ("Franquicia vs Independiente", "/blog/franquicia-padel-vs-club-independiente/"),
        ("Múltiplos EBITDA", "/blog/valoracion-clubes-padel-multiplos-ebitda/"),
    ],
    "traspaso-club-padel-guia-legal-contratos-precio": [
        ("Vender Club en Privado", "/vender-club-padel/"),
        ("Calculadora Valoración Club", "/calculadora-valoracion-club-padel/"),
        ("Contrato Alquiler Nave", "/blog/contrato-alquiler-nave-industrial-club-padel/"),
        ("Due Diligence M&A", "/blog/due-diligence-compra-club-padel-checklist/"),
    ],
    "contrato-alquiler-nave-industrial-club-padel": [
        ("Naves para Pádel", "/naves-para-padel/"),
        ("Calculadora Pistas Nave", "/calculadora-pistas-nave/"),
        ("Requisitos Técnicos Naves", "/blog/requisitos-tecnicos-naves-industriales-padel/"),
        ("Licencia de Apertura", "/blog/licencia-apertura-club-padel-normativa-requisitos/"),
    ],
    "requisitos-tecnicos-naves-industriales-padel": [
        ("Calculadora Pistas Nave", "/calculadora-pistas-nave/"),
        ("Alquilar Nave a Operador", "/naves-para-padel/"),
        ("Climatización de Naves", "/blog/climatizacion-naves-padel-indoor-sistemas-costes/"),
        ("Contrato Alquiler Nave", "/blog/contrato-alquiler-nave-industrial-club-padel/"),
    ],
    "unit-economics-inversion-club-padel-8-pistas": [
        ("Invertir en Pádel", "/invertir-en-padel/"),
        ("ROI y Payback", "/blog/inversion-pistas-padel-retorno-roi-payback/"),
        ("Cuánto Cuesta Montar Club", "/blog/cuanto-cuesta-montar-un-club-de-padel-indoor/"),
        ("Cuánto Gana un Club", "/blog/cuanto-gana-un-club-de-padel-facturacion-rentabilidad/"),
    ],
    "due-diligence-compra-club-padel-checklist": [
        ("Comprar Club Off-Market", "/comprar-club-padel/"),
        ("Calculadora Valoración Club", "/calculadora-valoracion-club-padel/"),
        ("Múltiplos EBITDA", "/blog/valoracion-clubes-padel-multiplos-ebitda/"),
        ("Traspaso de Clubes", "/blog/traspaso-club-padel-guia-legal-contratos-precio/"),
    ],
    "franquicia-padel-vs-club-independiente": [
        ("Expansión de Cadenas", "/blog/expansion-cadenas-padel-espana-europa/"),
        ("Invertir en Pádel", "/invertir-en-padel/"),
        ("Software de Gestión", "/blog/software-gestion-clubes-padel-comparativa/"),
        ("Cuánto Gana un Club", "/blog/cuanto-gana-un-club-de-padel-facturacion-rentabilidad/"),
    ],
    "por-que-vender-club-padel-off-market-confidencial": [
        ("Vender Club en Privado", "/vender-club-padel/"),
        ("Calculadora Valoración Club", "/calculadora-valoracion-club-padel/"),
        ("Expansión de Cadenas", "/blog/expansion-cadenas-padel-espana-europa/"),
        ("Traspaso de Clubes", "/blog/traspaso-club-padel-guia-legal-contratos-precio/"),
    ],
    "licencia-apertura-club-padel-normativa-requisitos": [
        ("Calculadora Pistas Nave", "/calculadora-pistas-nave/"),
        ("Requisitos Técnicos Naves", "/blog/requisitos-tecnicos-naves-industriales-padel/"),
        ("Contrato Alquiler Nave", "/blog/contrato-alquiler-nave-industrial-club-padel/"),
        ("Cuánto Cuesta Montar Club", "/blog/cuanto-cuesta-montar-un-club-de-padel-indoor/"),
    ],
    "cuanto-cuesta-construir-una-pista-de-padel": [
        ("Cuánto Cuesta Montar Club", "/blog/cuanto-cuesta-montar-un-club-de-padel-indoor/"),
        ("Calculadora Pistas Nave", "/calculadora-pistas-nave/"),
        ("Unit Economics 8 Pistas", "/blog/unit-economics-inversion-club-padel-8-pistas/"),
        ("Climatización de Naves", "/blog/climatizacion-naves-padel-indoor-sistemas-costes/"),
    ],
    "climatizacion-naves-padel-indoor-sistemas-costes": [
        ("Requisitos Técnicos Naves", "/blog/requisitos-tecnicos-naves-industriales-padel/"),
        ("Calculadora Pistas Nave", "/calculadora-pistas-nave/"),
        ("Cuánto Cuesta Montar Club", "/blog/cuanto-cuesta-montar-un-club-de-padel-indoor/"),
        ("Software y Domótica", "/blog/software-gestion-clubes-padel-comparativa/"),
    ],
    "inversion-pistas-padel-retorno-roi-payback": [
        ("Invertir en Pádel", "/invertir-en-padel/"),
        ("Unit Economics 8 Pistas", "/blog/unit-economics-inversion-club-padel-8-pistas/"),
        ("Cuánto Gana un Club", "/blog/cuanto-gana-un-club-de-padel-facturacion-rentabilidad/"),
        ("Calculadora Valoración Club", "/calculadora-valoracion-club-padel/"),
    ],
    "software-gestion-clubes-padel-comparativa": [
        ("Cuánto Gana un Club", "/blog/cuanto-gana-un-club-de-padel-facturacion-rentabilidad/"),
        ("Due Diligence M&A", "/blog/due-diligence-compra-club-padel-checklist/"),
        ("Franquicia vs Independiente", "/blog/franquicia-padel-vs-club-independiente/"),
        ("Comprar Club Off-Market", "/comprar-club-padel/"),
    ],
    "expansion-cadenas-padel-espana-europa": [
        ("Comprar Club Off-Market", "/comprar-club-padel/"),
        ("Vender Club a Operador", "/vender-club-padel/"),
        ("Mercados Madrid / Barcelona", "/mercados/madrid/"),
        ("Franquicia vs Independiente", "/blog/franquicia-padel-vs-club-independiente/"),
    ],
}

TW_CDN_RE = re.compile(
    r'\s*<!-- Tailwind CSS CDN -->\s*<script src="https://cdn\.tailwindcss\.com"></script>\s*<script>\s*tailwind\.config\s*=\s*\{.*?</script>',
    re.S,
)
TW_BARE_RE = re.compile(
    r'\s*<script src="https://cdn\.tailwindcss\.com"></script>\s*<script>\s*tailwind\.config\s*=\s*\{.*?</script>',
    re.S,
)


def swap_to_static_css_and_og(html: str, is_en: bool = False, extra_hreflang: str = "") -> str:
    html = TW_CDN_RE.sub('\n  <link rel="stylesheet" href="/assets/css/padelgree.min.css">', html)
    html = TW_BARE_RE.sub('\n  <link rel="stylesheet" href="/assets/css/padelgree.min.css">', html)

    if extra_hreflang and extra_hreflang not in html:
        html = html.replace(
            '<link rel="alternate" hreflang="x-default"',
            f'{extra_hreflang}\n  <link rel="alternate" hreflang="x-default"',
            1,
        )

    og_img = "https://padelgree.com/assets/og/padelgree-en.png" if is_en else "https://padelgree.com/assets/og/padelgree-es.png"
    if 'property="og:image"' not in html:
        html = html.replace(
            '<meta property="og:description"',
            f'<meta property="og:image" content="{og_img}">\n  <meta property="og:image:width" content="1200">\n  <meta property="og:image:height" content="630">\n  <meta property="og:description"',
            1,
        )
    if 'name="twitter:card"' not in html:
        html = html.replace(
            "</head>",
            f'  <meta name="twitter:card" content="summary_large_image">\n  <meta name="twitter:image" content="{og_img}">\n</head>',
            1,
        )
    else:
        html = re.sub(r'<meta name="twitter:card" content="summary">', '<meta name="twitter:card" content="summary_large_image">', html)
        if 'name="twitter:image"' not in html:
            html = html.replace('</head>', f'  <meta name="twitter:image" content="{og_img}">\n</head>', 1)

    return html


def upgrade_es_articles():
    blog_dir = ROOT / "blog"
    for sub in sorted(blog_dir.iterdir()):
        if not sub.is_dir():
            continue
        html_path = sub / "index.html"
        if not html_path.exists():
            continue
        slug = sub.name
        txt = html_path.read_text(encoding="utf-8")

        extra_href = ""
        if slug in ES_EN_PAIRED_BLOGS:
            en_u = f"https://padelgree.com/en/blog/{ES_EN_PAIRED_BLOGS[slug]}/"
            if f'hreflang="en"' not in txt:
                extra_href = f'<link rel="alternate" hreflang="en" href="{en_u}">'

        txt = swap_to_static_css_and_og(txt, is_en=False, extra_hreflang=extra_href)

        # Update header to expose Valoración calculator cleanly
        if '/calculadora-valoracion-club-padel/' not in txt and '<a href="/blog/" class="text-xs font-bold text-slate-600' in txt:
            txt = txt.replace(
                '<a href="/blog/" class="text-xs font-bold text-slate-600 hover:text-slate-950 transition">← Ver todos los artículos</a>',
                '<a href="/blog/" class="text-xs font-bold text-slate-600 hover:text-slate-950 transition">← Blog</a>\n        <a href="/calculadora-valoracion-club-padel/" class="hidden sm:inline-block text-xs font-bold text-slate-700 hover:text-slate-950 transition">Calculadora Valor</a>',
                1,
            )

        # Inject internal linking cluster mesh above WhatsApp CTA box (idempotent)
        if "<!-- INTERLINKING CLUSTER -->" not in txt:
            rels = RELATED_CLUSTERS.get(slug, [
                ("Calculadora Valoración Club", "/calculadora-valoracion-club-padel/"),
                ("Calculadora Pistas Nave", "/calculadora-pistas-nave/"),
                ("Vender Club en Privado", "/vender-club-padel/"),
                ("Comprar Club Off-Market", "/comprar-club-padel/"),
            ])
            pills = "\n        ".join(
                f'<a href="{u}" class="px-3.5 py-2 rounded-xl border border-slate-200 hover:border-slate-950 bg-white text-xs font-bold text-slate-900 transition">{t} →</a>'
                for t, u in rels
            )
            cluster_html = f"""    <!-- INTERLINKING CLUSTER -->
    <div class="mt-10 pt-8 border-t border-slate-200">
      <h2 class="font-heading font-black text-lg text-slate-950 mb-3">Calculadoras y Guías Relacionadas</h2>
      <div class="flex flex-wrap gap-2">
        {pills}
      </div>
    </div>

"""
            txt = txt.replace("    <!-- CAJA DE CONTACTO CON JAVIER -->", cluster_html + "    <!-- CAJA DE CONTACTO CON JAVIER -->", 1)

        html_path.write_text(txt, encoding="utf-8")


def upgrade_es_blog_hub():
    hub_path = ROOT / "blog" / "index.html"
    txt = hub_path.read_text(encoding="utf-8")
    txt = swap_to_static_css_and_og(
        txt,
        is_en=False,
        extra_hreflang='<link rel="alternate" hreflang="en" href="https://padelgree.com/en/blog/">',
    )
    if "<!-- PILLS HERRAMIENTAS Y MONEY PAGES -->" not in txt:
        pills_bar = """    <!-- PILLS HERRAMIENTAS Y MONEY PAGES -->
    <div class="flex flex-wrap items-center gap-2 mb-10 pb-8 border-b border-slate-200">
      <a href="/calculadora-valoracion-club-padel/" class="px-4 py-2 rounded-full bg-slate-950 text-white text-xs font-heading font-bold uppercase tracking-wider hover:bg-slate-800 transition">Calculadora Valoración EBITDA →</a>
      <a href="/calculadora-pistas-nave/" class="px-4 py-2 rounded-full border border-slate-300 hover:border-slate-950 text-slate-950 text-xs font-heading font-bold uppercase tracking-wider transition">Calculadora Pistas Nave →</a>
      <a href="/vender-club-padel/" class="px-3.5 py-2 rounded-full border border-slate-200 hover:border-slate-950 text-slate-700 text-xs font-bold transition">Vender Club</a>
      <a href="/comprar-club-padel/" class="px-3.5 py-2 rounded-full border border-slate-200 hover:border-slate-950 text-slate-700 text-xs font-bold transition">Comprar Club</a>
      <a href="/naves-para-padel/" class="px-3.5 py-2 rounded-full border border-slate-200 hover:border-slate-950 text-slate-700 text-xs font-bold transition">Naves Industriales</a>
      <a href="/en/blog/" class="px-3.5 py-2 rounded-full border border-slate-200 hover:border-slate-950 text-slate-700 text-xs font-bold transition">English Blog</a>
    </div>

"""
        txt = txt.replace("    <!-- LISTADO DE 16 ARTÍCULOS EN GRID -->", pills_bar + "    <!-- LISTADO DE 16 ARTÍCULOS EN GRID -->", 1)
    hub_path.write_text(txt, encoding="utf-8")


def upgrade_es_home():
    home_path = ROOT / "index.html"
    txt = home_path.read_text(encoding="utf-8")

    # 1. Spanish SEO title & description while preserving brand identity
    txt = txt.replace(
        "<title>Padelgree | The Confidential B2B Network for Padel Deals</title>",
        "<title>Padelgree | Comprar y Vender Clubes de Pádel, Naves e Inversión Off-Market</title>",
    )
    txt = txt.replace(
        '<meta name="description" content="The confidential B2B network for padel deals. Private introductions between padel operators, club owners, commercial landlords, and investors. Zero public listings.">',
        '<meta name="description" content="La red B2B confidencial para operaciones de pádel. Conexiones privadas off-market entre operadores, dueños de clubes, propietarios de naves industriales e inversores.">',
    )

    # 2. Proper reciprocal hreflang to /en/ + clean og:image + static CSS
    txt = txt.replace(
        '<link rel="alternate" hreflang="en" href="https://padelgree.com/">',
        '<link rel="alternate" hreflang="en" href="https://padelgree.com/en/">',
    )
    txt = swap_to_static_css_and_og(txt, is_en=False)

    # 3. Defer Lucide cleanly (remove head sync script, load deferred before body close)
    txt = txt.replace(
        '  <!-- Lucide Icons -->\n  <script src="https://unpkg.com/lucide@latest"></script>\n',
        "",
    )
    txt = txt.replace(
        '  <!-- Lucide Icons -->\r\n  <script src="https://unpkg.com/lucide@latest"></script>\r\n',
        "",
    )
    if "lucide.min.js" not in txt:
        txt = txt.replace(
            "  <!-- SCRIPT -->",
            '  <!-- SCRIPT -->\n  <script src="https://unpkg.com/lucide@0.468.0/dist/umd/lucide.min.js" defer></script>',
        )
    txt = txt.replace(
        "  <script>\n    lucide.createIcons();",
        "  <script>\n    document.addEventListener('DOMContentLoaded', () => { if (window.lucide) lucide.createIcons(); });",
    )
    txt = txt.replace(
        "  <script>\r\n    lucide.createIcons();",
        "  <script>\r\n    document.addEventListener('DOMContentLoaded', () => { if (window.lucide) lucide.createIcons(); });",
    )

    # 4. Header: replace JS language toggle button with crawlable <a href="/en/">EN</a> + Valoración link
    old_btn = re.compile(
        r'<button type="button" onclick="toggleLanguage\(\)"[^>]*>.*?<span id="current-lang">EN</span>.*?</button>',
        re.S,
    )
    txt = old_btn.sub(
        '<a href="/en/" class="px-2.5 py-1 rounded-full border border-slate-300 text-xs font-bold text-slate-700 hover:border-slate-900 transition" title="English version">EN</a>',
        txt,
    )
    if '/calculadora-valoracion-club-padel/' not in txt:
        txt = txt.replace(
            '<a href="/blog/" class="text-xs font-heading font-bold text-slate-700 hover:text-slate-950 tracking-wider uppercase transition">\n          Blog\n        </a>',
            '<a href="/blog/" class="text-xs font-heading font-bold text-slate-700 hover:text-slate-950 tracking-wider uppercase transition">Blog</a>\n        <a href="/calculadora-valoracion-club-padel/" class="hidden sm:inline-block text-xs font-heading font-bold text-slate-700 hover:text-slate-950 tracking-wider uppercase transition">Valoración</a>',
        )

    # 5. Enrich footer with Money Pages, Calculators, Markets, and English Blog (without touching Hero!)
    if "<!-- SOLUCIONES Y CALCULADORAS FOOTER -->" not in txt:
        sol_footer = """      <!-- SOLUCIONES Y CALCULADORAS FOOTER -->
      <div class="pt-3 border-t border-slate-100 flex flex-wrap items-center justify-between gap-y-2 text-xs text-slate-600">
        <div class="flex flex-wrap items-center gap-x-3 gap-y-1.5">
          <span class="font-heading font-black text-slate-900">SOLUCIONES &amp; HERRAMIENTAS:</span>
          <a href="/vender-club-padel/" class="hover:text-slate-950 transition">Vender Club</a>
          <span>·</span>
          <a href="/comprar-club-padel/" class="hover:text-slate-950 transition">Comprar Club</a>
          <span>·</span>
          <a href="/naves-para-padel/" class="hover:text-slate-950 transition">Alquiler de Naves</a>
          <span>·</span>
          <a href="/invertir-en-padel/" class="hover:text-slate-950 transition">Invertir en Pádel</a>
          <span>·</span>
          <a href="/calculadora-valoracion-club-padel/" class="font-bold text-slate-900 hover:underline">Calculadora Valoración</a>
          <span>·</span>
          <a href="/calculadora-pistas-nave/" class="font-bold text-slate-900 hover:underline">Calculadora Pistas Nave</a>
          <span>·</span>
          <a href="/mercados/madrid/" class="hover:text-slate-950 transition">Madrid</a>
          <span>·</span>
          <a href="/mercados/barcelona/" class="hover:text-slate-950 transition">Barcelona</a>
          <span>·</span>
          <a href="/mercados/valencia/" class="hover:text-slate-950 transition">Valencia</a>
          <span>·</span>
          <a href="/mercados/malaga/" class="hover:text-slate-950 transition">Málaga</a>
          <span>·</span>
          <a href="/en/" class="font-bold text-slate-900 hover:underline">English (/en/)</a>
          <span>·</span>
          <a href="/llm-knowledge.html" class="hover:text-slate-950 transition">Manual Técnico</a>
        </div>
      </div>

"""
        txt = txt.replace("      <!-- SECCIÓN BLOG Y ARTÍCULOS TÉCNICOS -->", sol_footer + "      <!-- SECCIÓN BLOG Y ARTÍCULOS TÉCNICOS -->", 1)

    home_path.write_text(txt, encoding="utf-8")


def compile_static_css():
    tw_cmd = ROOT.parent / "coolpadel-web" / "node_modules" / ".bin" / "tailwindcss.cmd"
    if not tw_cmd.exists():
        tw_cmd = ROOT.parent / "coolpadel-web" / "node_modules" / ".bin" / "tailwindcss"
    cmd = [
        str(tw_cmd),
        "-c", str(ROOT / "tailwind.config.js"),
        "-i", str(ROOT / "assets" / "css" / "input.css"),
        "-o", str(ROOT / "assets" / "css" / "padelgree.min.css"),
        "--minify",
    ]
    subprocess.run(cmd, cwd=str(ROOT), check=True)
    size = (ROOT / "assets" / "css" / "padelgree.min.css").stat().st_size
    print(f"Compiled static CSS: padelgree.min.css ({size} bytes)")


def build_pure_sitemap():
    """Creates a clean HTML-only sitemap.xml (no .txt/.md files that trigger GSC warnings)."""
    urls = []
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT).as_posix()
        if rel == "index.html":
            loc = "https://padelgree.com/"
            prio = "1.0"
            freq = "weekly"
        elif rel.endswith("/index.html"):
            path_part = "/" + rel[: -len("index.html")]
            loc = "https://padelgree.com" + path_part
            prio = "0.9" if path_part in ("/en/", "/blog/", "/en/blog/") or "calculadora" in path_part or "calculator" in path_part else "0.8"
            freq = "weekly" if path_part in ("/en/", "/blog/", "/en/blog/") else "monthly"
        else:
            path_part = "/" + rel
            loc = "https://padelgree.com" + path_part
            prio = "0.7"
            freq = "monthly"
        urls.append((path_part if rel != "index.html" else "/", loc, prio, freq))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for path_part, loc, prio, freq in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <lastmod>{TODAY}</lastmod>")
        lines.append(f"    <changefreq>{freq}</changefreq>")
        lines.append(f"    <priority>{prio}</priority>")
        if path_part in ALL_HTML_PAIRED:
            es_u = "https://padelgree.com" + path_part
            en_u = "https://padelgree.com" + ALL_HTML_PAIRED[path_part]
            lines.append(f'    <xhtml:link rel="alternate" hreflang="es" href="{es_u}"/>')
            lines.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{en_u}"/>')
            lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{es_u}"/>')
        elif path_part in EN_TO_ES_PAIRED:
            en_u = "https://padelgree.com" + path_part
            es_u = "https://padelgree.com" + EN_TO_ES_PAIRED[path_part]
            lines.append(f'    <xhtml:link rel="alternate" hreflang="es" href="{es_u}"/>')
            lines.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{en_u}"/>')
            lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{es_u}"/>')
        lines.append("  </url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated clean HTML-only sitemap.xml with {len(urls)} canonical URLs")


def main():
    upgrade_es_home()
    upgrade_es_blog_hub()
    upgrade_es_articles()
    compile_static_css()
    build_pure_sitemap()


if __name__ == "__main__":
    main()
