import pandas as pd
from sklearn.linear_model import LinearRegression
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Load dataset
data = pd.read_csv("house_data.csv")

# Features & Target
X = data[['Area', 'Bedrooms', 'Bathrooms', 'Age']]
y = data['Price']

# Train Model
model = LinearRegression()
model.fit(X, y)

# ---------------- UI ----------------
app = tb.Window(themename="superhero")  # modern theme
app.title("🏠 House Price Prediction")
app.geometry("500x500")

title = tb.Label(
    app,
    text="House Price Prediction System",
    font=("Helvetica", 18, "bold"),
    bootstyle="primary"
)
title.pack(pady=20)

# Inputs
area = tb.Entry(app)
area.pack(pady=10)
area.insert(0, "Enter Area (sq ft)")

bedrooms = tb.Entry(app)
bedrooms.pack(pady=10)
bedrooms.insert(0, "Enter Bedrooms")

bathrooms = tb.Entry(app)
bathrooms.pack(pady=10)
bathrooms.insert(0, "Enter Bathrooms")

age = tb.Entry(app)
age.pack(pady=10)
age.insert(0, "Enter Age of House")

result_label = tb.Label(app, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# Prediction Function
def predict_price():
    try:
        a = float(area.get())
        b = float(bedrooms.get())
        c = float(bathrooms.get())
        d = float(age.get())

        prediction = model.predict([[a, b, c, d]])
        result_label.config(
            text=f"🏡 Predicted Price: ₹ {int(prediction[0])}",
            bootstyle="success"
        )
    except:
        result_label.config(text="❌ Enter valid numbers", bootstyle="danger")

# Button
btn = tb.Button(
    app,
    text="Predict Price",
    bootstyle="success",
    command=predict_price
)
btn.pack(pady=10)

app.mainloop()