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