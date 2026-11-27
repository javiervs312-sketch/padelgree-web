#!/usr/bin/env python3
"""Builds interactive B2B SEO/Lead-Magnet calculators (ES & EN) for Padelgree."""

from pathlib import Path
from _templates import build_head, build_header, build_footer, cta_box

ROOT = Path(__file__).resolve().parent


def write_page(rel: str, html: str):
    out = ROOT / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


def build_valuation_calc(lang: str):
    is_en = lang == "en"
    slug = "en/padel-club-valuation-calculator/" if is_en else "calculadora-valoracion-club-padel/"
    alt_slug = "calculadora-valoracion-club-padel/" if is_en else "en/padel-club-valuation-calculator/"
    canon = f"https://padelgree.com/{slug}"
    es_u = f"https://padelgree.com/calculadora-valoracion-club-padel/"
    en_u = f"https://padelgree.com/en/padel-club-valuation-calculator/"

    title = (
        "Free Padel Club Valuation Calculator (EBITDA Multiple & Asset Floor) | Padelgree"
        if is_en
        else "Calculadora Gratis: ¿Cuánto Vale tu Club de Pádel? (Múltiplo EBITDA) | Padelgree"
    )
    desc = (
        "Calculate the market valuation of any padel club in seconds using normalized EBITDA multiples (3.0x–5.8x), remaining warehouse lease tenure, court count, and asset replacement floor."
        if is_en
        else "Calcula gratis el valor real de venta o traspaso de tu club de pádel según su EBITDA anual, número de pistas, tipo de cubierta y años restantes de alquiler de nave."
    )
    h1 = (
        "Padel Club Valuation Calculator (EBITDA &amp; Assets)"
        if is_en
        else "Calculadora de Valoración de Clubes de Pádel"
    )
    intro = (
        "Estimate what corporate chains and institutional buyers actually pay in private M&amp;A transactions across Europe and the UK."
        if is_en
        else "Estima en 15 segundos el rango real de compraventa o traspaso que manejan hoy las cadenas y fondos por un club como el tuyo."
    )

    faqs = (
        [
            ("How does remaining lease length change club value?", "Under 5 remaining years compresses buyer multiples toward 2.5x–3.0x EBITDA or hardware salvage value. A 10–15 year lease unlocks 4.0x–5.5x multiples."),
            ("What if my club EBITDA is still ramping up?", "Asset replacement value (€22k–€30k per indoor panoramic court plus amortized civil fit-out) acts as the minimum valuation floor."),
        ]
        if is_en
        else [
            ("¿Cómo influyen los años restantes del alquiler en el valor del club?", "Con menos de 5 años de contrato, el múltiplo cae hacia 2,5x–3,0x EBITDA o valor de activos. Extender la nave a 10–15 años dispara el múltiplo a 4,0x–5,5x."),
            ("¿Qué pasa si el EBITDA actual es bajo por gestión mejorable?", "El suelo de valoración lo marca el valor de reposición de las pistas panorámicas (20k–30k€/pista) más la obra civil de solera y vestuarios ya ejecutada."),
        ]
    )

    graph = [
        {
            "@type": "WebApplication",
            "name": h1,
            "url": canon,
            "applicationCategory": "BusinessApplication",
            "operatingSystem": "All",
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in faqs
            ],
        },
    ]

    head = build_head(
        lang=lang,
        title=title,
        description=desc,
        canonical=canon,
        keywords="cuanto vale mi club de padel, tasacion club padel, padel club valuation calculator, valorar club padel ebitda",
        hreflang_es=es_u,
        hreflang_en=en_u,
        schema_graph=graph,
    )
    header = build_header(lang, f"/{alt_slug}")
    footer = build_footer(lang)

    lbl_courts = "Number of Courts" if is_en else "Número de Pistas"
    lbl_type = "Facility Type" if is_en else "Tipo de Instalación"
    lbl_ebitda = "Annual Normalized EBITDA (€)" if is_en else "EBITDA Anual Estimado (€/año)"
    lbl_lease = "Remaining Warehouse Lease (Years)" if is_en else "Años Restantes de Alquiler Nave"
    lbl_cond = "Courts &amp; Turf Condition" if is_en else "Estado de Pistas y Césped"
    lbl_est = "Estimated Market Valuation Range" if is_en else "Rango de Valoración Estimado en M&A"
    lbl_mult = "Estimated Multiple" if is_en else "Múltiplo Aplicable"
    lbl_floor = "Hardware Asset Floor" if is_en else "Suelo por Valor de Activos"
    lbl_cta = "Send this valuation in private to Javier" if is_en else "Enviar estimación en privado a Javier por WhatsApp"

    faqs_html = "\n".join(
        f'<div class="bg-white p-5 rounded-xl border border-slate-200">'
        f'<h3 class="font-heading font-bold text-slate-950 text-sm mb-1.5">{q}</h3>'
        f'<p class="text-xs text-slate-600 leading-relaxed">{a}</p></div>'
        for q, a in faqs
    )

    opt_type = (
        '<option value="indoor">Indoor Warehouse (&gt;8.5m height)</option>'
        '<option value="covered">Semi-covered / Canopy</option>'
        '<option value="outdoor">Outdoor Only</option>'
        if is_en
        else '<option value="indoor">Indoor en Nave (&gt;8,5m altura)</option>'
        '<option value="covered">Cubierta / Carpa</option>'
        '<option value="outdoor">Exterior (Outdoor)</option>'
    )
    opt_lease = (
        '<option value="short">Under 5 years remaining</option>'
        '<option value="mid" selected>5 to 9 years remaining</option>'
        '<option value="long">10+ years remaining</option>'
        '<option value="freehold">Freehold (Own the building/land)</option>'
        if is_en
        else '<option value="short">Menos de 5 años restantes</option>'
        '<option value="mid" selected>De 5 a 9 años restantes</option>'
        '<option value="long">10 o más años restantes</option>'
        '<option value="freehold">Nave / Suelo en propiedad</option>'
    )
    opt_cond = (
        '<option value="new">New / Panoramic &lt;2 years</option>'
        '<option value="good" selected>Good condition (2–5 years)</option>'
        '<option value="aged">Needs turf / LED renewal (&gt;5 years)</option>'
        if is_en
        else '<option value="new">Nuevas / Panorámicas &lt;2 años</option>'
        '<option value="good" selected>Buen estado (2–5 años)</option>'
        '<option value="aged">Requiere cambio de césped/LED (&gt;5 años)</option>'
    )

    body = f"""  <main class="max-w-4xl mx-auto px-4 sm:px-6 py-10 sm:py-14 flex-1">
    <nav class="flex items-center gap-2 text-xs text-slate-400 mb-6 font-mono">
      <a href="{"/en/" if is_en else "/"}" class="hover:text-slate-950 transition">{"Home" if is_en else "Inicio"}</a>
      <span>/</span>
      <span class="text-slate-900 font-bold">{"Valuation Calculator" if is_en else "Calculadora de Valoración"}</span>
    </nav>

    <div class="mb-8">
      <span class="text-xs font-mono font-bold tracking-widest text-slate-400 uppercase block mb-2">{"FREE M&A BENCHMARK TOOL" if is_en else "HERRAMIENTA GRATUITA M&A"}</span>
      <h1 class="font-heading font-black text-3xl sm:text-4xl lg:text-5xl text-slate-950 tracking-tight leading-tight mb-4">{h1}</h1>
      <p class="text-base text-slate-600 font-normal leading-relaxed">{intro}</p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
      <div class="lg:col-span-7 bg-white border border-slate-300 rounded-2xl p-6 space-y-4">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label for="vc-courts" class="block text-xs font-bold text-slate-700 mb-1.5">{lbl_courts}</label>
            <input id="vc-courts" type="number" min="1" max="30" value="8" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm font-bold text-slate-950 focus:outline-none focus:border-slate-950">
          </div>
          <div>
            <label for="vc-type" class="block text-xs font-bold text-slate-700 mb-1.5">{lbl_type}</label>
            <select id="vc-type" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm font-medium text-slate-950 focus:outline-none focus:border-slate-950">{opt_type}</select>
          </div>
        </div>

        <div>
          <label for="vc-ebitda" class="block text-xs font-bold text-slate-700 mb-1.5">{lbl_ebitda}</label>
          <input id="vc-ebitda" type="number" min="0" step="5000" value="180000" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm font-bold text-slate-950 focus:outline-none focus:border-slate-950">
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label for="vc-lease" class="block text-xs font-bold text-slate-700 mb-1.5">{lbl_lease}</label>
            <select id="vc-lease" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm font-medium text-slate-950 focus:outline-none focus:border-slate-950">{opt_lease}</select>
          </div>
          <div>
            <label for="vc-cond" class="block text-xs font-bold text-slate-700 mb-1.5">{lbl_cond}</label>
            <select id="vc-cond" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm font-medium text-slate-950 focus:outline-none focus:border-slate-950">{opt_cond}</select>
          </div>
        </div>
      </div>

      <div class="lg:col-span-5 bg-slate-950 text-white rounded-2xl p-6 space-y-5 border border-slate-900">
        <div>
          <span class="text-[11px] font-mono uppercase tracking-widest text-slate-400 block mb-1">{lbl_est}</span>
          <div id="vc-range" class="font-heading font-black text-2xl sm:text-3xl text-white tracking-tight">—</div>
        </div>
        <div class="grid grid-cols-2 gap-3 pt-4 border-t border-slate-800 text-xs">
          <div>
            <span class="text-slate-400 block mb-0.5">{lbl_mult}</span>
            <span id="vc-mult" class="font-mono font-bold text-base text-white">—</span>
          </div>
          <div>
            <span class="text-slate-400 block mb-0.5">{lbl_floor}</span>
            <span id="vc-floor" class="font-mono font-bold text-base text-white">—</span>
          </div>
        </div>
        <p id="vc-note" class="text-xs text-slate-300 leading-relaxed pt-2 border-t border-slate-800"></p>
        <a id="vc-wa" href="https://wa.me/34680317486" target="_blank" rel="noopener" class="block w-full text-center px-5 py-3 rounded-full bg-white hover:bg-slate-200 text-slate-950 font-heading font-bold text-xs uppercase tracking-wider transition">
          {lbl_cta} →
        </a>
      </div>
    </div>

    <div class="mt-12 pt-8 border-t border-slate-200">
      <h2 class="font-heading font-black text-xl text-slate-950 mb-4">{"FAQ" if is_en else "Preguntas Frecuentes"}</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">{faqs_html}</div>
    </div>
  </main>

  <script>
    function fmtEur(n) {{ return Math.round(n).toLocaleString('es-ES') + ' €'; }}
    function recalcVal() {{
      const courts = Math.max(1, parseInt(document.getElementById('vc-courts').value || '1', 10));
      const ftype = document.getElementById('vc-type').value;
      const ebitda = Math.max(0, parseFloat(document.getElementById('vc-ebitda').value || '0'));
      const lease = document.getElementById('vc-lease').value;
      const cond = document.getElementById('vc-cond').value;

      let lowM = 3.5, highM = 4.4;
      if (courts >= 8) {{ lowM += 0.4; highM += 0.5; }}
      else if (courts <= 4) {{ lowM -= 0.5; highM -= 0.5; }}

      if (ftype === 'indoor') {{ lowM += 0.2; highM += 0.3; }}
      else if (ftype === 'outdoor') {{ lowM -= 0.7; highM -= 0.7; }}

      if (lease === 'short') {{ lowM -= 1.0; highM -= 1.1; }}
      else if (lease === 'long') {{ lowM += 0.4; highM += 0.6; }}
      else if (lease === 'freehold') {{ lowM += 1.2; highM += 1.6; }}

      if (cond === 'new') {{ lowM += 0.2; highM += 0.2; }}
      else if (cond === 'aged') {{ lowM -= 0.3; highM -= 0.3; }}

      lowM = Math.max(2.0, lowM);
      highM = Math.max(lowM + 0.5, highM);

      const perCourt = ftype === 'indoor' ? 24000 : (ftype === 'covered' ? 20000 : 14000);
      const condFactor = cond === 'new' ? 0.9 : (cond === 'good' ? 0.72 : 0.45);
      const civilBonus = ftype === 'indoor' ? Math.min(180000, courts * 14000) : courts * 5000;
      const floorVal = courts * perCourt * condFactor + (lease === 'short' ? civilBonus * 0.35 : civilBonus);

      const lowVal = Math.max(floorVal, ebitda * lowM);
      const highVal = Math.max(floorVal * 1.18, ebitda * highM);

      document.getElementById('vc-range').innerText = fmtEur(lowVal) + ' – ' + fmtEur(highVal);
      document.getElementById('vc-mult').innerText = lowM.toFixed(1) + 'x – ' + highM.toFixed(1) + 'x';
      document.getElementById('vc-floor').innerText = fmtEur(floorVal);

      const isEn = {str(is_en).lower()};
      let note = '';
      if (lease === 'short') {{
        note = isEn
          ? 'Tip: Extending the warehouse lease above 10 years before going to market can lift exit valuation by 25%–35%.'
          : 'Clave: Si amplías el contrato de la nave a +10 años antes de salir a mercado, el múltiplo de venta sube un 25%–35%.';
      }} else if (courts >= 7 && ftype === 'indoor') {{
        note = isEn
          ? 'High institutional demand: 7+ court indoor clubs qualify for European multi-club operator buyouts.'
          : 'Alta demanda institucional: clubes indoor de 7+ pistas encajan con mandatos activos de cadenas compradoras.';
      }} else {{
        note = isEn
          ? 'Standard off-market private sale via blind teaser keeps member retention and staff stability at 100%.'
          : 'La venta confidencial mediante ficha ciega protege el 100% de tu masa social durante la negociación.';
      }}
      document.getElementById('vc-note').innerText = note;

      const waMsg = isEn
        ? `Hi Javier, from Padelgree Valuation Tool: ${{courts}} ${{ftype}} courts | EBITDA ${{fmtEur(ebitda)}} | Lease: ${{lease}} | Est: ${{fmtEur(lowVal)}} - ${{fmtEur(highVal)}}`
        : `Hola Javier, desde la Calculadora de Padelgree: ${{courts}} pistas (${{ftype}}) | EBITDA ${{fmtEur(ebitda)}} | Alquiler: ${{lease}} | Est: ${{fmtEur(lowVal)}} - ${{fmtEur(highVal)}}`;
      document.getElementById('vc-wa').href = 'https://wa.me/34680317486?text=' + encodeURIComponent(waMsg);
    }}
    ['vc-courts', 'vc-type', 'vc-ebitda', 'vc-lease', 'vc-cond'].forEach(id => {{
      document.getElementById(id).addEventListener('input', recalcVal);
      document.getElementById(id).addEventListener('change', recalcVal);
    }});
    recalcVal();
  </script>
{footer}"""
    write_page(f"{slug}index.html", head + "\n" + header + "\n" + body)


