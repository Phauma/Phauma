"""
Portafolio Dividendero Chileno
Datos extraídos de pantallas del broker al 09/06/2026.
Dividend yields históricos 2021-2025 según reportes CMF / Bolsa de Santiago.
2026 = estimado parcial al cierre del semestre.
"""

import json
from datetime import date

# ---------------------------------------------------------------------------
# 1. DATOS DEL PORTAFOLIO
#    - "acciones": de pantalla de detalle individual donde disponible,
#      de lo contrario, de la vista de lista del portafolio.
#    - "invertido_clp": costo histórico total según app.
#    - "valor_actual_clp": precio × acciones al 09/06/2026.
# ---------------------------------------------------------------------------

TPM_ACTUAL = 5.00          # Tasa Política Monetaria BCCh al cierre 2025 (%)
TPM_PROMEDIO_5A = 6.40     # Promedio TPM 2021-2025 (%)
UF_HOY = 38_840            # UF aproximada junio 2026 (CLP)

PORTAFOLIO = [
    {
        "simbolo": "ANDINA-B",
        "empresa": "Embotelladora Andina S.A.",
        "sector": "Consumo Básico",
        "acciones": 400,
        "precio_clp": 3_498.7,
        "invertido_clp": 725_998,
        "valor_actual_clp": 1_399_480,
        "rentabilidad_pct": 93.66,
        # Dividend yield histórico anual (%) — dividendo pagado / precio promedio año
        "dy": {2021: 5.5, 2022: 6.8, 2023: 5.2, 2024: 6.0, 2025: 5.4, 2026: 6.5},
        "payout_pct": 75,        # % de utilidades distribuidas
        "frecuencia_pago": "Semestral",
        "ipsa": True,
        "consistencia_anos": 20,  # años consecutivos pagando dividendo
        "notas": "Una de las pagadoras más consistentes del mercado local.",
    },
    {
        "simbolo": "COLBUN",
        "empresa": "Colbún S.A.",
        "sector": "Utilities",
        "acciones": 5_900,
        "precio_clp": 127,
        "invertido_clp": 658_540,
        "valor_actual_clp": 749_300,
        "rentabilidad_pct": 14.08,
        "dy": {2021: 2.5, 2022: 4.2, 2023: 3.1, 2024: 3.5, 2025: 2.8, 2026: 3.0},
        "payout_pct": 50,
        "frecuencia_pago": "Anual",
        "ipsa": True,
        "consistencia_anos": 10,
        "notas": "Dividend variable según resultados hidrológicos y ERNC.",
    },
    {
        "simbolo": "ENELCHILE",
        "empresa": "Enel Chile S.A.",
        "sector": "Utilities",
        "acciones": 20_000,
        "precio_clp": 76,
        "invertido_clp": 944_574,
        "valor_actual_clp": 1_520_000,
        "rentabilidad_pct": 57.93,
        "dy": {2021: 5.3, 2022: 4.8, 2023: 3.9, 2024: 4.5, 2025: 3.6, 2026: 4.0},
        "payout_pct": 70,
        "frecuencia_pago": "Anual",
        "ipsa": True,
        "consistencia_anos": 15,
        "notas": "Política de dividendo mínimo garantizado vía estatutos Enel Group.",
    },
    {
        "simbolo": "HABITAT",
        "empresa": "AFP Habitat S.A.",
        "sector": "Servicios Financieros",
        "acciones": 1_500,
        "precio_clp": 1_350.6,
        "invertido_clp": 822_857,
        "valor_actual_clp": 2_025_900,
        "rentabilidad_pct": 146.25,
        "dy": {2021: 9.0, 2022: 10.5, 2023: 11.2, 2024: 12.8, 2025: 13.5, 2026: 12.0},
        "payout_pct": 90,
        "frecuencia_pago": "Anual",
        "ipsa": False,
        "consistencia_anos": 18,
        "notas": "AFP con alta distribución; yield entre los más altos del mercado chileno.",
    },
    {
        "simbolo": "LTM",
        "empresa": "Latam Airlines Group S.A.",
        "sector": "Industrial (Aerolíneas)",
        "acciones": 130_000,
        "precio_clp": 22.61,
        "invertido_clp": 1_405_169,
        "valor_actual_clp": 2_939_300,
        "rentabilidad_pct": 102.61,
        "dy": {2021: 0.0, 2022: 0.0, 2023: 1.0, 2024: 2.5, 2025: 3.2, 2026: 3.5},
        "payout_pct": 30,
        "frecuencia_pago": "Anual",
        "ipsa": True,
        "consistencia_anos": 3,
        "notas": "Reemergió de quiebra en 2022; dividendo en proceso de normalización.",
    },
    {
        "simbolo": "PROVIDA",
        "empresa": "Administradora de Fondos de Pensiones Provida S.A.",
        "sector": "Servicios Financieros",
        "acciones": 600,
        "precio_clp": 5_035.1,
        "invertido_clp": 1_270_496,
        "valor_actual_clp": 3_021_060,
        "rentabilidad_pct": 138.68,
        "dy": {2021: 10.5, 2022: 12.0, 2023: 14.5, 2024: 16.8, 2025: 15.2, 2026: 14.5},
        "payout_pct": 95,
        "frecuencia_pago": "Semestral",
        "ipsa": False,
        "consistencia_anos": 22,
        "notas": "Controlada por MetLife; distribución casi total de utilidades. Mejor yield del portafolio.",
    },
    {
        "simbolo": "SOQUICOM",
        "empresa": "Soquimich Comercial S.A.",
        "sector": "Commodities (Minería)",
        "acciones": 2_500,
        "precio_clp": 374.32,
        "invertido_clp": 731_039,
        "valor_actual_clp": 935_800,
        "rentabilidad_pct": 29.36,
        "dy": {2021: 3.8, 2022: 4.5, 2023: 4.0, 2024: 3.8, 2025: 3.5, 2026: 3.2},
        "payout_pct": 55,
        "frecuencia_pago": "Anual",
        "ipsa": False,
        "consistencia_anos": 12,
        "notas": "Compañía relacionada al grupo SQM; dividendo estable y moderado.",
    },
    {
        "simbolo": "VAPORES",
        "empresa": "Compañía Sud Americana de Vapores S.A.",
        "sector": "Industrial (Naviero)",
        "acciones": 11_000,
        "precio_clp": 43,
        "invertido_clp": 813_233,
        "valor_actual_clp": 473_000,
        "rentabilidad_pct": -41.68,
        "dy": {2021: 8.5, 2022: 44.0, 2023: 5.2, 2024: 1.8, 2025: 1.2, 2026: 0.8},
        "payout_pct": 30,
        "frecuencia_pago": "Anual",
        "ipsa": True,
        "consistencia_anos": 4,
        "notas": "Superciclo naviero 2022 generó dividendo extraordinario ~44%. Ahora normalizado.",
    },
    {
        "simbolo": "SQM-B",
        "empresa": "Sociedad Química y Minera de Chile S.A.",
        "sector": "Commodities (Litio/Minería)",
        "acciones": 60,
        "precio_clp": 69_065,
        "invertido_clp": None,
        "valor_actual_clp": 4_143_900,
        "rentabilidad_pct": None,
        "dy": {2021: 5.2, 2022: 18.5, 2023: 9.5, 2024: 4.2, 2025: 3.5, 2026: 3.8},
        "payout_pct": 80,
        "frecuencia_pago": "Semestral",
        "ipsa": True,
        "consistencia_anos": 15,
        "notas": "Boom del litio 2022. Dividendo cíclico ligado al precio del litio.",
    },
    {
        "simbolo": "FALABELLA",
        "empresa": "S.A.C.I. Falabella",
        "sector": "Consumo Discrecional (Retail)",
        "acciones": 7,
        "precio_clp": 5_740,
        "invertido_clp": None,
        "valor_actual_clp": 40_180,
        "rentabilidad_pct": None,
        "dy": {2021: 1.8, 2022: 0.5, 2023: 0.0, 2024: 0.8, 2025: 1.5, 2026: 1.8},
        "payout_pct": 30,
        "frecuencia_pago": "Anual",
        "ipsa": True,
        "consistencia_anos": 2,
        "notas": "Suspendió dividendo en 2023 por pérdidas operacionales. Recuperación gradual.",
    },
    {
        "simbolo": "QUINENCO",
        "empresa": "Quinenco S.A.",
        "sector": "Holding Diversificado",
        "acciones": 81,
        "precio_clp": 3_800,
        "invertido_clp": None,
        "valor_actual_clp": 307_800,
        "rentabilidad_pct": None,
        "dy": {2021: 3.5, 2022: 4.2, 2023: 4.0, 2024: 4.8, 2025: 4.5, 2026: 4.5},
        "payout_pct": 60,
        "frecuencia_pago": "Anual",
        "ipsa": True,
        "consistencia_anos": 16,
        "notas": "Holding del Grupo Luksic. Dividendo estable y creciente.",
    },
    {
        "simbolo": "CFINRENTAS",
        "empresa": "CF Rentas Inmobiliarias S.A.",
        "sector": "Real Estate (REIT local)",
        "acciones": 378,
        "precio_clp": 2_195.22,
        "invertido_clp": None,
        "valor_actual_clp": 829_793,
        "rentabilidad_pct": None,
        "dy": {2021: 5.8, 2022: 6.5, 2023: 7.2, 2024: 7.8, 2025: 8.0, 2026: 7.5},
        "payout_pct": 85,
        "frecuencia_pago": "Trimestral",
        "ipsa": False,
        "consistencia_anos": 8,
        "notas": "Estructura tipo REIT chilena. Alta distribución trimestral; único en su clase en este portafolio.",
    },
    {
        "simbolo": "CENCOSUD",
        "empresa": "Cencosud S.A.",
        "sector": "Consumo Discrecional (Retail)",
        "acciones": 2,
        "precio_clp": 2_105,
        "invertido_clp": None,
        "valor_actual_clp": 4_210,
        "rentabilidad_pct": None,
        "dy": {2021: 2.8, 2022: 3.5, 2023: 3.0, 2024: 3.8, 2025: 3.2, 2026: 3.5},
        "payout_pct": 45,
        "frecuencia_pago": "Anual",
        "ipsa": True,
        "consistencia_anos": 12,
        "notas": "Posición muy pequeña (2 acciones). Considerar ampliar o consolidar.",
    },
    {
        "simbolo": "LIPIGAS",
        "empresa": "Empresas Lipigas S.A.",
        "sector": "Utilities (Gas Distribución)",
        "acciones": 44,
        "precio_clp": 8_439.6,
        "invertido_clp": None,
        "valor_actual_clp": 371_342,
        "rentabilidad_pct": None,
        "dy": {2021: 5.0, 2022: 5.8, 2023: 6.2, 2024: 6.8, 2025: 6.0, 2026: 6.5},
        "payout_pct": 70,
        "frecuencia_pago": "Semestral",
        "ipsa": False,
        "consistencia_anos": 14,
        "notas": "Distribución regulada de gas, flujo estable y predecible.",
    },
]

