import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Clique Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Navigation
# Sidebar Information
st.sidebar.markdown("### CS F364: Design and Analysis of Algorithms")
st.sidebar.markdown("**Assignment 1**")
st.sidebar.markdown("Made by: **Group 30**")
st.sidebar.markdown("* Bhaskar Mishra")
st.sidebar.markdown("* Nishchay Deep")
st.sidebar.markdown("* Thakur Manas Singh")
st.sidebar.markdown("* Unnam Kinshuk Chowdary")
st.sidebar.markdown("* Tanmay Sharma")
st.sidebar.markdown("---")

page = st.sidebar.selectbox("Navigate", [
    "Home", 
    "Dataset: Wiki-Vote", 
    "Dataset: Email-Enron", 
    "Dataset: as-skitter"
])

# Static Data
dataset_names = ["Wiki-Vote", "Email-Enron", "as-skitter"]

largest_clique_sizes = {
    "Wiki-Vote": 17,
    "Email-Enron": 20,
    "as-skitter": 67
}

maximal_cliques_count = {
    "Wiki-Vote": 459002,
    "Email-Enron": 226859,
    "as-skitter": 37322355
}

execution_times = {
    "Wiki-Vote": {"Tomita_2006": 5, "ELS": 20, "Chiba_1985": 600},
    "Email-Enron": {"Tomita_2006": 40, "ELS": 20, "Chiba_1985": 700},
    "as-skitter": {"Tomita_2006": 1750, "ELS": 1600}
}

# Clique Size Distributions 
clique_distributions = {
    "Wiki-Vote": {
        2: 8655, 3: 13718, 4: 27292, 5: 48416, 6: 68872,
        7: 83266, 8: 76732, 9: 54456, 10: 35470, 11: 21736,
        12: 11640, 13: 5449, 14: 2329, 15: 740, 16: 208, 17: 23
    },
    "Email-Enron": {
        2: 14070, 3: 7077, 4: 13319, 5: 18143, 6: 22715,
        7: 25896, 8: 24766, 9: 22884, 10: 21393, 11: 17833,
        12: 15181, 13: 11487, 14: 7417, 15: 3157, 16: 1178,
        17: 286, 18: 41, 19: 10, 20: 6
    },
    "as-skitter": {
        2: 2319807, 3: 3171609, 4: 1823321, 5: 939336, 6: 684873,
        7: 598284, 8: 588889, 9: 608937, 10: 665661, 11: 728098,
        12: 798073, 13: 877282, 14: 945194, 15: 980831, 16: 939987,
        17: 839330, 18: 729601, 19: 639413, 20: 600192, 21: 611976,
        22: 640890, 23: 673924, 24: 706753, 25: 753633, 26: 818353,
        27: 892719, 28: 955212, 29: 999860, 30: 1034106, 31: 1055653,
        32: 1017560, 33: 946717, 34: 878552, 35: 809485, 36: 744634,
        37: 663650, 38: 583922, 39: 520239, 40: 474301, 41: 420796,
        42: 367879, 43: 321829, 44: 275995, 45: 222461, 46: 158352,
        47: 99522, 48: 62437, 49: 39822, 50: 30011, 51: 25637,
        52: 17707, 53: 9514, 54: 3737, 55: 2042, 56: 1080,
        57: 546, 58: 449, 59: 447, 60: 405, 61: 283,
        62: 242, 63: 146, 64: 84, 65: 49, 66: 22, 67: 4
    }
}


# Utility to plot clique size distribution
def plot_clique_distribution(dataset_name):
    dist = clique_distributions[dataset_name]
    df = pd.DataFrame({
        "Clique Size": list(dist.keys()),
        "Count": list(dist.values())
    })
    fig = px.bar(df, x="Clique Size", y="Count",
                 title=f"Clique Size Distribution - {dataset_name}",
                 template="plotly_white")
    fig.update_layout(xaxis_title="Clique Size", yaxis_title="Count")
    st.plotly_chart(fig, use_container_width=True)

# Pages
if page == "Home":
    st.title("Clique Analytics Dashboard")
    st.markdown("#### Overview of Algorithms and Datasets")
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Largest Clique Sizes")
        df_largest = pd.DataFrame({
            "Dataset": dataset_names,
            "Largest Clique Size": [largest_clique_sizes[ds] for ds in dataset_names]
        })
        fig_largest = px.bar(
            df_largest,
            x="Largest Clique Size",
            y="Dataset",
            orientation="h",
            color="Dataset",
            title="Largest Clique Size per Dataset",
            template="plotly_dark"  # or "plotly_white" if you prefer
        )
        st.plotly_chart(fig_largest, use_container_width=True)

    with col2:
        st.subheader("Total Number of Maximal Cliques")
        df_maximal = pd.DataFrame({
            "Dataset": dataset_names,
            "Maximal Cliques": [maximal_cliques_count[ds] for ds in dataset_names]
        })
        fig_maximal = px.bar(
            df_maximal,
            x="Maximal Cliques",
            y="Dataset",
            orientation="h",
            color="Dataset",
            title="Total Maximal Cliques per Dataset",
            template="plotly_dark"
        )
        st.plotly_chart(fig_maximal, use_container_width=True)


    st.markdown("### Execution Times for All Algorithms")
    rows = []
    for ds in dataset_names:
        for algo, time in execution_times[ds].items():
            rows.append({"Dataset": ds, "Algorithm": algo, "Execution Time (approx in sec)": time})
    df_exec = pd.DataFrame(rows)
    fig_exec = px.bar(df_exec, x="Dataset", y="Execution Time (approx in sec)", color="Algorithm",
                  barmode="group", template="plotly_white")
    st.plotly_chart(fig_exec, use_container_width=True)


elif page == "Dataset: Wiki-Vote":
    st.title("Dataset Analysis: Wiki-Vote")
    st.markdown("Wikipedia voting network on admin promotions. Directed edges converted to undirected for clique analysis.")
    plot_clique_distribution("Wiki-Vote")

elif page == "Dataset: Email-Enron":
    st.title("Dataset Analysis: Email-Enron")
    st.markdown("Undirected network formed from email exchanges in the Enron corpus.")
    plot_clique_distribution("Email-Enron")

elif page == "Dataset: as-skitter":
    st.title("Dataset Analysis: as-skitter")
    st.markdown("Network of autonomous systems from traceroute data.")
    plot_clique_distribution("as-skitter")
