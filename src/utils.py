import os
import logging

def setup_logging(log_file='training.log'):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

def save_model(model, save_dir, model_name='fire_model.pt'):
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, model_name)
    model.save(save_path)
    logging.info(f"Model saved at {save_path}")