# ---------------------------------------------------------------------------
# 2. MÉTRICAS CALCULADAS
# ---------------------------------------------------------------------------

ANOS_HISTORICOS = [2021, 2022, 2023, 2024, 2025, 2026]

def calcular_metricas(stock):
    dy = stock["dy"]
    dy_promedio = sum(dy.values()) / len(dy)
    dy_actual = dy.get(2026, dy.get(2025, 0))

    # Yield on Cost (YOC): dividendo recibido sobre precio de compra
    if stock["invertido_clp"] and stock["acciones"]:
        precio_compra_promedio = stock["invertido_clp"] / stock["acciones"]
        yoc = (dy_actual / 100) * stock["precio_clp"] / precio_compra_promedio * 100
    else:
        yoc = None

    # Prima / descuento vs TPM
    spread_tpm = dy_actual - TPM_ACTUAL

    # Tendencia: positiva si 2024 > 2021
    tendencia = "↑" if dy.get(2025, 0) > dy.get(2021, 0) else "↓"

    return {
        "dy_promedio_5a": round(dy_promedio, 2),
        "dy_actual_2026": round(dy_actual, 2),
        "yoc": round(yoc, 2) if yoc else None,
        "spread_vs_tpm": round(spread_tpm, 2),
        "tendencia_dy": tendencia,
    }


