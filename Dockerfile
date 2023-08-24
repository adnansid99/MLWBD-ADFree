FROM python:3.11.4

COPY . .

RUN pip install --force-reinstall -r requirements.txt

CMD ["gunicorn", "-w", "2", "main:app"]