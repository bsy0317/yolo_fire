# 모델 설정
MODEL_CONFIG = {
    "model_architecture": "yolo11n.pt",  # YOLO 모델 아키텍처 (yolo11n.pt, yolo11s.pt, yolo11m.pt, yolo11l.pt, yolo11x.pt)
    "epochs": 50,  # 학습할 Epoch 수
    "batch": 16,  # 배치 크기
    "data_yaml_path": "./datasets/data.yaml",  # 데이터셋 경로
    "save_dir": "./weights",  # 모델, 로그 저장경로
}

# 객체 감지 설정
DETECT_CONFIG = {
    "model_path": "./weights/fire_model.pt",  # 가중치 모델 경로
    "confidence_threshold": 0.8,  # 감지 신뢰도 임계값
}
