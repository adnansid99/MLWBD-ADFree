FROM python:3.11.4

COPY . .

RUN pip install -r requirements.txt

# CMD ["python", "main.py"]
# CMD ["gunicorn", "-b", "0.0.0.0", "main:app"]

# gunicorn -b "0.0.0.0" main:app
