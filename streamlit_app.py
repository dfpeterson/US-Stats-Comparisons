import streamlit as st
import altair as alt
import datetime
#import random
from stats_engine import period_data 

dash_title = 'America at a Glance'
VERSION = '0.0.03'
st.set_page_config(layout='wide', page_title=dash_title)

st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Cormorant+Garamond:wght@400;500;600&display=swap');

/* Global old-paper look */
html, body, .stApp, .main, [class*="css"] {
    background-color: #f3ebd6 !important;  /* yellowed newsprint */
    color: #141414;
    font-family: 'Cormorant Garamond', serif !important;
    line-height: 1.55;
}

/* Paper grain */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    background:
        radial-gradient(circle at 50% 50%, rgba(255,255,255,0.03), rgba(0,0,0,0.07)),
        repeating-linear-gradient(90deg, rgba(0,0,0,0.02), rgba(0,0,0,0.02) 1px, transparent 1px, transparent 4px);
    opacity: 0.4;
    z-index: -1;
}

/* Make Streamlit content span the full width of the main area */
.main .block-container,
.main > div,
.stApp > div {
    max-width: 100% !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
}

/* Optional “page” wrapper so content doesn’t hit the very edge */
.page {
    max-width: 1200px;              /* adjust wider/narrower to taste */
    margin: 0 auto;
    padding: 0 2rem 3rem;
}

/* ===== Masthead (Updated layout) ===== */

.masthead {
    margin: 0 0 1.5rem 0;
    padding-top: 0.5rem;
    border-top: 4px solid #000;
    border-bottom: 4px solid #000;
}

.masthead-inner {
    border-top: 2px solid #000;
    border-bottom: 2px solid #000;
    padding: 0.75rem 2rem 1rem;
}

/* Big centered masthead title */
.masthead-title {
    font-family: 'Playfair Display', serif;
    font-weight: 900;
    font-size: 64px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    text-align: center;
    margin: 0 0 0.6rem 0;
}

/* Flex container to align Volume left + Date right */
.masthead-subrow {
    display: flex;
    justify-content: space-between;
    width: 100%;
    margin-top: 0.2rem;
}

/* Volume (left) */
.masthead-volume {
    font-family: 'Cormorant Garamond', serif;
    font-size: 15px;
    text-transform: uppercase;
    letter-spacing: 0.16em;
    margin: 0;
}

/* Dateline (right) */
.masthead-date {
    font-family: 'Cormorant Garamond', serif;
    font-size: 15px;
    text-transform: uppercase;
    letter-spacing: 0.16em;
    margin: 0;
    text-align: right;
}

/* Section headers for below-the-fold sections */
.section-header {
    font-family: 'Cormorant Garamond', serif;
    font-size: 24px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    border-bottom: 1px solid #555;
    margin-top: 1.5rem;
    margin-bottom: 0.4rem;
}

