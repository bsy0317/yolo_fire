import cv2
import os
from ultralytics import YOLO
from src.config import DETECT_CONFIG

def detect_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    output_path = os.path.join(os.path.dirname(video_path), 'detected_' + os.path.basename(video_path))
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 비디오 저장을 위한 VideoWriter 객체 생성
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' 코덱을 사용하여 MP4 형식으로 저장
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    model = YOLO(DETECT_CONFIG['model_path'])
    print(f"Saving detected video to {output_path}")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Object Detection
        results = model(frame)
        annotated_frame = frame.copy()
        # results가 리스트이므로 각 결과에 대해 처리
        for result in results:
            annotated_frame = result.plot()  # 각 결과 객체에서 plot() 사용
        # cv2.imwrite(output_path, annotated_frame)
        out.write(annotated_frame)
        
        # 'q'를 눌러 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()
