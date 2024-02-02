FROM python:alpine

WORKDIR /project_app

COPY . .

RUN pip install --no-cache-dir dash plotly pandas

EXPOSE 8050

CMD ["python", "project.py", "--host", "0.0.0.0", "--port", "8050"]