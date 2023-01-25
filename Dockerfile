FROM python:3.10-slim as base

FROM base as builder
RUN apt update && apt install -y git gcc g++
RUN pip install --prefix=/install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
ENV PYTHONPATH=/install/lib/python3.10/site-packages:$PYTHONPATH
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --prefix=/install -r requirements.txt

FROM base
COPY --from=builder /install /usr/local
WORKDIR /app
COPY . /app
RUN apt update && apt install -y tesseract-ocr && rm -rf /var/lib/apt/lists/* && python inference.py
ENTRYPOINT ["python", "inference.py"]