def build_warehouse_calc(lang: str):
    is_en = lang == "en"
    slug = "en/padel-warehouse-court-calculator/" if is_en else "calculadora-pistas-nave/"
    alt_slug = "calculadora-pistas-nave/" if is_en else "en/padel-warehouse-court-calculator/"
    canon = f"https://padelgree.com/{slug}"
    es_u = "https://padelgree.com/calculadora-pistas-nave/"
    en_u = "https://padelgree.com/en/padel-warehouse-court-calculator/"

    title = (
        "Padel Warehouse Court Fit-Out & Rent Calculator | Padelgree"
        if is_en
        else "Calculadora de Pistas de Pádel por m² de Nave Industrial | Padelgree"
    )
    desc = (
        "Check how many indoor padel courts fit inside your warehouse, verify ceiling height compliance (8.5m–11m), and estimate feasible institutional lease income."
        if is_en
        else "Calcula al instante cuántas pistas de pádel indoor caben en tu nave industrial, si cumple la altura mínima bajo viga y qué renta mensual puede pagar un operador."
    )
    h1 = (
        "Padel Warehouse Capacity &amp; Rent Calculator"
        if is_en
        else "Calculadora de Pistas de Pádel por Nave Industrial"
    )
    intro = (
        "Enter warehouse dimensions and clear eaves height to validate padel club feasibility and long-term lease potential."
        if is_en
        else "Introduce las dimensiones de tu nave y altura libre bajo viga para validar cuántas pistas caben y el alquiler orientativo para un operador."
    )

    graph = [{
        "@type": "WebApplication",
        "name": h1,
        "url": canon,
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "All",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
    }]

    head = build_head(
        lang=lang,
        title=title,
        description=desc,
        canonical=canon,
        keywords="cuantas pistas padel caben en una nave, altura minima nave padel, padel warehouse court calculator",
        hreflang_es=es_u,
        hreflang_en=en_u,
        schema_graph=graph,
    )
    header = build_header(lang, f"/{alt_slug}")
    footer = build_footer(lang)

    body = f"""  <main class="max-w-4xl mx-auto px-4 sm:px-6 py-10 sm:py-14 flex-1">
    <nav class="flex items-center gap-2 text-xs text-slate-400 mb-6 font-mono">
      <a href="{"/en/" if is_en else "/"}" class="hover:text-slate-950 transition">{"Home" if is_en else "Inicio"}</a>
      <span>/</span>
      <span class="text-slate-900 font-bold">{"Warehouse Court Calculator" if is_en else "Calculadora Pistas Nave"}</span>
    </nav>

    <div class="mb-8">
      <span class="text-xs font-mono font-bold tracking-widest text-slate-400 uppercase block mb-2">{"INDUSTRIAL REAL ESTATE FEASIBILITY" if is_en else "VIABILIDAD TÉCNICA DE NAVES"}</span>
      <h1 class="font-heading font-black text-3xl sm:text-4xl lg:text-5xl text-slate-950 tracking-tight leading-tight mb-4">{h1}</h1>
      <p class="text-base text-slate-600 font-normal leading-relaxed">{intro}</p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
      <div class="lg:col-span-7 bg-white border border-slate-300 rounded-2xl p-6 space-y-4">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label for="wc-len" class="block text-xs font-bold text-slate-700 mb-1.5">{"Warehouse Length (m)" if is_en else "Largo de la Nave (metros)"}</label>
            <input id="wc-len" type="number" min="20" max="200" value="60" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm font-bold text-slate-950 focus:outline-none focus:border-slate-950">
          </div>
          <div>
            <label for="wc-wid" class="block text-xs font-bold text-slate-700 mb-1.5">{"Warehouse Width (m)" if is_en else "Ancho de la Nave (metros)"}</label>
            <input id="wc-wid" type="number" min="12" max="150" value="46" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm font-bold text-slate-950 focus:outline-none focus:border-slate-950">
          </div>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label for="wc-h" class="block text-xs font-bold text-slate-700 mb-1.5">{"Clear Ceiling Height Under Beam (m)" if is_en else "Altura Libre Bajo Viga (metros)"}</label>
            <input id="wc-h" type="number" step="0.5" min="5" max="20" value="9.5" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm font-bold text-slate-950 focus:outline-none focus:border-slate-950">
          </div>
          <div>
            <label for="wc-market" class="block text-xs font-bold text-slate-700 mb-1.5">{"Market Pricing Zone" if is_en else "Zona / Mercado"}</label>
            <select id="wc-market" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm font-medium text-slate-950 focus:outline-none focus:border-slate-950">
              <option value="es_prime">{"Madrid / Barcelona" if is_en else "Madrid / Barcelona"}</option>
              <option value="es_sec">{"Spain Regional Cities" if is_en else "Resto Capitales España"}</option>
              <option value="eu_high">{"UK / Paris / Munich / Milan" if is_en else "Europa Prime (UK, París, Milán, Múnich)"}</option>
            </select>
          </div>
        </div>
      </div>

      <div class="lg:col-span-5 bg-slate-950 text-white rounded-2xl p-6 space-y-5">
        <div class="grid grid-cols-2 gap-3">
          <div>
            <span class="text-[11px] font-mono uppercase tracking-widest text-slate-400 block mb-1">{"Max Courts" if is_en else "Pistas Máximas"}</span>
            <div id="wc-courts" class="font-heading font-black text-3xl text-white">—</div>
          </div>
          <div>
            <span class="text-[11px] font-mono uppercase tracking-widest text-slate-400 block mb-1">{"Footprint" if is_en else "Superficie"}</span>
            <div id="wc-sqm" class="font-heading font-black text-2xl text-white pt-1">—</div>
          </div>
        </div>
        <div class="pt-4 border-t border-slate-800 space-y-2 text-xs">
          <div class="flex justify-between"><span class="text-slate-400">{"Height Grade:" if is_en else "Calificación Altura:"}</span><span id="wc-hstatus" class="font-bold text-white">—</span></div>
          <div class="flex justify-between"><span class="text-slate-400">{"Est. Operator Rent:" if is_en else "Renta Operador Est.:"}</span><span id="wc-rent" class="font-mono font-bold text-white">—</span></div>
        </div>
        <a id="wc-wa" href="https://wa.me/34680317486" target="_blank" rel="noopener" class="block w-full text-center px-5 py-3 rounded-full bg-white hover:bg-slate-200 text-slate-950 font-heading font-bold text-xs uppercase tracking-wider transition">
          {"Match warehouse with operators" if is_en else "Cruzar nave en privado con operadores"} →
        </a>
      </div>
    </div>
  </main>

  <script>
    function recalcWarehouse() {{
      const L = Math.max(10, parseFloat(document.getElementById('wc-len').value || '10'));
      const W = Math.max(10, parseFloat(document.getElementById('wc-wid').value || '10'));
      const H = Math.max(4, parseFloat(document.getElementById('wc-h').value || '4'));
      const mkt = document.getElementById('wc-market').value;
      const isEn = {str(is_en).lower()};

      const sqm = Math.round(L * W);
      // Reserve ~16% space for changing rooms, reception, and corridors; each court bay ~255 sqm (11.5 x 22m)
      const usableSqm = sqm * 0.84;
      const byArea = Math.floor(usableSqm / 255);
      // Also check orientation grids (20x10 + 1.5m corridor = 22x11.5m or rotated)
      const opt1 = Math.floor(L / 22.0) * Math.floor(W / 11.5);
      const opt2 = Math.floor(W / 22.0) * Math.floor(L / 11.5);
      const maxCourts = Math.max(0, Math.min(byArea, Math.max(opt1, opt2, Math.floor(usableSqm / 270))));

      let hMsg = '';
      if (H < 8.0) hMsg = isEn ? 'Too Low (<8m)' : 'Insuficiente (<8m)';
      else if (H < 8.5) hMsg = isEn ? 'Tight Minimum (8.0–8.5m)' : 'Mínimo Justo (8,0–8,5m)';
      else if (H < 10.0) hMsg = isEn ? 'Commercial Optimal (8.5–10m)' : 'Óptima Comercial (8,5–10m)';
      else hMsg = isEn ? 'FIP Competition Grade (10m+)' : 'Grado Competición FIP (10m+)';

      const rateSqm = mkt === 'eu_high' ? [7.0, 11.0] : (mkt === 'es_prime' ? [4.5, 6.8] : [3.2, 4.8]);
      const rLow = Math.round(sqm * rateSqm[0]);
      const rHigh = Math.round(sqm * rateSqm[1]);

      document.getElementById('wc-courts').innerText = maxCourts + (isEn ? ' courts' : ' pistas');
      document.getElementById('wc-sqm').innerText = sqm.toLocaleString('es-ES') + ' m²';
      document.getElementById('wc-hstatus').innerText = hMsg;
      document.getElementById('wc-rent').innerText = rLow.toLocaleString('es-ES') + ' – ' + rHigh.toLocaleString('es-ES') + ' €/mes';

      const waMsg = isEn
        ? `Hi Javier, checking warehouse feasibility on Padelgree: ${{sqm}} sqm (${{L}}x${{W}}m) | Clear height: ${{H}}m | Est capacity: ${{maxCourts}} courts.`
        : `Hola Javier, desde Calculadora Pistas Nave Padelgree: ${{sqm}} m² (${{L}}x${{W}}m) | Altura libre: ${{H}}m | Capacidad est: ${{maxCourts}} pistas.`;
      document.getElementById('wc-wa').href = 'https://wa.me/34680317486?text=' + encodeURIComponent(waMsg);
    }}
    ['wc-len', 'wc-wid', 'wc-h', 'wc-market'].forEach(id => {{
      document.getElementById(id).addEventListener('input', recalcWarehouse);
      document.getElementById(id).addEventListener('change', recalcWarehouse);
    }});
    recalcWarehouse();
  </script>
{footer}"""
    write_page(f"{slug}index.html", head + "\n" + header + "\n" + body)


def main():
    build_valuation_calc("es")
    build_valuation_calc("en")
    build_warehouse_calc("es")
    build_warehouse_calc("en")
    print("Built 4 interactive B2B calculators (ES + EN)")


if __name__ == "__main__":
    main()
