import streamlit as st
import us_stats
import datetime
import random

dash_title = 'America at a Glance'
VERSION = '0.0.1'
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
if 'date' in st.query_params:
    date = datetime.datetime.strptime(st.query_params['date'], '%Y-%m-%d').date()
else:
    min_date = datetime.date(1776, 1, 1)
    max_date = datetime.date(2025, 1, 1)
    disp_date = datetime.date(1776, 1, 1)+datetime.timedelta(days=random.randint(1, (max_date - min_date).days))

    date = st.date_input("Pick a date", value=datetime.date(1841, 3, 5),
                        min_value=min_date,
                        max_value=max_date)
st.markdown(f'<div class="headline">{dash_title} – {date}</div>', unsafe_allow_html=True)

# Sidebar
engine = us_stats.PeriodData(f'{date:%Y-%m-%d}')
comp = -engine

col1, col2 = st.columns([2, 1])

# Column 1: Chart or Data
with col1:
    st.markdown('<div class="section-header">Economic Review</div>', unsafe_allow_html=True)
    col1a, col1b = st.columns([1, 1])
    with col1a:
        st.markdown('<div class="section-header">US</div>', unsafe_allow_html=True)
        st.metric("Population", f"{engine.us_pop.pretty}")
        st.metric("GDP", f"${engine.us_gdp.pretty}")
        st.metric("Per Capita GDP", f"${engine.us_gdp.pretty_per_capita}")
    with col1b:
        st.markdown('<div class="section-header">World</div>', unsafe_allow_html=True)
        st.metric("Population", f"{engine.world_pop.pretty}")
        st.metric("GDP", f"${engine.world_gdp.pretty}")
        st.metric("Per Capita GDP", f"${engine.world_gdp.pretty_per_capita}")
    #st.metric("CPI", f"{engine.cpi}")
    #st.metric("Adjusted CPI", f"{comp.cpi_delta.delta}")
    st.metric(f"$100 in {comp.second_year} comparable value in {comp.first_year}", f"${100*comp.cpi_delta:.2f}")
    st.metric(f"$100 om {comp.first_year} comparable value in {comp.second_year}", f"${100/comp.cpi_delta:.2f}")

# Comparison
    st.write(f"{comp.us_pop_delta}")
    st.markdown('<div class="section-header">Constitutional Amendments</div>', unsafe_allow_html=True)
    amendments = ['I-X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', '~XVIII~' if engine.amendments >= 21 else 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII']
    st.markdown(" ".join(f'**[{a}]({"https://www.archives.gov/founding-docs/amendments-11-27#" + a.lower().replace('~','') if i else "https://www.archives.gov/founding-docs/bill-of-rights-transcript"})**' if i + 10 <= engine.amendments else f'*[{a}]({"https://www.archives.gov/founding-docs/amendments-11-27#" + a.lower() if i else "https://www.archives.gov/founding-docs/bill-of-rights-transcript"})*' for i, a in enumerate(amendments)))

# Column 2: Sidebar Info
with col2:
    st.markdown('<div class="section-header">Leader of the Nation</div>', unsafe_allow_html=True)
    st.image(f"images/presidents/{engine.president.image}", caption=f"{engine.president}")
    st.markdown(f"**{engine.president.name}**")

    st.markdown('<div class="section-header">National Flag</div>', unsafe_allow_html=True)
    st.image(f"images/flags/{engine.flag.image}", caption=f"{engine.flag}")
    st.markdown(f"{engine.flag}")

    st.markdown(f'<div class="section-header">Map of the US on {engine.date}</div>', unsafe_allow_html=True)
    #st.image(f"images/maps/{engine.map}", use_column_width=True)
    st.markdown(f"{engine.state_admissions}")

st.markdown(f"**Version:** {VERSION}")
st.markdown("_Early demo — features and layout will evolve_")
st.markdown("_Contact: [LinkedIn](https://www.linkedin.com/in/dfpeterson/) | [GitHub](https://github.com/dfpeterson/) | [E-mail](mailto:dfpeterson+stats@gmail.com)_")
# Main stats

#Sources
