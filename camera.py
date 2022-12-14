import cv2

QUALITY = 5
encode_param = [int(cv2.IMWRITE_WEBP_QUALITY), QUALITY]

# Webカメラの設定情報
DEVICE_ID = 0

WIDTH = 480
HEIGHT = 270
FPS = 30

# VideoCapture オブジェクトを取得します
capture = cv2.VideoCapture(DEVICE_ID)
# カメラの解像度・FPSの変更
capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
capture.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
capture.set(cv2.CAP_PROP_FPS, FPS)


def get_frames():
    while True:
        ret, frame = capture.read()
        # image = cv2.resize(frame, (480, 270))
        image = frame
        ret, jpg_str = cv2.imencode(".jpeg", image, encode_param)
        yield b"--boundary\r\nContent-Type:image/jpeg\r\n\r\n" + jpg_str.tobytes() + b"\r\n\r\n"


if __name__ == "__main__":
    while True:
        ret, frame = capture.read()
        cv2.imshow("camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()