for s in PORTAFOLIO:
    s["metricas"] = calcular_metricas(s)

# ---------------------------------------------------------------------------
# 3. RESUMEN DEL PORTAFOLIO
# ---------------------------------------------------------------------------

valor_total = sum(s["valor_actual_clp"] for s in PORTAFOLIO)
invertido_total = sum(s["invertido_clp"] for s in PORTAFOLIO if s["invertido_clp"])

# Dividend yield ponderado por valor de mercado
dy_ponderado = sum(
    s["metricas"]["dy_actual_2026"] * s["valor_actual_clp"]
    for s in PORTAFOLIO
) / valor_total

resumen = {
    "fecha": str(date(2026, 6, 9)),
    "valor_portafolio_clp": round(valor_total),
    "valor_portafolio_uf": round(valor_total / UF_HOY, 2),
    "invertido_parcial_clp": round(invertido_total),
    "num_posiciones": len(PORTAFOLIO),
    "dy_ponderado_pct": round(dy_ponderado, 2),
    "tpm_bccch_pct": TPM_ACTUAL,
    "spread_portafolio_vs_tpm": round(dy_ponderado - TPM_ACTUAL, 2),
}

# ---------------------------------------------------------------------------
# 4. GENERACIÓN HTML
# ---------------------------------------------------------------------------

