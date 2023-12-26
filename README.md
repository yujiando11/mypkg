# mypkg

ROS2のパッケージ

[![test](https://github.com/yujiando11/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/yujiando11/mypkg/actions/workflows/test.yml)

## ノードの説明

### talker.py
* パブリッシャを持つノードであり、トピック`/countup`を通じて1秒ごとにメッセージを送信する
    * トピックに流れるメッセージの型は16ビット符号つき整数である

### listener.py
* サブスクライバーを持つノードであり、トピック`/countup`からメッセージをもらってから経過した時間を表示する
    
### talk_listen.launch.py
* `talker.py`と`listener.py`を一度に立ち上げる


## トピックの説明

### /countup
* 16ビット符号つき整数のメッセージをやりとりするデータ



## ダウンロード方法
* ROS2がインストールされている環境を準備してください

### ホームディレクトリでワークスペースを作成する
```
$ mkdir ros2_ws
```

### ワークスペースに移動する
```
$ cd ros2_ws/
```

### ワークスペースでディレクトリを作成し、移動する
```
$ mkdir src
$ cd src/
```

### 当リポジトリをクローンする
```
$ git clone https://github.com/yujiando11/mypkg.git 
```

### ワークスペースに移動し、ビルドする
```
$ cd ~/ros2_ws/
$ colcon build
```

### 当リポジトリを利用可能にする
```
$ vi ~/.bashrc
```
* ~/.bashrcの末尾に以下の2行を追加する
```
source ~/ros2_ws/install/setup.bash
source ~/ros2_ws/install/local_setup.bash
```

## 実行方法1
* `ros2 run`で実行する
    * 端末を2つ用意する

```
端末1 $ ros2 run mypkg talker
端末2 $ ros2 run mypkg listener
[INFO] [1703141713.490386542] [listener]: 0 s
[INFO] [1703141714.477060126] [listener]: 1 s
[INFO] [1703141715.477431162] [listener]: 2 s
[INFO] [1703141716.477034609] [listener]: 3 s
[INFO] [1703141717.476984585] [listener]: 4 s
[INFO] [1703141718.477023733] [listener]: 5 s 
```

## 実行方法2
* `ros2 launch`で実行する
    * 端末を1つ用意する

```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/ando/.ros/log/2023-12-21-16-03-22-329880-LAPTOP-30H05QRF-1528
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [1530]
[INFO] [listener-2]: process started with pid [1532]
[listener-2] [INFO] [1703142203.911974162] [listener]: 0 s
[listener-2] [INFO] [1703142204.900762271] [listener]: 1 s
[listener-2] [INFO] [1703142205.900151024] [listener]: 2 s
[listener-2] [INFO] [1703142206.900088615] [listener]: 3 s
[listener-2] [INFO] [1703142207.900285177] [listener]: 4 s
[listener-2] [INFO] [1703142208.900146352] [listener]: 5 s
```

## 必要なソフトウェア
* Python
    * テスト済み:3.7~3.10

## テスト環境
* Ubuntu 20.04
* ROS2 foxy

## 著作権・ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
* このパッケージのコードは、下記のスライド(CC-BY-SA 4.0 by Ryuichi Ueda)のものを一部加筆し、本人の許可を得て自身の著作としたものです。
    * [ryuichiueda/my-slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

© 2023 yujiando11

















