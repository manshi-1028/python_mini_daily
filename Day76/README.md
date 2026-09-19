
# Day 76 — Beautiful Plotly Charts & Analysing the Android App Store 📱📊

## 100 Days of Code — Python Bootcamp

### 📚 What I Learned

Day 76 focused on **data cleaning, exploratory data analysis, and interactive data visualisation with Plotly**.

The project analysed data from the **Android App Store** to understand app categories, ratings, reviews, installs, prices, and popularity.

---

<img width="439" alt="day76(1)" src="https://user-images.githubusercontent.com/98851253/167261942-5fd48d7d-8ac7-4c73-93ad-a44ab46cd1ab.png">
<img width="431" alt="day76(2)" src="https://user-images.githubusercontent.com/98851253/167261943-c25af1f7-a7c4-4860-9344-c138ab6a8bfb.png">

## 🛠️ Technologies Used

- Python
- Pandas
- Plotly
- Jupyter Notebook / Google Colab
- CSV datasets

---

# 📂 Project Dataset

The project works with Android app store data containing information such as:

- App name
- Category
- Rating
- Reviews
- Size
- Installs
- Type
- Price
- Content Rating
- Genres

The main goal was to clean the dataset and then create visualisations to discover patterns.

---

# 🧹 Data Cleaning

Before visualising the data, the dataset needs to be cleaned.

### Load the dataset

```python
import pandas as pd

df = pd.read_csv("apps.csv")
