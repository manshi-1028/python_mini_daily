
# Day 78 — Analysing the Nobel Prize with Plotly, Seaborn & Matplotlib 🏆📊

## 100 Days of Code — Python Bootcamp

### 📚 What I Learned

Day 78 focused on **exploratory data analysis and visualisation** using the Nobel Prize dataset.

The project involved investigating Nobel Prize winners and answering questions such as:

- Which countries have produced the most Nobel laureates?
- Which gender has received more Nobel Prizes?
- How has the distribution changed over time?
- Which category has the most prizes?
- Are Nobel Prize winners becoming younger?
- Who was the youngest Nobel Prize winner?

---


## Nobel Prize Analysis
<img width="1298" alt="day78(1)" src="https://user-images.githubusercontent.com/98851253/167689730-fded30a6-0d56-4a84-9446-db0ad87c3309.png">
<img width="1299" alt="day78(2)" src="https://user-images.githubusercontent.com/98851253/167689732-e8255e50-1aa1-4db9-bb28-eaae9570aa83.png">
<img width="1295" alt="day78(3)" src="https://user-images.githubusercontent.com/98851253/167689734-e872ce2e-7c65-45e8-ae3b-603a74edbaf7.png">

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook

---

# 📂 Dataset

The Nobel Prize dataset contains information about Nobel laureates, including:

- Name
- Birth date
- Birth country
- Sex
- Prize category
- Prize year
- Motivation
- Organization

Load the dataset:

```python
import pandas as pd

df = pd.read_csv("nobel_prize_data.csv")
