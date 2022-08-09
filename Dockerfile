FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
