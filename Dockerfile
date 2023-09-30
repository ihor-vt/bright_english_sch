FROM python:3.9

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . $APP_HOME/

RUN apt-get update && apt-get install -y sqlite3 && chmod +x /usr/bin/sqlite3

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR $APP_HOME/english_school

CMD ["gunicorn", "english_school.wsgi:application", "--bind", "0.0.0.0:8000"]
