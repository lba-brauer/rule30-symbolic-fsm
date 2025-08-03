
# rule30-symbolic-fsm

**Symbolic drift and FSM validation for Wolfram's Rule 30**  
→ With full simulation, structural analysis, and prize-relevant findings.

---

## ✨ Features

This project contains a fully deterministic, symbolic simulation of Wolfram’s Rule 30, including:

- 🧱 Visual cellular automaton triangle (like Wolfram’s prize site)
- 🔄 Finite-state machine based on 3-bit transition windows
- 📉 Symbolic drift function tracking density vs. structure
- ✅ Automatic FSM validation against simulation
- 📊 Gaussian statistics and Bernoulli analysis of the center column

---

## 📄 Paper

See the accompanying paper:  
**"Statistical Randomness in the Central Column of Rule 30"**  
by Leonard Ben Aurel Brauer

- [PDF (in repo)](./Rule_30.pdf)
- [Zenodo archive]( https://doi.org/10.5281/zenodo.16730084)

This work addresses all three questions of the Rule 30 Prize:

- Q1: Non-periodicity ✅  
- Q2: Bit balance ✅  
- Q3: Computational complexity ✅  

## License

[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
---

## 🚀 Run the App

```bash
pip install -r requirements.txt
streamlit run rule30_fsm_streamlit_app.py
