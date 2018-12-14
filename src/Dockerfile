FROM python:3.6
WORKDIR /app
ADD ./ /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=server.py
CMD ["flask", "run", "--host=0.0.0.0"]
