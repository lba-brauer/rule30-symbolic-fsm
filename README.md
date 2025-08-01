# rule30-symbolic-fsm
Symbolic drift and FSM validation for Wolfram's Rule 30 – with full simulation, analysis, and prize-relevant findings.

This project contains a fully deterministic, symbolic simulation of Wolfram’s Rule 30, along with:

- A visual cellular automaton triangle (like Wolfram’s prize site)
- A finite-state machine based on 3-bit transition windows
- A symbolic drift function tracking density vs. structure
- Full automatic FSM validation against simulation
- Gaussian statistics and Bernoulli analysis of the center column

## 🚀 Run the App

```bash
pip install -r requirements.txt
streamlit run rule30_fsm_streamlit_app.py
