"""Shared monochrome editorial HTML chrome & SEO helpers for Padelgree."""

from html import escape
import json


def build_head(
    *,
    lang: str,
    title: str,
    description: str,
    canonical: str,
    keywords: str = "",
    og_type: str = "website",
    hreflang_es: str | None = None,
    hreflang_en: str | None = None,
    schema_graph: list[dict] | None = None,
) -> str:
    og_img = (
        "https://padelgree.com/assets/og/padelgree-en.png"
        if lang == "en"
        else "https://padelgree.com/assets/og/padelgree-es.png"
    )
    og_locale = "en_US" if lang == "en" else "es_ES"

    hreflang_tags = []
    if hreflang_es:
        hreflang_tags.append(f'  <link rel="alternate" hreflang="es" href="{hreflang_es}">')
    if hreflang_en:
        hreflang_tags.append(f'  <link rel="alternate" hreflang="en" href="{hreflang_en}">')
    xdef = hreflang_es or hreflang_en or canonical
    hreflang_tags.append(f'  <link rel="alternate" hreflang="x-default" href="{xdef}">')
    hreflang_block = "\n".join(hreflang_tags)

    kw_meta = f'\n  <meta name="keywords" content="{escape(keywords)}">' if keywords else ""

    schema_block = ""
    if schema_graph:
        payload = {"@context": "https://schema.org", "@graph": schema_graph}
        schema_block = (
            '\n  <script type="application/ld+json">\n'
            + json.dumps(payload, ensure_ascii=False, indent=2)
            + "\n  </script>"
        )

    return f"""<!DOCTYPE html>
<html lang="{lang}" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">
  <meta name="author" content="Javier Villoria">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">{kw_meta}

  <link rel="icon" type="image/svg+xml" href="https://padelgree.com/favicon.svg">
  <link rel="apple-touch-icon" href="https://padelgree.com/favicon.svg">

  <link rel="canonical" href="{canonical}">
{hreflang_block}

  <link rel="alternate" type="text/markdown" href="https://padelgree.com/llms.txt" title="LLMs.txt">
  <link rel="alternate" type="text/markdown" href="https://padelgree.com/llms-full.txt" title="LLMs-Full.txt">

  <meta property="og:type" content="{og_type}">
  <meta property="og:locale" content="{og_locale}">
  <meta property="og:site_name" content="Padelgree">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:image" content="{og_img}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{escape(title)}">
  <meta name="twitter:description" content="{escape(description)}">
  <meta name="twitter:image" content="{og_img}">{schema_block}

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/padelgree.min.css">
</head>"""


def build_header(lang: str, alt_url: str | None = None) -> str:
    if lang == "en":
        home = "/en/"
        blog_href = "/en/blog/"
        val_href = "/en/padel-club-valuation-calculator/"
        val_label = "Valuation"
        switch_href = alt_url or "/"
        switch_label = "ES"
        cta_label = "Contact"
    else:
        home = "/"
        blog_href = "/blog/"
        val_href = "/calculadora-valoracion-club-padel/"
        val_label = "Valoración"
        switch_href = alt_url or "/en/"
        switch_label = "EN"
        cta_label = "Contactar"

    return f"""<body class="bg-white text-slate-900 font-sans font-medium antialiased selection:bg-slate-900 selection:text-white min-h-screen flex flex-col justify-between">
  <header class="fixed top-0 left-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-slate-200">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 h-14 sm:h-16 flex items-center justify-between">
      <a href="{home}" class="flex items-center">
        <span class="font-heading font-black text-xl sm:text-2xl tracking-wider text-slate-950">PADELGREE</span>
      </a>
      <div class="flex items-center gap-2.5 sm:gap-4">
        <a href="{blog_href}" class="text-xs font-heading font-bold text-slate-700 hover:text-slate-950 tracking-wider uppercase transition">Blog</a>
        <a href="{val_href}" class="hidden sm:inline-block text-xs font-heading font-bold text-slate-700 hover:text-slate-950 tracking-wider uppercase transition">{val_label}</a>
        <a href="{switch_href}" class="px-2.5 py-1 rounded-full border border-slate-300 text-xs font-bold text-slate-700 hover:border-slate-900 transition">{switch_label}</a>
        <a href="https://wa.me/34680317486" target="_blank" rel="noopener" class="px-3.5 py-1.5 rounded-full bg-slate-950 hover:bg-slate-800 text-white font-heading font-bold text-xs uppercase tracking-wider transition">{cta_label}</a>
      </div>
    </div>
  </header>
  <div class="h-14 sm:h-16 w-full" aria-hidden="true"></div>"""


