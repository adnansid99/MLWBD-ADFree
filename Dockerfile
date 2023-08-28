FROM python:3.11.4

COPY . .

RUN pip install --force-reinstall -r requirements.txt

# CMD ["python", "main.py"]
CMD ["gunicorn", "main:app"]