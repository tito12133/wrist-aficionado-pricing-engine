import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Wrist Aficionado | Pricing Intelligence",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ultra-luxury sharp CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=Montserrat:wght@200;300;400;500;600&display=swap');
    
    * {
        border-radius: 0px !important;
    }
    
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #0d0d0d 100%);
    }
    
    /* Gold accent glow */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 20% 50%, rgba(212, 175, 55, 0.02) 0%, transparent 40%),
                    radial-gradient(circle at 80% 80%, rgba(212, 175, 55, 0.015) 0%, transparent 40%);
        pointer-events: none;
    }
    
    /* Main title */
    h1 {
        font-family: 'Cormorant Garamond', serif;
        background: linear-gradient(135deg, #d4af37 0%, #f4e5a8 50%, #d4af37 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 300;
        font-size: 5rem !important;
        letter-spacing: 12px;
        text-transform: uppercase;
        text-align: center;
        padding: 30px 0 20px 0;
        margin: 0;
        text-shadow: 0 0 40px rgba(212, 175, 55, 0.3);
    }
    
    .subtitle {
        font-family: 'Montserrat', sans-serif;
        color: #666666;
        font-size: 0.7rem;
        letter-spacing: 6px;
        text-transform: uppercase;
        font-weight: 300;
        text-align: center;
        margin-bottom: 60px;
        border-top: 1px solid rgba(212, 175, 55, 0.2);
        padding-top: 15px;
    }
    
    /* Metrics - refined */
    [data-testid="stMetricValue"] {
        font-family: 'Montserrat', sans-serif;
        font-size: 2.2rem !important;
        color: #d4af37 !important;
        font-weight: 300 !important;
    }
    
    [data-testid="stMetricLabel"] {
        font-family: 'Montserrat', sans-serif;
        color: #505050 !important;
        font-size: 0.6rem !important;
        letter-spacing: 3px !important;
        text-transform: uppercase !important;
        font-weight: 400 !important;
    }
    
    div[data-testid="metric-container"] {
        background: rgba(10, 10, 10, 0.8);
        border: 1px solid rgba(212, 175, 55, 0.15);
        padding: 28px 18px;
        box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.5);
    }
    
    /* Sidebar - pure luxury */
    div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #000000 0%, #0a0a0a 100%);
        border-right: 1px solid #d4af37;
    }
    
    [data-testid="stSidebar"] h3 {
        color: #d4af37 !important;
        font-family: 'Montserrat', sans-serif;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
        letter-spacing: 5px !important;
        text-transform: uppercase !important;
        margin-top: 40px !important;
        margin-bottom: 35px !important;
        text-align: center;
    }
    
    /* FIX SIDEBAR LABELS - FORCE GOLD */
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .st-emotion-cache-16idsys p,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span {
        color: #d4af37 !important;
        font-family: 'Montserrat', sans-serif !important;
        font-size: 0.7rem !important;
        font-weight: 400 !important;
        letter-spacing: 2px !important;
    }
    
    /* Section headers */
    h3 {
        font-family: 'Cormorant Garamond', serif;
        color: #d4af37;
        font-size: 1.4rem !important;
        font-weight: 400;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-top: 60px !important;
        margin-bottom: 20px !important;
        padding-bottom: 10px;
        border-bottom: 1px solid rgba(212, 175, 55, 0.3);
    }
    
    /* Data table */
    .stDataFrame {
        font-family: 'Montserrat', sans-serif;
        font-size: 0.8rem;
    }
    
    [data-testid="stDataFrame"] {
        border: 1px solid rgba(212, 175, 55, 0.2);
    }
    
    /* Download button */
    .stDownloadButton button {
        background: linear-gradient(135deg, #d4af37 0%, #c9a028 100%);
        color: #000000;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        letter-spacing: 4px;
        text-transform: uppercase;
        border: 1px solid #d4af37;
        padding: 16px 45px;
        font-size: 0.75rem;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
    }
    
    .stDownloadButton button:hover {
        background: #d4af37;
        box-shadow: 0 6px 25px rgba(212, 175, 55, 0.5);
    }
    
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, #d4af37, transparent);
        margin: 70px 0;
    }
    
    p {
        font-family: 'Montserrat', sans-serif;
        color: #666666;
        font-size: 0.75rem;
        letter-spacing: 1px;
        font-weight: 300;
    }
    
    /* Force remove all rounding */
    .js-plotly-plot, .plotly, svg {
        border-radius: 0px !important;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv('watch_listings.csv')
    df['scraped_date'] = pd.to_datetime(df['scraped_date'])
    return df

df = load_data()

# Title
st.markdown("<h1>WRIST AFICIONADO</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>PRICING INTELLIGENCE ENGINE</p>", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("### FILTERS")

selected_models = st.sidebar.multiselect(
    "Reference",
    options=sorted(df['sku'].unique()),
    default=list(df['sku'].unique()[:2])
)

selected_conditions = st.sidebar.multiselect(
    "Condition",
    options=df['condition'].unique(),
    default=list(df['condition'].unique())
)

price_range = st.sidebar.slider(
    "Price Range",
    min_value=int(df['price_usd'].min()),
    max_value=int(df['price_usd'].max()),
    value=(int(df['price_usd'].min()), int(df['price_usd'].max())),
    format="$%d"
)

year_range = st.sidebar.slider(
    "Year",
    min_value=int(df['year'].min()),
    max_value=int(df['year'].max()),
    value=(int(df['year'].min()), int(df['year'].max()))
)

# Filter
filtered_df = df[
    (df['sku'].isin(selected_models)) &
    (df['condition'].isin(selected_conditions)) &
    (df['price_usd'] >= price_range[0]) &
    (df['price_usd'] <= price_range[1]) &
    (df['year'] >= year_range[0]) &
    (df['year'] <= year_range[1])
]

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("LISTINGS", f"{len(filtered_df):,}")

with col2:
    avg_price = filtered_df['price_usd'].mean()
    st.metric("AVERAGE", f"${avg_price:,.0f}")

with col3:
    floor_price = filtered_df['price_usd'].min()
    st.metric("FLOOR", f"${floor_price:,.0f}")

with col4:
    opportunities = len(filtered_df[filtered_df['price_usd'] < avg_price * 0.92])
    st.metric("TARGETS", opportunities)

st.markdown("---")

# Refined gold palette
gold = ['#d4af37', '#c9a028', '#b8941f', '#a68316', '#94720d']

# Chart 1: Box Plot
st.markdown("### PRICE DISTRIBUTION")

fig1 = go.Figure()

for idx, condition in enumerate(sorted(filtered_df['condition'].unique())):
    for sku_idx, sku in enumerate(sorted(filtered_df['sku'].unique())):
        data = filtered_df[(filtered_df['condition'] == condition) & (filtered_df['sku'] == sku)]
        if len(data) > 0:
            fig1.add_trace(go.Box(
                y=data['price_usd'],
                name=f"{condition}",
                marker=dict(color=gold[idx % len(gold)], line=dict(width=0.5, color='#d4af37')),
                line=dict(color=gold[idx % len(gold)], width=1),
                boxmean=False,
                showlegend=(sku_idx == 0)
            ))

fig1.update_layout(
    template='plotly_dark',
    plot_bgcolor='#000000',
    paper_bgcolor='#0a0a0a',
    font=dict(family="Montserrat", size=9, color="#666666", weight=300),
    showlegend=True,
    legend=dict(orientation="h", y=-0.25, x=0.5, xanchor="center", font=dict(size=9)),
    yaxis=dict(title="USD", gridcolor='#1a1a1a', showgrid=True),
    height=380,
    margin=dict(t=5, b=80, l=50, r=10)
)

st.plotly_chart(fig1, use_container_width=True)

# Chart 2: Perfect Donut
st.markdown("### GEOGRAPHIC DISTRIBUTION")

location_counts = filtered_df['location'].value_counts()

fig2 = go.Figure(data=[go.Pie(
    labels=location_counts.index,
    values=location_counts.values,
    hole=0.65,
    marker=dict(
        colors=gold,
        line=dict(color='#000000', width=2)
    ),
    textposition='outside',
    texttemplate='%{label}<br>%{percent}',
    textfont=dict(size=9, family="Montserrat", color="#666666"),
    hovertemplate='<b>%{label}</b><br>%{value} listings<br>%{percent}<extra></extra>',
    sort=False
)])

fig2.update_layout(
    template='plotly_dark',
    plot_bgcolor='#000000',
    paper_bgcolor='#0a0a0a',
    showlegend=False,
    height=380,
    margin=dict(t=5, b=5, l=5, r=5),
    annotations=[dict(
        text='MARKETS',
        x=0.5, y=0.5,
        font=dict(size=11, family="Montserrat", color="#d4af37", weight=300),
        showarrow=False
    )]
)

st.plotly_chart(fig2, use_container_width=True)

# Chart 3: Line Chart
st.markdown("### PRICE TRENDS")

trend_df = filtered_df.groupby(['scraped_date', 'sku'])['price_usd'].mean().reset_index()
fig3 = go.Figure()

for idx, sku in enumerate(sorted(trend_df['sku'].unique())):
    sku_data = trend_df[trend_df['sku'] == sku]
    fig3.add_trace(go.Scatter(
        x=sku_data['scraped_date'],
        y=sku_data['price_usd'],
        mode='lines',
        name=sku,
        line=dict(width=1.5, color=gold[idx % len(gold)]),
        hovertemplate='%{y:$,.0f}<extra></extra>'
    ))

fig3.update_layout(
    template='plotly_dark',
    plot_bgcolor='#000000',
    paper_bgcolor='#0a0a0a',
    font=dict(family="Montserrat", size=9, color="#666666"),
    showlegend=True,
    legend=dict(orientation="h", y=-0.25, x=0.5, xanchor="center", font=dict(size=9)),
    xaxis=dict(gridcolor='#1a1a1a', showgrid=True),
    yaxis=dict(title="USD", gridcolor='#1a1a1a', showgrid=True),
    height=380,
    margin=dict(t=5, b=80, l=50, r=10)
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# Table
st.markdown("### ACQUISITION TARGETS")
st.markdown("*Below-market opportunities with 30% margin potential*")

opportunity_df = filtered_df[filtered_df['price_usd'] < filtered_df.groupby('sku')['price_usd'].transform('mean') * 0.92].copy()
opportunity_df = opportunity_df.sort_values('price_usd')

opportunity_df['list'] = (opportunity_df['price_usd'] * 1.30).round(0).astype(int)
opportunity_df['profit'] = (opportunity_df['list'] - opportunity_df['price_usd']).astype(int)
opportunity_df['margin'] = ((opportunity_df['profit'] / opportunity_df['list']) * 100).round(1)

display_df = opportunity_df[['sku', 'condition', 'year', 'price_usd', 'list', 'profit', 'margin', 'location']].head(20)
display_df.columns = ['REF', 'CONDITION', 'YR', 'FLOOR', 'LIST', 'PROFIT', 'MARGIN%', 'LOCATION']

st.dataframe(display_df, use_container_width=True, hide_index=True, height=450)

st.markdown("---")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="EXPORT",
        data=csv,
        file_name="wrist_aficionado.csv",
        mime="text/csv",
        use_container_width=True
    )
