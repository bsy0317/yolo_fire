from ultralytics import YOLO
from src.utils import save_model, setup_logging
from src.config import MODEL_CONFIG
import logging
import torch
def train_model():
    setup_logging()
    device = 'cpu'
    device = torch.device(device if torch.cuda.is_available() else 'cpu')
    if torch.backends.mps.is_available():
        device = 'mps'
    print('Device:', device)
    
    model = YOLO(
        MODEL_CONFIG['model_architecture'],
        verbose=False,
    )

    logging.info("Starting training...")

    results = model.train(
        data=MODEL_CONFIG['data_yaml_path'], 
        epochs=MODEL_CONFIG['epochs'],
        batch=MODEL_CONFIG['batch'],
        project=MODEL_CONFIG['save_dir'],
        name="exp",
        device=device,
        save=True
    )

    save_model(model, MODEL_CONFIG['save_dir'])

if __name__ == '__main__':
    # https://docs.ultralytics.com/ko/guides/yolo-performance-metrics/
    train_model()
