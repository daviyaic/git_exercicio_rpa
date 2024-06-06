FROM python

WORKIDIR /app

COPY rpa_python.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD["python", "rpa_python.py"]
