import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Simulator Kebijakan Ekonomi",
    page_icon="🧭",
    layout="wide",
)


st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap');

:root {
    --bg: #09090f;
    --panel: rgba(255, 255, 255, 0.075);
    --panel-2: rgba(255, 255, 255, 0.115);
    --line: rgba(255, 255, 255, 0.135);
    --text: #f8fafc;
    --muted: #a1a1aa;
    --orange: #fb923c;
    --yellow: #facc15;
    --pink: #ec4899;
    --green: #34d399;
    --red: #fb7185;
    --cyan: #22d3ee;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.stApp {
    color: var(--text);
    background:
        radial-gradient(circle at 15% 8%, rgba(251, 146, 60, 0.28), transparent 28%),
        radial-gradient(circle at 82% 10%, rgba(236, 72, 153, 0.22), transparent 30%),
        radial-gradient(circle at 60% 95%, rgba(34, 211, 238, 0.13), transparent 35%),
        linear-gradient(145deg, #07070c 0%, #101018 48%, #09090f 100%);
}

.block-container {
    max-width: 1420px;
    padding-top: 1.2rem;
    padding-bottom: 2.4rem;
}

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

.main-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    padding: 16px 18px;
    margin-bottom: 18px;
    border: 1px solid var(--line);
    border-radius: 24px;
    background: rgba(255, 255, 255, 0.055);
    backdrop-filter: blur(18px);
    box-shadow: 0 20px 60px rgba(0,0,0,.22);
}

.nav-left {
    display: flex;
    align-items: center;
    gap: 13px;
}

.nav-logo {
    width: 46px;
    height: 46px;
    display: grid;
    place-items: center;
    border-radius: 16px;
    color: #160b05;
    font-weight: 900;
    font-size: 22px;
    background: linear-gradient(135deg, var(--yellow), var(--orange));
    box-shadow: 0 12px 34px rgba(251,146,60,.25);
}

.nav-title {
    color: white;
    font-size: 17px;
    font-weight: 900;
    line-height: 1.1;
}

.nav-subtitle {
    color: var(--muted);
    font-size: 12px;
    margin-top: 2px;
}

.nav-badge {
    padding: 11px 15px;
    border-radius: 999px;
    font-size: 12px;
    color: #fef3c7;
    font-weight: 800;
    border: 1px solid rgba(250,204,21,.26);
    background: rgba(250,204,21,.10);
}

.hero-shell {
    position: relative;
    overflow: hidden;
    min-height: 335px;
    padding: 34px;
    margin-bottom: 22px;
    border-radius: 34px;
    border: 1px solid var(--line);
    background:
        linear-gradient(130deg, rgba(255,255,255,.11), rgba(255,255,255,.035)),
        linear-gradient(135deg, rgba(251,146,60,.18), rgba(236,72,153,.13));
    box-shadow: 0 28px 90px rgba(0,0,0,.33);
    backdrop-filter: blur(20px);
}

.hero-shell::before {
    content: "";
    position: absolute;
    width: 470px;
    height: 470px;
    right: -145px;
    top: -175px;
    border-radius: 50%;
    background: conic-gradient(from 180deg, var(--orange), var(--pink), var(--cyan), var(--orange));
    opacity: .24;
    filter: blur(1px);
}

.hero-shell::after {
    content: "";
    position: absolute;
    inset: 0;
    opacity: .10;
    background-image:
        linear-gradient(rgba(255,255,255,.18) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,.18) 1px, transparent 1px);
    background-size: 42px 42px;
}

.hero-inner {
    position: relative;
    z-index: 2;
    display: grid;
    grid-template-columns: minmax(0, 1.35fr) minmax(320px, .65fr);
    gap: 26px;
    align-items: stretch;
}

.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 9px 13px;
    margin-bottom: 18px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 900;
    letter-spacing: 1.1px;
    text-transform: uppercase;
    color: #ffedd5;
    background: rgba(251,146,60,.13);
    border: 1px solid rgba(251,146,60,.24);
}

.hero-title {
    margin: 0;
    max-width: 840px;
    color: white;
    font-size: clamp(36px, 5.4vw, 74px);
    line-height: .94;
    letter-spacing: -2.9px;
    font-weight: 950;
}

