import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Lorentz Force", page_icon="🌀")

st.title("🌀 Simulador: Força de Lorentz")

st.sidebar.header("Initial Parameters")
q = st.sidebar.number_input("Charge (q) [Coulombs]:", value=1.0, step=0.1)
v = st.sidebar.number_input("Velocity (v) [m/s]:", value=5.0, step=0.1)
b = st.sidebar.number_input("Magnetic Field (B) [Tesla]:", value=1.0, step=0.1)
m = st.sidebar.number_input("Mass (m) [kg]:", value=1.0, step=0.1)
# if q = 0, the force will be zero regardless of the other values
if q == 0:
    st.warning("⚠️ The Lorentz force is zero because the charge (q) is zero.")
elif b == 0:
    st.warning("⚠️ Trajectory is linear because the Magnetic Field (B) is zero.")
else:
    # Creating the time array
    t = np.linspace(0, 20, 1000)  # Time array from 0 to 10 seconds0
    w = (q * b) / m  # Ciclotron frequency
    r = v / w  # Radius of the circular motion
    x_t = r * np.cos(w * t)  # x-coordinate as a function 
    y_t = r * np.sin(w * t)  # y-coordinate as a function
    z_t = (v * 0.1) * t  # z-coordinate as a function of time (linear motion along z-axis)
    
    # Creating the 3D plot
    fig = go.Figure()

    fig.add_trace(go.Scatter3d(
        x=x_t, y=y_t, z=z_t,    
        mode='lines',
        line=dict(width=5, color='#22d3ee'), 
        name='Trajectory'
    ))

    fig.update_layout(
        title="Charged Particle Trajectory",
        template="plotly_dark",
        scene=dict(
            xaxis_title='X (m)',
            yaxis_title='Y (m)',
            zaxis_title='Z (m)',
            aspectmode='cube'
        ),
        height=600,
        margin=dict(r=0, b=0, l=0, t=40)
    )

    st.plotly_chart(fig, use_container_width=True)

    # Math & Stats
    st.markdown("---")
    st.latex(r"\vec{F} = q(\vec{v} \times \vec{B})")
    
    # Creating columns for cleaner stats display
    col1, col2 = st.columns(2)
    col1.metric("Motion Radius", f"{r:.2f} m")
    col2.metric("Cyclotron Frequency", f"{w:.2f} rad/s")