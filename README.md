# ⚛️ Physics Web Suite

**Physics Web Suite** is an interactive web application designed to help students and enthusiasts visualize fundamental physics concepts through real-time simulations.

Built with **Python**, this suite transforms mathematical equations into interactive 2D and 3D models, making abstract concepts in Electromagnetism and Optics intuitive and easy to explore.

## 🚀 Live Demo
Check out the live application here:  
👉 **[physicswebsuitebybastosdev.streamlit.app](https://physicswebsuitebybastosdev.streamlit.app)**

---

## 📚 Key Modules

### 1. 🔦 Snell's Law Simulator (Optics)
A real-time simulation of light behavior at the interface between two media.
* **Refraction & Reflection**: Calculates the angle of refraction based on user-defined indices ($n_1, n_2$).
* **Total Internal Reflection**: Automatically detects and visualizes the reflected ray when the incident angle exceeds the critical angle.
* **Vector Math**: Utilizes NumPy for precise coordinate calculation and ray tracing.

### 2. 🌀 Lorentz Force Simulator (Electromagnetism)
A 3D visualization of a charged particle moving through a magnetic field.
* **3D Trajectory Mapping**: Renders the helical path of the particle using interactive 3D plots.
* **Dynamic Physics Engine**: Users can adjust Charge ($q$), Mass ($m$), Velocity ($\vec{v}$), and Magnetic Field ($\vec{B}$) to instantly observe changes in the cyclotron radius and frequency.
* **Vector Visualization**: Demonstrates the cross product relationship $\vec{F} = q(\vec{v} \times \vec{B})$.

---

## 🛠️ Technologies Used
* **Python 3.x**: Core simulation logic.
* **Streamlit**: Web framework for UI and cloud deployment.
* **Plotly**: Interactive graphing engine for 2D and 3D vector rendering.
* **NumPy**: High-performance library for vector algebra and numerical calculations.

---