def color_dy(val):
    if val >= 8:
        return "#00c853"
    elif val >= 5:
        return "#64dd17"
    elif val >= 3:
        return "#ffd600"
    elif val >= 1:
        return "#ff6d00"
    else:
        return "#d50000"

def color_rent(val):
    if val is None:
        return "#888"
    return "#00c853" if val >= 0 else "#d50000"

def fmt_clp(val):
    if val is None:
        return "—"
    return f"${val:,.0f}".replace(",", ".")

def fmt_pct(val, decimals=1):
    if val is None:
        return "—"
    sign = "+" if val > 0 else ""
    return f"{sign}{val:.{decimals}f}%"

ANCHO_TABLA = 100

html_rows_dy = ""
for s in PORTAFOLIO:
    dy = s["dy"]
    m = s["metricas"]
    pesos_col = s["valor_actual_clp"] / valor_total * 100

    dy_cells = "".join(
        f'<td style="color:{color_dy(dy.get(a,0))};font-weight:bold">'
        f'{dy.get(a,"—"):.1f}%</td>'
        for a in ANOS_HISTORICOS
    )
    yoc_str = f'{m["yoc"]:.1f}%' if m["yoc"] else "—"
    ipsa_badge = '<span style="background:#1565c0;padding:1px 5px;border-radius:3px;font-size:10px">IPSA</span>' if s["ipsa"] else ""

    html_rows_dy += f"""
    <tr>
      <td><b>{s['simbolo']}</b> {ipsa_badge}<br>
          <small style="color:#aaa">{s['sector']}</small></td>
      <td style="text-align:right">{s['acciones']:,}</td>
      <td style="text-align:right">{fmt_clp(s['precio_clp'])}</td>
      <td style="text-align:right">{fmt_clp(s['valor_actual_clp'])}</td>
      <td style="text-align:right">{fmt_clp(s['invertido_clp'])}</td>
      <td style="text-align:right;color:{color_rent(s['rentabilidad_pct'])}">{fmt_pct(s['rentabilidad_pct'])}</td>
      {dy_cells}
      <td style="text-align:right;color:{color_dy(m['dy_promedio_5a'])};font-weight:bold">{m['dy_promedio_5a']:.1f}%</td>
      <td style="text-align:right">{yoc_str}</td>
      <td style="text-align:right;color:{'#00c853' if m['spread_vs_tpm']>0 else '#d50000'}">{fmt_pct(m['spread_vs_tpm'])}</td>
      <td style="text-align:right">{m['tendencia_dy']}</td>
      <td style="text-align:right">{s['consistencia_anos']} años</td>
      <td style="text-align:right">{s['payout_pct']}%</td>
      <td style="text-align:right">{s['frecuencia_pago']}</td>
      <td style="text-align:right">{pesos_col:.1f}%</td>
    </tr>"""

# Totales / promedios
html_rows_dy += f"""
    <tr style="background:#1a237e;font-weight:bold;font-size:14px">
      <td colspan="3">TOTALES / PONDERADO</td>
      <td style="text-align:right">{fmt_clp(valor_total)}</td>
      <td style="text-align:right">{fmt_clp(invertido_total)} *</td>
      <td colspan="8"></td>
      <td style="text-align:right;color:{color_dy(dy_ponderado)}">{dy_ponderado:.2f}%</td>
      <td colspan="4"></td>
    </tr>"""

# Sector breakdown
sector_map: dict = {}
for s in PORTAFOLIO:
    sec = s["sector"].split(" ")[0]
    sector_map[sec] = sector_map.get(sec, 0) + s["valor_actual_clp"]

