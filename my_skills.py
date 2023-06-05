import requests
import streamlit as st
from streamlit_lottie import st_lottie
import plotly.graph_objects as go
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.render import make_snapshot
from pyecharts.globals import ThemeType
from snapshot_selenium import snapshot
from streamlit_echarts import st_pyecharts

st.set_page_config(page_title="Manoj Roy | Skills", page_icon=":running:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- LOAD ASSETS ----
lottie_skills = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_ul35wckt.json"
)


# ---- Header ----
st.subheader("Hi, I am Manoj Roy :wave:")
st.title("Data Enthusiast & Researcher")
st.write("##")
st.markdown(
    """
    <div class="newspaper">
        <p class="first-letter">A</p> highly motivated and detail-oriented researcher with an Masters in Applied Statistics and
        Data Science, possessing a strong background in statistics and data analysis. Passionate about
        public health and epidemiology, with a keen interest in understanding the spread and control
        of infectious diseases, committed to improving health outcomes in communities. A natural
        collaborator with excellent communication skills, confident in the ability to work effectively
        with multidisciplinary research teams and engage with stakeholders from diverse
        backgrounds. Committed to continuous learning and professional development, excited
        about opportunities in a career as a researcher in epidemiology.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
        .newspaper {
            font-family: 'Georgia', serif;
            font-size: 16px;
            line-height: 1.6;
            margin: 0 auto;
            max-width: 700px;
            padding: 20px;
            text-align: justify;
        }
        
        .first-letter {
            font-size: 48px;
            font-weight: bold;
            color: #333333;
            margin: 0;
            padding-right: 10px;
            float: left;
        }
    </style>
    """,
    unsafe_allow_html=True
)
# ---- Header ----

# Create the pie chart
pie_chart = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add(
        "Access From",
        [
            ["Statistical", 335],
            ["Technical", 310],
            ["Proactive Learning", 274],
            ["Problem Solving", 235],
            ["Exploring", 400]
        ],
        radius="95%",
        center=["65%", "65%"],
        rosetype="radius",
        label_opts=opts.LabelOpts(
            color="black",
            position="inside",
            font_size=10,
            formatter="{b}: {d}%",
        ),
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{b}: {d}%"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="My Skills",
            title_textstyle_opts=opts.TextStyleOpts(
                color="white",
                font_size=25,
                font_weight="bold",
                align="center",
                vertical_align="top"
            ),
            pos_top="5%",
            pos_left="center"
        ),
        legend_opts=opts.LegendOpts(
            orient="vertical",
            pos_top="middle",
            pos_right="5%",
            item_width=15,
            item_height=15,
            textstyle_opts=opts.TextStyleOpts(color="white"),
        ),
    )
)

# Render the pie chart as HTML
make_snapshot(snapshot, pie_chart.render(), "skills_manoj_pie.png")

# Create two columns layout
col1, col2 = st.columns([2, 1])

# Display the pie chart in the first column
with col1:
    st_pyecharts(pie_chart)

# Display the coding animation in the second column
with col2:
    st_lottie(lottie_skills, speed=1, width=300, height=300)
    




