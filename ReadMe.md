# LayoutLMv3 Document Classification

This repository contains the code for the document classification task using LayoutLMv3.

# Dataset

The dataset used for this task is the [Document Classification Dataset](https://www.kaggle.com/code/ritvik1909/layoutlmv2-document-classification/data) from Kaggle.

# Prerequisites

1 - Install [Docker](https://docs.docker.com/engine/install/) optional (if you want to run the docker image)

2 - Install [tesseract](https://tesseract-ocr.github.io/tessdoc/Home.html)

# Training

1 - Install dependencies

```bash
pip install -r requirements.txt
```

2 - Run all cells in the notebook `layoutlmv3_training_inference_notebook.ipynb`


# Docker image

1 - Build the docker image

```bash
docker build -t layoutlmv3 .
```

2 - Run the docker image

```bash
docker run -e IMAGE_NAME=(filename) -v (path of dir):/images_dir layoutlmv3
```

# Already built docker image

1 - Pull the docker image

```bash
docker pull ghcr.io/faizankarim/dl_assignment_px_faizankarim
```

2 - Run the docker image

```bash
docker run -e IMAGE_NAME=(filename) -v (path of dir):/images_dir ghcr.io/faizankarim/dl_assignment_px_faizankarim
```