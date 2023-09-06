FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD streamlit run potential_customer_prediction_web_app.py
