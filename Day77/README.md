

# Day 77 — Linear Regression & Data Visualisation with Seaborn 📈

## 100 Days of Code — Python Bootcamp

### 📚 What I Learned

Day 77 focused on **Seaborn**, **linear regression**, and analysing relationships between variables.

The project uses movie budget and revenue data to investigate whether there is a relationship between how much a movie costs to make and how much money it earns.

---

## Seaborn Regression Plot
<img width="1315" alt="day77" src="https://user-images.githubusercontent.com/98851253/167321056-7628596e-75e2-419d-9fec-0d1911beca4d.png">

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook / Google Colab

---

# 📂 Project Dataset

The dataset contains information about movies, including:

- Movie title
- Release date
- Budget
- Revenue

The main objective is to investigate:

> **Does a higher movie budget generally lead to higher revenue?**

---

# 📊 Loading the Dataset

```python
import pandas as pd

df = pd.read_csv("cost_revenue_dirty.csv")
