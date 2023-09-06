FROM python:3.11.4

COPY . .

ENV PORT="8000"

RUN pip install -r requirements.txt

# CMD ["python", "main.py"]
CMD ["gunicorn", "-w", "5", "-b", "0.0.0.0:8000", "main:app"]

# gunicorn -b "0.0.0.0" main:app
