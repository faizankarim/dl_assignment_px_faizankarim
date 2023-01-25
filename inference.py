from PIL import Image
import torch
from transformers import LayoutLMv3FeatureExtractor, LayoutLMv3Tokenizer, LayoutLMv3Processor, \
    LayoutLMv3ForSequenceClassification
import os


def predict():
    label2idx = {'email': 0, 'resume': 1, 'scientific_publication': 2}

    feature_extractor = LayoutLMv3FeatureExtractor(apply_ocr=True, ocr_lang='eng')
    tokenizer = LayoutLMv3Tokenizer.from_pretrained("microsoft/layoutlmv3-base")
    processor = LayoutLMv3Processor(feature_extractor, tokenizer)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = LayoutLMv3ForSequenceClassification.from_pretrained("saved_model")
    model.to(device)
    image = Image.open('/images_dir/' + os.environ['IMAGE_NAME']).convert("RGB")
    encoded_inputs = processor(image, padding="max_length", truncation=True, return_tensors="pt").to(device)
    outputs = model(**encoded_inputs)
    preds = torch.softmax(outputs.logits, dim=1).tolist()[0]
    pred_labels = {label: pred for label, pred in zip(label2idx.keys(), preds)}
    print('prediction: ', pred_labels)


if __name__ == '__main__':
    try:
        predict()
    except Exception as e:
        print(e)