def build_footer(lang: str) -> str:
    if lang == "en":
        links = (
            '<a href="/en/" class="hover:text-slate-950 transition">Home</a><span>·</span>'
            '<a href="/en/sell-padel-club/" class="hover:text-slate-950 transition">Sell Club</a><span>·</span>'
            '<a href="/en/buy-padel-club/" class="hover:text-slate-950 transition">Buy Club</a><span>·</span>'
            '<a href="/en/padel-warehouses/" class="hover:text-slate-950 transition">Warehouses</a><span>·</span>'
            '<a href="/en/padel-club-valuation-calculator/" class="hover:text-slate-950 transition font-bold text-slate-800">Valuation Tool</a><span>·</span>'
            '<a href="/en/blog/" class="hover:text-slate-950 transition">Blog</a><span>·</span>'
            '<a href="/" class="hover:text-slate-950 transition">Español</a>'
        )
    else:
        links = (
            '<a href="/" class="hover:text-slate-950 transition">Inicio</a><span>·</span>'
            '<a href="/vender-club-padel/" class="hover:text-slate-950 transition">Vender Club</a><span>·</span>'
            '<a href="/comprar-club-padel/" class="hover:text-slate-950 transition">Comprar Club</a><span>·</span>'
            '<a href="/naves-para-padel/" class="hover:text-slate-950 transition">Naves</a><span>·</span>'
            '<a href="/calculadora-valoracion-club-padel/" class="hover:text-slate-950 transition font-bold text-slate-800">Calculadora Valor</a><span>·</span>'
            '<a href="/blog/" class="hover:text-slate-950 transition">Blog</a><span>·</span>'
            '<a href="/en/" class="hover:text-slate-950 transition">English</a>'
        )

    return f"""  <footer class="w-full border-t border-slate-200 bg-white py-8 mt-12">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-500">
      <span class="font-heading font-bold text-slate-950">PADELGREE · The Confidential B2B Network for Padel Deals</span>
      <div class="flex flex-wrap items-center justify-center gap-x-2.5 gap-y-1">
        {links}
      </div>
    </div>
  </footer>
  <script src="https://unpkg.com/lucide@0.468.0/dist/umd/lucide.min.js" defer></script>
  <script>document.addEventListener('DOMContentLoaded', () => {{ if (window.lucide) lucide.createIcons(); }});</script>
</body>
</html>"""


def cta_box(lang: str, heading: str, body: str, wa_prefill: str) -> str:
    import urllib.parse
    wa_url = "https://wa.me/34680317486?text=" + urllib.parse.quote(wa_prefill)
    btn_txt = "Talk to Javier on WhatsApp" if lang == "en" else "Hablar con Javier por WhatsApp"
    return f"""    <div class="mt-12 bg-slate-50 border border-slate-300 rounded-2xl p-6 sm:p-8">
      <h3 class="font-heading font-black text-lg sm:text-xl text-slate-950 mb-2">{escape(heading)}</h3>
      <p class="text-xs sm:text-sm text-slate-600 mb-5 leading-relaxed font-normal">{escape(body)}</p>
      <div class="flex flex-col sm:flex-row gap-3">
        <a href="{wa_url}" target="_blank" rel="noopener" class="px-5 py-2.5 rounded-full bg-slate-950 hover:bg-slate-800 text-white font-heading font-bold text-xs uppercase tracking-wider text-center transition">
          {btn_txt}
        </a>
        <a href="mailto:javier@padelgree.com" class="px-5 py-2.5 rounded-full border border-slate-300 hover:border-slate-950 text-slate-950 font-heading font-bold text-xs uppercase tracking-wider text-center transition">
          javier@padelgree.com
        </a>
      </div>
    </div>"""
