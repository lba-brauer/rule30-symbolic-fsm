import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import itertools
import pandas as pd

# --- Rule 30 Update Function ---
def rule30(x, y, z):
    return x ^ (y | z)

# --- Simulate Rule 30 as 2D Triangle ---
def simulate_rule30(rows=60, width=121):
    center = width // 2
    data = np.zeros((rows, width), dtype=int)
    data[0, center] = 1
    for t in range(1, rows):
        for i in range(1, width - 1):
            left, center_val, right = data[t-1, i-1], data[t-1, i], data[t-1, i+1]
            data[t, i] = rule30(left, center_val, right)
    return data

# --- FSM construction ---
def build_fsm():
    G = nx.DiGraph()
    states = list(itertools.product([0, 1], repeat=3))
    for state in states:
        x, y, z = state
        w = rule30(x, y, z)
        next_state = (y, z, w)
        G.add_edge(state, next_state)
    return G

# --- Validate FSM against simulation ---
def validate_fsm(data):
    errors = []
    for t in range(1, len(data)):
        for i in range(1, len(data[0]) - 1):
            triplet = (data[t-1, i-1], data[t-1, i], data[t-1, i+1])
            expected = rule30(*triplet)
            actual = data[t, i]
            if expected != actual:
                errors.append((t, i, triplet, expected, actual))
    return pd.DataFrame(errors, columns=["Time", "Position", "Triplet", "Expected", "Actual"])

# --- Visualization functions ---
def plot_triangle(data):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(data, cmap='cividis', interpolation='nearest')
    ax.set_title("Rule 30 Simulation Triangle")
    ax.axis('off')
    return fig

def plot_fsm_graph(G):
    pos = nx.spring_layout(G, seed=42)
    fig, ax = plt.subplots(figsize=(10, 6))
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=1200, ax=ax)
    nx.draw_networkx_labels(G, pos, labels={node: str(node) for node in G.nodes()}, ax=ax)
    nx.draw_networkx_edges(G, pos, arrows=True, ax=ax)
    ax.set_title("FSM Transition Graph of Rule 30 (3-bit states)")
    ax.axis('off')
    return fig

# --- Streamlit UI ---
st.title("Rule 30: FSM and Triangle Comparison")

# Triangle Simulation
st.subheader("1. Rule 30 Triangle")
rows = st.slider("Simulation steps (rows)", 20, 200, 60)
width = st.slider("Simulation width (columns)", 21, 201, 121, step=2)
triangle = simulate_rule30(rows, width)
st.pyplot(plot_triangle(triangle))

# FSM Graph
st.subheader("2. Finite State Machine (3-bit transitions)")
fsm = build_fsm()
st.pyplot(plot_fsm_graph(fsm))

# FSM Validation
st.subheader("3. FSM Validation Against Simulation")
errors = validate_fsm(triangle)
if not errors.empty:
    st.dataframe(errors)
else:
    st.success("✅ All transitions are valid.")
