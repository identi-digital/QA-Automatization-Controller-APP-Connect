FROM python:3.10

WORKDIR /app/qa-plataforma

COPY . .

RUN python -m pip install --upgrade pip

RUN pip install -r ./requirements.txt
WORKDIR /app/qa-plataforma

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["main.py"]