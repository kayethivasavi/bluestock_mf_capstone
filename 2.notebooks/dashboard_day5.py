import pandas as pd
import plotly.express as px
import os

BASE = r"C:\Users\VASAVI\Desktop\bluestock_mf_capstone"

sip = pd.read_csv(os.path.join(BASE, "1.data/raw/04_monthly_sip_inflows.csv"))
aum = pd.read_csv(os.path.join(BASE, "1.data/raw/03_aum_by_fund_house.csv"))

sip['month'] = pd.to_datetime(sip['month'])

# SIP Trend
fig1 = px.line(
    sip,
    x='month',
    y='sip_inflow_crore',
    title='SIP Inflow Trend (2022-2025)'
)

fig1.write_html(os.path.join(BASE, "5.reports/sip_trend.html"))

# AUM Bar
fig2 = px.bar(
    aum,
    x='fund_house',
    y='aum_lakh_crore',
    title='AUM by Fund House'
)

fig2.write_html(os.path.join(BASE, "5.reports/aum_bar.html"))

print("Dashboard created successfully!")
demo = pd.read_csv(os.path.join(BASE, "1.data/raw/08_investor_transactions.csv"))

# -------------------------
# PAGE 3: Investor Analytics
# -------------------------

# State-wise investment
state_fig = px.bar(
    demo.groupby('state')['amount_inr'].sum().reset_index(),
    x='state',
    y='amount_inr',
    title='Investment by State'
)

state_fig.write_html(os.path.join(BASE, "5.reports/state_investment.html"))

# SIP vs Lumpsum split
txn_fig = px.pie(
    demo,
    names='transaction_type',
    title='Transaction Type Split'
)

txn_fig.write_html(os.path.join(BASE, "5.reports/transaction_split.html"))

print("Page 3 created")
# -------------------------
# PAGE 4: SIP & Market Trends
# -------------------------

# SIP trend already exists, now add category view
category = pd.read_csv(os.path.join(BASE, "1.data/raw/05_category_inflows.csv"))
category['month'] = pd.to_datetime(category['month'])

# Category heatmap (simple version)
heatmap_fig = px.density_heatmap(
    category,
    x='month',
    y='category',
    z='net_inflow_crore',
    title='Category Inflow Heatmap'
)

heatmap_fig.write_html(os.path.join(BASE, "5.reports/category_heatmap.html"))

# Top categories
top_cat = category.groupby('category')['net_inflow_crore'].sum().reset_index()

top_fig = px.bar(
    top_cat,
    x='category',
    y='net_inflow_crore',
    title='Top Categories by Inflow'
)

top_fig.write_html(os.path.join(BASE, "5.reports/top_categories.html"))

print("Page 4 created")