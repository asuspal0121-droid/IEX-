import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ==========================================
# 1. PAGE CONFIGURATION (Browser Tab Title)
# ==========================================
st.set_page_config(
    page_title="IEX Market Dashboard",
    page_icon="⚡",
    layout="wide"
)

# ==========================================
# 2. CSS STYLING (To mimic the SolarFlow Dark/Light look)
# ==========================================
# This hides the default top red bar and adjusts the sidebar
st.markdown("""
    <style>
    .main {background-color: #F8F9FA;} 
    [data-testid="stSidebar"] {background-color: #1E232E; color: white;}
    .css-1d391kg {padding-top: 1rem;}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. SIDEBAR (Navigation like 'SolarFlow' Left Panel)
# ==========================================
with st.sidebar:
    st.title("⚡ IEX Dashboard") # Title similar to "SolarFlow"
    
    # The menu options extracted from your IEX image headers
    selected_market = st.radio(
        "Navigation", 
        [
            "Dashboard Overview", 
            "Day Ahead Market", 
            "Green Day Ahead Market", 
            "High Price Day Ahead Market", 
            "Real Time Market"
        ]
    )
    
    st.markdown("---")
    st.caption("Last Updated: 2026-01-20")

# ==========================================
# 4. MAIN DASHBOARD CONTENT
# ==========================================

# HEADER SECTION
st.title(f"{selected_market}")
st.markdown("Welcome back! Here is today's market performance.")

# --- PLACEHOLDERS FOR YOUR DATA ---
# In the future, you will connect your 'scrapping.py' output here.
# For now, I am putting dummy numbers so you can see the layout.

# ROW 1: METRIC CARDS (Mimicking the SolarFlow Cards)
col1, col2, col3, col4 = st.columns(4)

with col1:
    # 1. Day Ahead Market Header
    st.metric(
        label="Day Ahead Market (Price)", 
        value="₹ 5.40", 
        delta="12%"
    )

with col2:
    # 2. Green Day Ahead Market Header
    st.metric(
        label="Green Day Ahead (Vol)", 
        value="12.5 MU", 
        delta="-5%"
    )

with col3:
    # 3. High Price DAM Header
    st.metric(
        label="High Price DAM", 
        value="₹ 15.00", 
        delta="0.5%"
    )

with col4:
    # 4. Real Time Market Header
    st.metric(
        label="Real Time Market", 
        value="₹ 4.20", 
        delta="2%"
    )

st.markdown("---")

# ==========================================
# 5. DETAILED CHARTS (The "Analytics" section)
# ==========================================

# We create a simple chart that updates based on the sidebar selection
# You can add your scraped data into the 'y=' lists below.

st.subheader("Market Trends")

if selected_market == "Dashboard Overview":
    # Example: Comparison Chart
    chart_data = pd.DataFrame({
        'Market': ['DAM', 'G-DAM', 'HP-DAM', 'RTM'],
        'Volume': [100, 45, 12, 80] # <--- REPLACE WITH YOUR SCRAPED DATA
    })
    st.bar_chart(chart_data, x='Market', y='Volume')

elif selected_market == "Day Ahead Market":
    # Example: Line Chart for time series
    st.write("Hourly Price Trends for Day Ahead Market")
    chart_data = pd.DataFrame({
        'Hour': range(1, 25),
        'Price': [4, 5, 6, 5, 4, 3, 5, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]
    })
    st.line_chart(chart_data, x='Hour', y='Price')

else:
    st.info("No data connected for this section yet. You can add it in the code!")

# ==========================================
# 6. HOW TO ADD YOUR SCRAPED DATA
# ==========================================
with st.expander("🛠️ Developer Options (How to Edit)"):
    st.write("""
    1. Open `dashboard.py`.
    2. Import your scraping script: `import scrapping`.
    3. Replace the `value="₹ 5.40"` in the `st.metric` section with your variables.
       * Example: `value=scrapping.current_price`
    """)