sector_html = "".join(
    f'<div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #333">'
    f'<span>{sec}</span><span>{v/valor_total*100:.1f}%  ({fmt_clp(v)})</span></div>'
    for sec, v in sorted(sector_map.items(), key=lambda x: -x[1])
)

html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Portafolio Dividendero Chile — {resumen['fecha']}</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ background: #0d0d1a; color: #e0e0e0; font-family: 'Segoe UI', Arial, sans-serif; padding: 20px; }}
    h1 {{ color: #90caf9; font-size: 22px; margin-bottom: 4px; }}
    h2 {{ color: #7c4dff; font-size: 16px; margin: 20px 0 8px; }}
    .subtitle {{ color: #888; font-size: 13px; margin-bottom: 20px; }}
    .kpi-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 24px; }}
    .kpi {{ background: #1a1a2e; border: 1px solid #2d2d5e; border-radius: 8px; padding: 14px; }}
    .kpi-label {{ color: #888; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; }}
    .kpi-value {{ font-size: 22px; font-weight: bold; margin-top: 4px; }}
    .kpi-sub {{ font-size: 11px; color: #aaa; margin-top: 2px; }}
    .green {{ color: #00c853; }}
    .red {{ color: #d50000; }}
    .yellow {{ color: #ffd600; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 12px; }}
    th {{ background: #1a1a2e; color: #90caf9; padding: 8px 6px; text-align: center; position: sticky; top: 0; border-bottom: 2px solid #3d3d7a; white-space: nowrap; }}
    td {{ padding: 7px 6px; border-bottom: 1px solid #1f1f3a; vertical-align: middle; }}
    tr:hover {{ background: #161630; }}
    .scroll-wrap {{ overflow-x: auto; border-radius: 8px; border: 1px solid #2d2d5e; }}
    .note-box {{ background: #1a1a2e; border-left: 3px solid #7c4dff; padding: 10px 14px; margin: 8px 0; font-size: 12px; color: #ccc; border-radius: 4px; }}
    .sector-box {{ background: #1a1a2e; border: 1px solid #2d2d5e; border-radius: 8px; padding: 14px; max-width: 420px; font-size: 13px; }}
    .legend {{ display: flex; gap: 12px; flex-wrap: wrap; margin: 8px 0 16px; font-size: 11px; }}
    .leg-item {{ display: flex; align-items: center; gap: 4px; }}
    .leg-dot {{ width: 10px; height: 10px; border-radius: 50%; }}
    .footer {{ color: #555; font-size: 11px; margin-top: 24px; border-top: 1px solid #222; padding-top: 12px; }}
  </style>
</head>
<body>
  <h1>Portafolio Dividendero Chile</h1>
  <div class="subtitle">Datos al {resumen['fecha']} · {resumen['num_posiciones']} posiciones · Fuente: broker personal + CMF/Bolsa de Santiago</div>

  <!-- KPIs -->
  <div class="kpi-grid">
    <div class="kpi">
      <div class="kpi-label">Valor Total Portafolio</div>
      <div class="kpi-value green">{fmt_clp(resumen['valor_portafolio_clp'])}</div>
      <div class="kpi-sub">{resumen['valor_portafolio_uf']:,.1f} UF</div>
    </div>
    <div class="kpi">
      <div class="kpi-label">Invertido Conocido *</div>
      <div class="kpi-value">{fmt_clp(resumen['invertido_parcial_clp'])}</div>
      <div class="kpi-sub">Posiciones con costo de adquisición</div>
    </div>
    <div class="kpi">
      <div class="kpi-label">DY Ponderado Portafolio</div>
      <div class="kpi-value green">{resumen['dy_ponderado_pct']:.2f}%</div>
      <div class="kpi-sub">Weighted avg por valor de mercado</div>
    </div>
    <div class="kpi">
      <div class="kpi-label">TPM BCCh</div>
      <div class="kpi-value yellow">{resumen['tpm_bccch_pct']:.2f}%</div>
      <div class="kpi-sub">Tasa de referencia libre de riesgo</div>
    </div>
    <div class="kpi">
      <div class="kpi-label">Spread vs TPM</div>
      <div class="kpi-value {'green' if resumen['spread_portafolio_vs_tpm']>=0 else 'red'}">{fmt_pct(resumen['spread_portafolio_vs_tpm'])}</div>
      <div class="kpi-sub">Prima del portafolio sobre tasa libre riesgo</div>
    </div>
    <div class="kpi">
      <div class="kpi-label">Posiciones con DY &gt; TPM</div>
      <div class="kpi-value green">{sum(1 for s in PORTAFOLIO if s['metricas']['dy_actual_2026'] > TPM_ACTUAL)} / {len(PORTAFOLIO)}</div>
      <div class="kpi-sub">Batiendo tasa libre de riesgo actual</div>
    </div>
  </div>

  <div class="legend">
    <b style="font-size:12px">DY Color:</b>
    <div class="leg-item"><div class="leg-dot" style="background:#00c853"></div> ≥8% Excelente</div>
    <div class="leg-item"><div class="leg-dot" style="background:#64dd17"></div> ≥5% Muy bueno</div>
    <div class="leg-item"><div class="leg-dot" style="background:#ffd600"></div> ≥3% Aceptable</div>
    <div class="leg-item"><div class="leg-dot" style="background:#ff6d00"></div> ≥1% Bajo</div>
    <div class="leg-item"><div class="leg-dot" style="background:#d50000"></div> &lt;1% Sin dividendo</div>
  </div>

  <h2>Tabla Principal — Dividend Yield Histórico 2021–2026</h2>
  <div class="scroll-wrap">
    <table>
      <thead>
        <tr>
          <th>Empresa</th>
          <th>Acciones</th>
          <th>Precio CLP</th>
          <th>Valor Mercado</th>
          <th>Invertido</th>
          <th>Rentab. Total</th>
          <th>DY 2021</th>
          <th>DY 2022</th>
          <th>DY 2023</th>
          <th>DY 2024</th>
          <th>DY 2025</th>
          <th>DY 2026E</th>
          <th>DY Prom 5a</th>
          <th>YOC</th>
          <th>Spread TPM</th>
          <th>Tendencia</th>
          <th>Consistencia</th>
          <th>Payout %</th>
          <th>Frecuencia</th>
          <th>% Portafolio</th>
        </tr>
      </thead>
      <tbody>
        {html_rows_dy}
      </tbody>
    </table>
  </div>

  <p style="font-size:11px;color:#666;margin-top:6px">* El costo de adquisición solo está disponible para las posiciones con pantalla de detalle individual.</p>

  <!-- Notas por empresa -->
  <h2>Notas por Empresa</h2>
  {"".join(f'<div class="note-box"><b>{s["simbolo"]}</b> — {s["notas"]}</div>' for s in PORTAFOLIO)}

  <!-- Distribución sectorial -->
  <h2>Distribución Sectorial (por valor de mercado)</h2>
  <div class="sector-box">
    {sector_html}
    <div style="display:flex;justify-content:space-between;padding:6px 0;font-weight:bold;color:#90caf9;margin-top:4px">
      <span>TOTAL</span><span>{fmt_clp(valor_total)}</span>
    </div>
  </div>

  <!-- Variables estratégicas -->
  <h2>Variables Clave para Estrategia Dividendera Chilena</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:12px;margin-bottom:16px">

    <div class="kpi" style="font-size:12px">
      <div class="kpi-label">TPM vs DY Portafolio</div>
      <div style="margin-top:8px">
        <div>TPM BCCh: <b class="yellow">{TPM_ACTUAL}%</b></div>
        <div>DY ponderado portafolio: <b class="green">{resumen['dy_ponderado_pct']:.2f}%</b></div>
        <div>Spread: <b class="green">+{resumen['spread_portafolio_vs_tpm']:.2f}%</b></div>
        <div style="margin-top:6px;color:#aaa">El spread positivo justifica el riesgo de renta variable sobre instrumentos de renta fija.</div>
      </div>
    </div>

    <div class="kpi" style="font-size:12px">
      <div class="kpi-label">Ley de Dividendo Mínimo</div>
      <div style="margin-top:8px;color:#ccc">
        En Chile, la Ley N°18.046 obliga a las SA abiertas a distribuir al menos el <b>30% de sus utilidades netas</b>.
        Esto genera un piso de dividendo garantizado para todas las empresas rentables del portafolio.<br><br>
        <b>AFPs (HABITAT, PROVIDA)</b> típicamente distribuyen &gt;90% por política corporativa.
      </div>
    </div>

    <div class="kpi" style="font-size:12px">
      <div class="kpi-label">Tributación Dividendos Chile</div>
      <div style="margin-top:8px;color:#ccc">
        <b>Crédito fiscal:</b> Dividendos llevan crédito por impuesto de primera categoría (27%).<br>
        <b>Inversores locales:</b> Impuesto Global Complementario con crédito.<br>
        <b>Inversores extranjeros:</b> 35% retención menos crédito → tasa efectiva ~8%.<br>
        <b>FIP / Fondos:</b> Régimen especial de transparencia tributaria.
      </div>
    </div>

    <div class="kpi" style="font-size:12px">
      <div class="kpi-label">Yield on Cost (YOC)</div>
      <div style="margin-top:8px;color:#ccc">
        Mide el rendimiento real sobre TU precio de compra, no sobre el precio actual.
        Una acción comprada barata con DY bajo actual puede tener YOC excelente.<br><br>
        <b>Mejor YOC estimado:</b> PROVIDA (~30%+), HABITAT (~25%+), ENELCHILE (~8%).
      </div>
    </div>

    <div class="kpi" style="font-size:12px">
      <div class="kpi-label">Riesgo de Corte de Dividendo</div>
      <div style="margin-top:8px;color:#ccc">
        <span class="red">Alto:</span> LTM (aerolínea, histórico inestable), VAPORES (cíclico), FALABELLA (retail en reestructuración)<br>
        <span class="yellow">Medio:</span> SQM-B (ligado al litio), COLBUN (hidrología)<br>
        <span class="green">Bajo:</span> PROVIDA, HABITAT, ANDINA-B, LIPIGAS, CFINRENTAS
      </div>
    </div>

    <div class="kpi" style="font-size:12px">
      <div class="kpi-label">Ciclo Electoral y Riesgo Regulatorio</div>
      <div style="margin-top:8px;color:#ccc">
        Chile 2025: Nueva constitución descartada → riesgo regulatorio disminuido.<br>
        <b>Utilities (ENELCHILE, COLBUN, LIPIGAS):</b> Sujetas a regulación CNE/SEC.<br>
        <b>AFPs (HABITAT, PROVIDA):</b> Exposición a reforma previsional en curso.<br>
        <b>Minería (SQM-B):</b> Renegociación contrato Corfo hasta 2030.
      </div>
    </div>

  </div>

  <div class="footer">
    Generado el {date.today()} · Dividend yields históricos basados en datos CMF/Bolsa de Santiago.
    2026E = estimado a la fecha de corte. Precios al 09/06/2026.
    Este documento es solo para seguimiento personal y no constituye asesoría financiera.
    Verificar siempre en <a href="https://www.cmfchile.cl" style="color:#90caf9">cmfchile.cl</a> y
    <a href="https://www.bolsadesantiago.com" style="color:#90caf9">bolsadesantiago.com</a>.
  </div>
</body>
</html>
"""

# Guardar HTML
output_path = "portafolio_dividendos_chile.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"HTML generado: {output_path}")
print(f"\n{'='*60}")
print(f"RESUMEN PORTAFOLIO AL {resumen['fecha']}")
print(f"{'='*60}")
print(f"Valor total:            {fmt_clp(resumen['valor_portafolio_clp'])}  ({resumen['valor_portafolio_uf']:.0f} UF)")
print(f"Invertido (conocido):   {fmt_clp(resumen['invertido_parcial_clp'])}")
print(f"DY ponderado 2026E:     {resumen['dy_ponderado_pct']:.2f}%")
print(f"TPM BCCh:               {resumen['tpm_bccch_pct']:.2f}%")
print(f"Spread vs TPM:          +{resumen['spread_portafolio_vs_tpm']:.2f}%")
print(f"\n{'Empresa':<15} {'Acciones':>10} {'Valor CLP':>14} {'DY 2026E':>10} {'YOC':>8} {'Spread':>8} {'Consistencia':>13}")
print("-"*80)
for s in sorted(PORTAFOLIO, key=lambda x: -x["metricas"]["dy_actual_2026"]):
    m = s["metricas"]
    yoc_str = f'{m["yoc"]:.1f}%' if m["yoc"] else "  —"
    print(f"{s['simbolo']:<15} {s['acciones']:>10,} {fmt_clp(s['valor_actual_clp']):>14} "
          f"{m['dy_actual_2026']:>8.1f}% {yoc_str:>8} "
          f"{fmt_pct(m['spread_vs_tpm']):>8} {s['consistencia_anos']:>10} años")
print(f"\n* Fuente DY: CMF / Bolsa de Santiago / reportes anuales. 2026E = estimado.")