/* Base body text */
p, .stMarkdown, .stText {
    font-size: 18px;
    line-height: 1.6;
}
</style>
    """)

if 'date' in st.query_params:
    date = datetime.datetime.strptime(st.query_params['date'], '%Y-%m-%d').date()
else:
    with st.sidebar:
        date = st.date_input('Pick a date', value=datetime.date(1841, 3, 5),
                            #value=datetime.date(1776, 1, 1)+datetime.timedelta(days=random.randint(1, (datetime.date(2025, 1, 1) - datetime.date(1776, 1, 1)).days)),
                            min_value=datetime.date(1776, 1, 1),
                            max_value=datetime.date(2025, 1, 1))

# Sidebar
engine = period_data.PeriodData(f'{date:%Y-%m-%d}')
comp = -engine

st.html(f"""
    <div class="masthead">
      <div class="masthead-inner">
        <div class="masthead-title">{dash_title}</div>
                <div class="masthead-subrow">
            <div class="masthead-volume">VOLUME {engine.amendments.as_numeral}.—ESTABLISHED JULY 4, 1776.</div>
            <div class="masthead-date">{date:%A %B %d, %Y}.</div>
        </div>
      </div>
    </div>
    """)


col1, col2 = st.columns([2, 1])

# Column 1: Chart or Data
with col1:
    st.html('<div class="section-header">Economic Overview</div>')
    col1a, col1b = st.columns([1, 1])
    with col1a:
        st.html('<div class="section-header">US</div>')
        st.metric('GDP', f'{engine.us_gdp.pretty}')
        st.metric('Per Capita GDP', f'{engine.us_gdp.pretty_per_capita}')
    with col1b:
        st.html('<div class="section-header">World</div>')
        st.metric('GDP', f'{engine.world_gdp.pretty}')
        st.metric('Per Capita GDP', f'{engine.world_gdp.pretty_per_capita}')
    #st.metric("CPI", f"{engine.cpi}")
    #st.metric("Adjusted CPI", f"{comp.cpi_delta.delta}")
    st.metric(f'$100 in {comp.second_year} comparable value in {comp.first_year}', f'${100*comp.cpi_delta:,.2f}')
    st.metric(f'$100 in {comp.first_year} comparable value in {comp.second_year}', f'${100/comp.cpi_delta:,.2f}')

    st.html('<div class="section-header">Demographic State of the Union</div>')
    col1a, col1b = st.columns([1, 1])
    with col1a:
        st.metric('Population', f'{engine.us_pop.pretty}', delta=f'{comp.us_pop_delta.delta:.1%}', delta_color='off', delta_arrow='off')
        st.write(f'{comp.us_pop_delta}')
    with col1b:
        st.metric('Population', f'{engine.world_pop.pretty}', delta=f'{comp.world_pop_delta.delta:.1%}', delta_color='off', delta_arrow='off')
        st.write(f'{comp.world_pop_delta}')


# Comparison
    st.html('<div class="section-header">Constitutional Amendments</div>')
    st.html(engine.amendments.html)

# Column 2: Sidebar Info
with col2:
    st.html('<div class="section-header">State of the Government</div>')
    st.html('<div class="section-header">The Executive Branch</div>')
    st.html(f'<strong>{engine.president.name}</strong>')
    #st.html(f'<img src="images/parties/{engine.president.party.lower()}.jpg"> {engine.president.party.title()}')
    st.html(f'{engine.president.calc_days(date)}')
    st.image(f'images/presidents/{engine.president.image}', caption=f'{engine.president}')

    st.html('<div class="section-header">The Legislative Branch</div>')

    st.html('<div class="section-header">The Judicial Branch</div>')
    #st.html(engine.supreme_court.html)
    # st.bar_chart(engine.supreme_court.bar_chart, x='Name', y=['Assoc. Tenure', 'Chief Tenure'],
    #              horizontal=True, width='stretch', sort='-Tenure', x_label='Tenure (years)',
    #              y_label=None, color=['#555555', '#111111'])

    chart = (
            alt.Chart(engine.supreme_court.bar_chart)
            .mark_bar()
            .encode(
                y=alt.Y("Name:N", sort="-x", title=None),
                x=alt.X("Tenure:Q", title="Years Served"),
                 color=alt.Color(
                     "Role:N",
                     scale=alt.Scale(
                         domain=["Vacant", "Associate", "Chief"],
                         range=["#AAAAAA", "#555555", "#111111"],
                     ),
                     legend=None,
                 ),
                tooltip=[
                alt.Tooltip("Name:N", title="Justice"),
                alt.Tooltip("Role:N", title="Role"),
                alt.Tooltip("Tenure:Q", title="Years", format=",.2f"),
                alt.Tooltip("State:N", title="From"),
                alt.Tooltip("President:N", title="Appointed by"),
                ],
            )
            .properties(
                background="#f3ebd6",
                height=400,
            )
            .configure_view(stroke=None)
            .configure_axis(
                labelFont="Cormorant Garamond",
                titleFont="Cormorant Garamond",
                labelColor="#111",
                titleColor="#111",
                grid=False,
            )
        )

    st.altair_chart(chart, use_container_width=True)

    #st.dataframe(engine.supreme_court.bar_chart, use_container_width=True)

    st.html('<div class="section-header">The State of the States</div>')
    st.image(f'images/flags/{engine.flag.image}', caption=f'{engine.flag}')
    st.html(f'Adopted on {engine.flag.pretty_date}')

    st.html(f'<div class="section-header">Map of the US on {engine.pretty_date}</div>')
    #st.image(f"images/maps/{engine.map}", use_column_width=True)
    st.html(f"Number of states in the union <strong>{engine.state_admissions.num_states}</strong>")
    st.html(f'The newest state: <strong>{engine.state_admissions.last_state_name}</strong> (admitted {engine.state_admissions.last_state_pretty_date})')

st.html(f"<strong>Version:<strong> {VERSION}")
st.html('<em>Early demo — features and layout will evolve</em>')
st.markdown('_Contact: [LinkedIn](https://www.linkedin.com/in/dfpeterson/) | [GitHub](https://github.com/dfpeterson/) | [E-mail](mailto:dfpeterson+stats@gmail.com)_')

#Sources