.hero-title span {
    color: transparent;
    background: linear-gradient(90deg, #facc15, #fb923c, #ec4899);
    -webkit-background-clip: text;
    background-clip: text;
}

.hero-desc {
    max-width: 720px;
    margin: 20px 0 0;
    color: #d4d4d8;
    font-size: 16px;
    line-height: 1.75;
}

.hero-side {
    display: grid;
    gap: 14px;
}

.mini-card {
    padding: 18px;
    border-radius: 24px;
    border: 1px solid var(--line);
    background: rgba(10,10,16,.48);
    box-shadow: inset 0 1px 0 rgba(255,255,255,.08);
}

.mini-label {
    color: var(--muted);
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: .8px;
}

.mini-value {
    margin-top: 7px;
    color: white;
    font-size: 29px;
    font-weight: 950;
    letter-spacing: -1px;
}

.control-card {
    margin: 8px 0 26px;
    padding: 24px 24px 10px;
    border-radius: 30px;
    border: 1px solid var(--line);
    background: rgba(255,255,255,.072);
    backdrop-filter: blur(18px);
    box-shadow: 0 24px 70px rgba(0,0,0,.23);
}

.control-title {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    margin-bottom: 7px;
}

.control-title h2 {
    margin: 0;
    color: white;
    font-size: 22px;
    font-weight: 950;
    letter-spacing: -.7px;
}

.control-title p {
    margin: 0;
    color: var(--muted);
    font-size: 13px;
}

[data-testid="stSlider"] {
    padding: 13px 14px 8px;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,.10);
    background: rgba(0,0,0,.16);
}

[data-testid="stSlider"] label p {
    color: #f8fafc !important;
    font-size: 13px !important;
    font-weight: 800 !important;
}

[data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {
    background: #facc15 !important;
    border-color: #facc15 !important;
    box-shadow: 0 0 0 5px rgba(250,204,21,.15) !important;
}

[data-testid="stSlider"] [data-baseweb="slider"] div {
    color: #facc15 !important;
}

.stButton>button {
    width: 100%;
    min-height: 47px;
    border: 1px solid rgba(251,146,60,.34);
    border-radius: 18px;
    color: #fff7ed !important;
    font-weight: 900;
    background: linear-gradient(135deg, rgba(251,146,60,.30), rgba(236,72,153,.22));
    box-shadow: 0 14px 34px rgba(236,72,153,.10);
}

.stButton>button:hover {
    border-color: rgba(250,204,21,.72);
    background: linear-gradient(135deg, rgba(251,146,60,.45), rgba(236,72,153,.30));
}

.section-title {
    margin: 12px 0 14px;
    color: white;
    font-size: 23px;
    font-weight: 950;
    letter-spacing: -.8px;
}

.section-title span {
    display: inline-block;
    width: 13px;
    height: 13px;
    margin-right: 10px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--yellow), var(--pink));
    box-shadow: 0 0 28px rgba(251,146,60,.38);
}

.metric-card {
    min-height: 167px;
    padding: 22px;
    border-radius: 28px;
    border: 1px solid var(--line);
    background:
        linear-gradient(145deg, rgba(255,255,255,.105), rgba(255,255,255,.045));
    box-shadow: 0 22px 65px rgba(0,0,0,.24);
    backdrop-filter: blur(18px);
}

.metric-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 18px;
}

.metric-name {
    color: var(--muted);
    font-size: 13px;
    font-weight: 850;
}

.metric-icon {
    display: grid;
    place-items: center;
    width: 40px;
    height: 40px;
    border-radius: 15px;
    font-size: 20px;
    background: rgba(255,255,255,.09);
}

.metric-value {
    color: white;
    font-size: 31px;
    line-height: 1.05;
    font-weight: 950;
    letter-spacing: -1.2px;
}

.delta-pill {
    display: inline-flex;
    margin-top: 13px;
    padding: 7px 10px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 900;
}

.delta-good {
    color: #bbf7d0;
    background: rgba(52,211,153,.15);
    border: 1px solid rgba(52,211,153,.22);
}

.delta-bad {
    color: #fecdd3;
    background: rgba(251,113,133,.15);
    border: 1px solid rgba(251,113,133,.22);
}

.delta-flat {
    color: #e5e7eb;
    background: rgba(255,255,255,.10);
    border: 1px solid rgba(255,255,255,.14);
}

.status-box {
    margin: 18px 0 30px;
    padding: 18px 20px;
    border-radius: 23px;
    font-size: 15px;
    font-weight: 750;
    border: 1px solid var(--line);
    background: rgba(255,255,255,.075);
    box-shadow: 0 18px 45px rgba(0,0,0,.17);
}

