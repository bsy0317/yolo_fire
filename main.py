import argparse
from src.train import train_model
from src.detect import detect_from_video
from src.config import MODEL_CONFIG

def main():
    parser = argparse.ArgumentParser(description="Fire, Smoke Detection using YOLOv11")
    
    parser.add_argument('--train', action='store_true', help="Start training")
    parser.add_argument('--detect', action='store_true', help="Object detection")
    parser.add_argument('--file', type=str, help="Video file path for detection")

    args = parser.parse_args()
    if args.train:
        try:
            train_model()
        finally:
            print("TensorBoard process terminated.")

    elif args.detect:
        if args.file:
            detect_from_video(args.file)
        else:
            print("Error: --detect requires --file to specify the video file path.")
    else:
        print("Please specify either --train or --detect with a valid file.")

if __name__ == '__main__':
    main()
