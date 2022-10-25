from threading import Thread
import web_server
import cansatNichrome
import cansatGyro
import cansatGPS
import flightpin
import motor

# TODO GPSの表示が遅れる問題を解決する（多分1秒ごとにしか関数実行してないから）

mode = 0  # 0=気球搭載モード 1=落下中モード 2=パラシュート切り離しモード 3=走行モード


def web_server_boot():
    thread = Thread(target=web_server.web_server_loop)
    thread.daemon = True
    thread.start()


def launching_mode():
    global mode
    # フライトピンの状態を確認
    flightpin.waiting()
    mode += 1


def falling_mode():
    global mode
    web_server_boot()
    # カメラ起動
    # 加速度を取得して落下検知（webからの応答を得る）角度もいっとくか？
    mode += 1


def separating_mode():
    global mode
    # ニクロム線を加熱してテグスを切断する
    cansatNichrome.cutting()
    mode += 1


def running_mode():
    global mode
    motor.GPIO.output(motor.STBY, motor.GPIO.HIGH)
    # モーターを制御、角度を取得
    while True:
        try:
            pass
        except KeyboardInterrupt:
            end()
            exit()



def end():
    motor.end()
    exit()


def mainloop():
    launching_mode()
    falling_mode()
    separating_mode()
    running_mode()


if __name__ == "__main__":
    mainloop()
