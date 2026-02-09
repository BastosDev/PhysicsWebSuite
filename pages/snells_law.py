import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Snell's Law", page_icon="🔦")

st.title("🔦 Snell's Law Simulator")

st.sidebar.header("Input Parameters")
n1 = st.sidebar.number_input("Refractive Index 1 (n1):", value=1.5, step=0.01)
n2 = st.sidebar.number_input("Refractive Index 2 (n2):", value=1.0, step=0.01)
theta1_d = st.sidebar.number_input("Angle of Incidence (°):", value=45.0, step=1.0)

theta1_r = np.radians(theta1_d)
arg = (n1/n2) * np.sin(theta1_r)

total_reflection = False
theta2_d = 0.0


if arg > 1.0:
    total_reflection = True
    st.error("🚨 Total Internal Reflection! The incident angle exceeds the critical angle.")
else:
    theta2_r = np.arcsin(arg)
    theta2_d = np.degrees(theta2_r)
    st.success(f"Angle of Refraction: {theta2_d:.2f}°")
    
# Coordinates for plotting the rays
height = 1.0

# Incident Ray
x_start = -height * np.tan(theta1_r)
x_inc = [x_start, 0]
y_inc = [height, 0]

# Resulting Ray
if total_reflection:
    # Reflection
    x_out = height * np.tan(theta1_r) 
    x_ref = [0, x_out]
    y_ref = [0, height] # Goes back up
    ray_color = "red"
    ray_name = "Reflected Ray (Total)"
else:
    # Refraction
    x_out = height * np.tan(theta2_r)
    x_ref = [0, x_out]
    y_ref = [0, -height]
    ray_color = "#4ade80"
    ray_name = "Refracted Ray"

# --- Plotly ---
fig = go.Figure()

# Interface Line
fig.add_trace(go.Scatter(
    x=[-2, 2], y=[0, 0], mode='lines', 
    line=dict(color='white', width=2), name='Interface'
))

# Normal Line
fig.add_trace(go.Scatter(
    x=[0, 0], y=[-1, 1], mode='lines', 
    line=dict(color='gray', width=1, dash='dash'), name='Normal'
))

# Incident Ray
fig.add_trace(go.Scatter(
    x=x_inc, y=y_inc, mode='lines+markers',
    line=dict(color='#22d3ee', width=4), name='Incident Ray'
))

# Resulting Ray
fig.add_trace(go.Scatter(
    x=x_ref, y=y_ref, mode='lines+markers',
    line=dict(color=ray_color, width=4), name=ray_name
))

fig.update_layout(
    title="Optical Visualization",
    template="plotly_dark",
    xaxis=dict(range=[-1.5, 1.5], title="X Position"),
    yaxis=dict(range=[-1.1, 1.1], title="Y Position", scaleanchor="x"),
    height=500
)

st.plotly_chart(fig, use_container_width=True)