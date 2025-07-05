import streamlit as st
import us_stats
import datetime

dash_title = 'America at a Glance'
st.set_page_config(layout="wide", page_title=dash_title)

#st.title(dash_title)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display&family=Libre+Baskerville&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Libre Baskerville', serif;
        background-color: #f4ecd8;
        color: #111111;
    }

    .headline {
        font-family: 'Playfair Display', serif;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        padding: 0.3em;
        border-bottom: 2px solid #444;
        margin-bottom: 0.5em;
    }

    .section-header {
        font-family: 'Playfair Display', serif;
        font-size: 24px;
        margin-top: 1.5em;
        margin-bottom: 0.3em;
        border-bottom: 1px dashed #888;
    }
    </style>
    """, unsafe_allow_html=True)

date = st.date_input("Pick a date", value=datetime.date(1860, 1, 1),
                     min_value=datetime.date(1776, 1, 1),
                     max_value=datetime.date(2025, 1, 1))
st.markdown(f'<div class="headline">{dash_title} – {date}</div>', unsafe_allow_html=True)

# Sidebar
engine = us_stats.PeriodData(f'{date:%Y-%m-%d}')
comp = -engine

col1, col2 = st.columns([2, 1])

# Column 1: Chart or Data
with col1:
    st.markdown('<div class="section-header">Economic Review</div>', unsafe_allow_html=True)
    st.metric("Population", f"{engine.us_pop}")
    st.metric("GDP", f"${engine.us_gdp}")
    #st.metric("CPI", f"{engine.cpi}")
    #st.metric("Adjusted CPI", f"{comp.cpi_delta.delta}")
    st.metric(f"{comp.second_year} $100 comparable value in {comp.first_year}", f"${100*comp.cpi_delta:.2f}")
    st.metric(f"{comp.first_year} $100 comparable value in {comp.second_year}", f"${100/comp.cpi_delta:.2f}")

# Comparison
    st.write(f"{comp.us_pop_delta}")
    st.markdown('<div class="section-header">Constitutional Amendments</div>', unsafe_allow_html=True)
    amendments = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
                  "XI", "XII", "XIII", "XIV", "XV"]
    ratified_count = 12  # Example cutoff
    st.markdown(" ".join(f"**{a}**" if i < ratified_count else f"*{a}*" for i, a in enumerate(amendments)))

# Column 2: Sidebar Info
with col2:
    st.markdown('<div class="section-header">Leader of the Nation</div>', unsafe_allow_html=True)
    st.image(f"images/presidents/{engine.president.image}", caption=f"{engine.president.name}")
    st.markdown(f"**{engine.president}**")

    st.markdown('<div class="section-header">National Flag</div>', unsafe_allow_html=True)
    st.image(f"images/flags/{engine.state_admissions.num_states}stars.png", caption=f"{engine.state_admissions}-Star Flag")
    st.markdown(f"{engine.state_admissions}")

    st.markdown(f'<div class="section-header">Map of the US on {engine.date}</div>', unsafe_allow_html=True)

# Main stats

#Sources