.status-good { color: #bbf7d0; border-color: rgba(52,211,153,.22); background: rgba(52,211,153,.10); }
.status-warn { color: #fed7aa; border-color: rgba(251,146,60,.26); background: rgba(251,146,60,.11); }
.status-info { color: #bae6fd; border-color: rgba(34,211,238,.24); background: rgba(34,211,238,.10); }

.chart-card {
    padding: 24px;
    border-radius: 30px;
    border: 1px solid var(--line);
    background: rgba(255,255,255,.072);
    backdrop-filter: blur(18px);
    box-shadow: 0 24px 70px rgba(0,0,0,.23);
}

.chart-card h3 {
    margin: 0 0 4px;
    color: white;
    font-size: 18px;
    font-weight: 950;
}

.chart-card p {
    margin: 0 0 16px;
    color: var(--muted);
    font-size: 13px;
}

[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,.12);
}

.footer-box {
    margin-top: 24px;
    padding: 16px;
    border-radius: 18px;
    color: var(--muted);
    text-align: center;
    font-size: 12px;
    border: 1px solid rgba(255,255,255,.09);
    background: rgba(255,255,255,.045);
}

@media(max-width: 900px) {
    .hero-inner { grid-template-columns: 1fr; }
    .hero-title { letter-spacing: -1.8px; }
    .main-nav { align-items: flex-start; flex-direction: column; }
}
</style>
""",
    unsafe_allow_html=True,
)


BASELINE = {"iklan": 10, "diskon": 5, "harga": 100}


def hitung_skenario(iklan: float, diskon: float, harga: float) -> dict[str, float]:
    """Model demonstrasi untuk simulasi what-if, seluruh nilai dalam juta rupiah."""
    permintaan_dasar = 1_000
    efek_iklan = 420 * (1 - np.exp(-iklan / 28))
    efek_diskon = 13 * diskon - 0.16 * diskon**2
    efek_harga = -9 * (harga - 100)

    permintaan = max(
        100,
        permintaan_dasar + efek_iklan + efek_diskon + efek_harga,
    )

    harga_jual = harga * (1 - diskon / 100)
    omzet = permintaan * harga_jual / 1_000
    biaya_produk = permintaan * 58 / 1_000
    biaya_iklan = iklan
    keuntungan = omzet - biaya_produk - biaya_iklan - 12

    kapasitas_stok = 1_450
    risiko_stok = np.clip((permintaan - kapasitas_stok) / kapasitas_stok * 100 + 5, 0, 100)

    return {
        "permintaan": permintaan,
        "omzet": omzet,
        "keuntungan": keuntungan,
        "risiko_stok": risiko_stok,
    }


@st.cache_data
def buat_kurva_respons(anggaran_maksimum: int, diskon: int, harga: int) -> pd.DataFrame:
    """Membuat data kurva respons iklan untuk visualisasi."""
    rentang_iklan = np.arange(0, anggaran_maksimum + 1, 5)
    keuntungan = [hitung_skenario(i, diskon, harga)["keuntungan"] for i in rentang_iklan]
    return pd.DataFrame({"Anggaran iklan": rentang_iklan, "Keuntungan": keuntungan})


def format_rupiah(nilai: float) -> str:
    return f"Rp {nilai:,.1f} juta".replace(",", "X").replace(".", ",").replace("X", ".")


def kembali_ke_baseline() -> None:
    st.session_state["iklan"] = BASELINE["iklan"]
    st.session_state["diskon"] = BASELINE["diskon"]
    st.session_state["harga"] = BASELINE["harga"]


def delta_class(nilai: float, inverse: bool = False) -> str:
    if abs(nilai) < 0.01:
        return "delta-flat"
    baik = nilai > 0
    if inverse:
        baik = nilai < 0
    return "delta-good" if baik else "delta-bad"


def metric_card(judul: str, nilai: str, delta: str, ikon: str, kelas_delta: str) -> None:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-head">
                <div class="metric-name">{judul}</div>
                <div class="metric-icon">{ikon}</div>
            </div>
            <div class="metric-value">{nilai}</div>
            <div class="delta-pill {kelas_delta}">{delta}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


baseline = hitung_skenario(**BASELINE)

st.markdown(
    """
    <div class="main-nav">
        <div class="nav-left">
            <div class="nav-logo">SE</div>
            <div>
                <div class="nav-title">Simulator Kebijakan Ekonomi</div>
                <div class="nav-subtitle">Tampilan baru tanpa sidebar · semua kontrol ada di dashboard</div>
            </div>
        </div>
        <div class="nav-badge">LIVE WHAT-IF DASHBOARD</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="hero-shell">
        <div class="hero-inner">
            <div>
                <div class="hero-eyebrow">● Scenario Strategy Room</div>
                <h1 class="hero-title">Ubah angka, lihat <span>dampak bisnis</span>.</h1>
                <p class="hero-desc">
                    Dashboard ini dibuat ulang dengan layout horizontal, kartu neon, dan grafik gelap.
                    Parameter iklan, diskon, dan harga tetap sama, tetapi tampilannya sudah berbeda total.
                </p>
            </div>
            <div class="hero-side">
                <div class="mini-card">
                    <div class="mini-label">Baseline keuntungan</div>
                    <div class="mini-value">{format_rupiah(baseline['keuntungan'])}</div>
                </div>
                <div class="mini-card">
                    <div class="mini-label">Baseline omzet</div>
                    <div class="mini-value">{format_rupiah(baseline['omzet'])}</div>
                </div>
                <div class="mini-card">
                    <div class="mini-label">Baseline permintaan</div>
                    <div class="mini-value">{baseline['permintaan']:,.0f} unit</div>
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="control-card">
        <div class="control-title">
            <div>
                <h2>Panel Pengaturan</h2>
                <p>Ubah slider di bawah, hasil simulasi langsung berubah.</p>
            </div>
        </div>
    """,
    unsafe_allow_html=True,
)

slider_col1, slider_col2, slider_col3, reset_col = st.columns([1, 1, 1, 0.75], gap="medium")

with slider_col1:
    iklan = st.slider("Anggaran iklan (juta Rp)", 0, 100, BASELINE["iklan"], 1, key="iklan")

with slider_col2:
    diskon = st.slider("Besaran diskon (%)", 0, 40, BASELINE["diskon"], 1, key="diskon")

with slider_col3:
    harga = st.slider("Harga awal per unit (ribu Rp)", 70, 130, BASELINE["harga"], 1, key="harga")

with reset_col:
    st.write("")
    st.write("")
    st.button("↻ Reset", on_click=kembali_ke_baseline, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

skenario = hitung_skenario(iklan, diskon, harga)

delta_untung = skenario["keuntungan"] - baseline["keuntungan"]
delta_omzet = skenario["omzet"] - baseline["omzet"]
delta_permintaan = skenario["permintaan"] - baseline["permintaan"]
delta_risiko = skenario["risiko_stok"] - baseline["risiko_stok"]

st.markdown('<div class="section-title"><span></span>Ringkasan Performa</div>', unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4, gap="medium")

with m1:
    metric_card(
        "Keuntungan",
        format_rupiah(skenario["keuntungan"]),
        f"{delta_untung:+.1f} juta vs baseline",
        "💰",
        delta_class(delta_untung),
    )

with m2:
    metric_card(
        "Omzet",
        format_rupiah(skenario["omzet"]),
        f"{delta_omzet:+.1f} juta vs baseline",
        "🧾",
        delta_class(delta_omzet),
    )

with m3:
    metric_card(
        "Permintaan",
        f"{skenario['permintaan']:,.0f} unit",
        f"{delta_permintaan:+.0f} unit vs baseline",
        "📦",
        delta_class(delta_permintaan),
    )

with m4:
    metric_card(
        "Risiko Stok",
        f"{skenario['risiko_stok']:.1f}%",
        f"{delta_risiko:+.1f} poin",
        "⚠️",
        delta_class(delta_risiko, inverse=True),
    )

if delta_untung > 3:
    status_class = "status-good"
    status_text = (
        f"✅ Skenario ini diperkirakan meningkatkan keuntungan sebesar "
        f"{format_rupiah(delta_untung)} dibandingkan baseline."
    )
elif delta_untung < -3:
    status_class = "status-warn"
    status_text = (
        f"⚠️ Skenario ini diperkirakan menurunkan keuntungan sebesar "
        f"{format_rupiah(abs(delta_untung))}. Periksa lagi kombinasi harga, diskon, dan iklan."
    )
else:
    status_class = "status-info"
    status_text = "ℹ️ Keuntungan skenario ini relatif sama dengan baseline."

st.markdown(f'<div class="status-box {status_class}">{status_text}</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title"><span></span>Analisis Skenario</div>', unsafe_allow_html=True)

chart_col, line_col = st.columns([1.05, 1], gap="large")

with chart_col:
    st.markdown(
        """
        <div class="chart-card">
            <h3>Perbandingan Kinerja</h3>
            <p>Baseline dibandingkan dengan skenario aktif.</p>
        """,
        unsafe_allow_html=True,
    )

    kategori = ["Keuntungan", "Omzet"]
    nilai_baseline = [baseline["keuntungan"], baseline["omzet"]]
    nilai_skenario = [skenario["keuntungan"], skenario["omzet"]]
    posisi = np.arange(len(kategori))

    fig, ax = plt.subplots(figsize=(8, 4.3))
    fig.patch.set_alpha(0)
    ax.set_facecolor((0, 0, 0, 0))

    lebar = 0.34
    bar_baseline = ax.bar(
        posisi - lebar / 2,
        nilai_baseline,
        lebar,
        label="Baseline",
        color="#52525b",
        zorder=3,
    )
    bar_skenario = ax.bar(
        posisi + lebar / 2,
        nilai_skenario,
        lebar,
        label="Skenario aktif",
        color="#fb923c",
        zorder=3,
    )

    ax.bar_label(bar_baseline, fmt="%.1f", padding=4, color="#d4d4d8", fontsize=9)
    ax.bar_label(bar_skenario, fmt="%.1f", padding=4, color="#ffffff", fontsize=9, fontweight="bold")
    ax.set_xticks(posisi, kategori)
    ax.legend(frameon=False, labelcolor="#e4e4e7")
    ax.spines[:].set_visible(False)
    ax.tick_params(axis="both", colors="#d4d4d8", length=0)
    ax.grid(axis="y", color=(1, 1, 1, 0.10), linewidth=1, zorder=0)
    ax.margins(y=0.2)

    st.pyplot(fig, use_container_width=True)
    plt.close(fig)
    st.markdown("</div>", unsafe_allow_html=True)

with line_col:
    st.markdown(
        """
        <div class="chart-card">
            <h3>Kurva Respons Iklan</h3>
            <p>Diskon dan harga mengikuti skenario aktif.</p>
        """,
        unsafe_allow_html=True,
    )

    kurva = buat_kurva_respons(100, diskon, harga)
    fig2, ax2 = plt.subplots(figsize=(8, 4.3))
    fig2.patch.set_alpha(0)
    ax2.set_facecolor((0, 0, 0, 0))
    ax2.plot(kurva["Anggaran iklan"], kurva["Keuntungan"], linewidth=3, color="#ec4899")
    ax2.fill_between(
        kurva["Anggaran iklan"],
        kurva["Keuntungan"],
        kurva["Keuntungan"].min(),
        color="#ec4899",
        alpha=0.15,
    )
    ax2.axvline(iklan, color="#facc15", linestyle="--", linewidth=2, label="Iklan aktif")
    ax2.scatter([iklan], [skenario["keuntungan"]], s=80, color="#facc15", zorder=5)
    ax2.set_xlabel("Anggaran iklan", color="#d4d4d8")
    ax2.set_ylabel("Keuntungan", color="#d4d4d8")
    ax2.legend(frameon=False, labelcolor="#e4e4e7")
    ax2.spines[:].set_visible(False)
    ax2.tick_params(axis="both", colors="#d4d4d8", length=0)
    ax2.grid(color=(1, 1, 1, 0.10), linewidth=1)

    st.pyplot(fig2, use_container_width=True)
    plt.close(fig2)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="section-title"><span></span>Detail Kebijakan</div>', unsafe_allow_html=True)

left_detail, right_detail = st.columns([1.1, 1], gap="large")

with left_detail:
    st.markdown(
        """
        <div class="chart-card">
            <h3>Komposisi Kebijakan</h3>
            <p>Perbandingan nilai baseline dan skenario yang sedang aktif.</p>
        """,
        unsafe_allow_html=True,
    )
    tabel = pd.DataFrame(
        {
            "Variabel": ["Anggaran iklan", "Diskon", "Harga awal"],
            "Baseline": ["Rp10 juta", "5%", "Rp100 ribu"],
            "Skenario": [f"Rp{iklan} juta", f"{diskon}%", f"Rp{harga} ribu"],
        }
    )
    st.dataframe(tabel, hide_index=True, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with right_detail:
    st.markdown(
        f"""
        <div class="chart-card">
            <h3>Snapshot Skenario</h3>
            <p>Ringkasan cepat dari parameter yang sedang dipilih.</p>
            <div class="mini-card">
                <div class="mini-label">Iklan</div>
                <div class="mini-value">Rp{iklan} juta</div>
            </div>
            <br>
            <div class="mini-card">
                <div class="mini-label">Diskon dan harga</div>
                <div class="mini-value">{diskon}% · Rp{harga} ribu</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="footer-box">Simulator Kebijakan Ekonomi · Tampilan super beda: tanpa sidebar, tema neon, layout horizontal</div>',
    unsafe_allow_html=True,
)
