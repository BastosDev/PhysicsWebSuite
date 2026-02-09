import streamlit as st

# Page Configuration (Browser Tab Title)
st.set_page_config(
    page_title="Gustavo Bastos | Portfolio",
    page_icon="⚛️",
    layout="centered"
)

# --- HEADER ---
st.title("⚛️ Physics Web Suite")
st.caption("Developed by Gustavo Porto Bastos | IFBA")

st.markdown("---")

# --- INTRODUCTION ---
st.write("""
### Welcome! 👋
This is a suite of interactive physics simulators built in pure **Python**, 
using the **Streamlit** library for web rendering and **Plotly** for vector visualization.

The goal of this project is to transform abstract physics concepts (Electromagnetism and Optics) 
into intuitive visual tools.
""")

# --- NAVIGATION GUIDE ---
st.info("👈 **Use the sidebar menu on the left** to access the simulators.")

st.markdown("""
### 📚 Available Modules:

1.  **🔦 Snell-Descartes Law**: 
    * Light refraction and reflection simulation.
    * Automatic detection of Total Internal Reflection.
    * Real-time vector calculations.

2.  **🌀 Lorentz Force**:
    * 3D visualization of charged particle trajectories.
    * Interaction between magnetic fields and velocity vectors.
""")

# --- FOOTER / CONTACT ---
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("📂 GitHub", "https://github.com/BastosDev")
with col2:
    st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/gustavo-porto-in/")
with col3:
    st.link_button("📧 Email", "mailto:gustavoporto.gp64@gmail.com")