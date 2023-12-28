# mypkg

ROS 2のパッケージ
* 3分タイマー

[![test](https://github.com/yujiando11/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/yujiando11/mypkg/actions/workflows/test.yml)

* ROS 2がインストールされている環境を準備してください

## ノードの説明

### talker.py
* パブリッシャを持つノードであり、トピック`/countup`を通じて1秒ごとにメッセージを送信する
    * トピックに流れるメッセージの型は16ビット符号つき整数である

### listener.py
* サブスクライバーを持つノードであり、トピック`/countup`からメッセージをもらってから経過した時間を表示する。その経過した時間が`180 s`になると`3分経ちました`と出力する
    
### talk_listen.launch.py
* `talker.py`と`listener.py`を一度に立ち上げる


## トピックの説明

### /countup
* 16ビット符号つき整数のメッセージをやりとりするデータ


## 実行方法
* `ros2 run`で実行する方法と`ros2 launch`で実行する方法がある


### `ros2 run`での実行方法
* 端末を2つ用意する

* 端末1
    * ホームディレクトリに移動する
    ```
    $ cd
    ```

    * talker.pyを立ち上げる
    ```
    $ ros2 run mypkg talker
    ```

* 端末2
    * ホームディレクトリに移動する
    ```
    $ cd
    ```

    * listener.pyを立ち上げる
    ```
    $ ros2 run mypkg listener
    ```

### `ros2 launch`での実行方法
* 端末を1つ用意する

    * ホームディレクトリに移動する
    ```
    $ cd
    ```
    
    * talk_listen.launch.pyを立ち上げる
    ```
    $ ros2 launch mypkg talk_listen.launch.py
    ```


## 実行結果

### `ros2 run`での実行結果
* `talker.py` `listener.py`はそれぞれ独立して、互いに通信しています

```
端末1 $ ros2 run mypkg talker
(なにも表示されません)

端末2 $ ros2 run mypkg listener
[INFO] [1703696577.526860959] [listener]:   1 s
[INFO] [1703696578.479243173] [listener]:   2 s
[INFO] [1703696579.479678537] [listener]:   3 s
[INFO] [1703696580.478828219] [listener]:   4 s
[INFO] [1703696581.479544913] [listener]:   5 s
・
・
・
[INFO] [1703696753.479542029] [listener]: 177 s
[INFO] [1703696754.479650744] [listener]: 178 s
[INFO] [1703696755.478888390] [listener]: 179 s
[INFO] [1703696756.479480722] [listener]: 180 s
[INFO] [1703696756.480129287] [listener]: 3分経ちました

```

### `ros2 launch`での実行結果
* `talker.py` `listener.py`はプロセス内通信しています

```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/ando/.ros/log/2023-12-28-02-08-04-810939-LAPTOP-30H05QRF-406
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [408]
[INFO] [listener-2]: process started with pid [410]
[listener-2] [INFO] [1703696886.460646089] [listener]:   1 s
[listener-2] [INFO] [1703696887.447993520] [listener]:   2 s
[listener-2] [INFO] [1703696888.448829933] [listener]:   3 s
[listener-2] [INFO] [1703696889.448411678] [listener]:   4 s
[listener-2] [INFO] [1703696890.447867555] [listener]:   5 s
・
・
・
[listener-2] [INFO] [1703697062.448100268] [listener]: 177 s
[listener-2] [INFO] [1703697063.447837527] [listener]: 178 s
[listener-2] [INFO] [1703697064.448619073] [listener]: 179 s
[listener-2] [INFO] [1703697065.448134570] [listener]: 180 s
[listener-2] [INFO] [1703697065.448869740] [listener]: 3分経ちました

```


## 必要なソフトウェア
* Python
    * テスト済み:3.7~3.10

## テスト環境
* Ubuntu 20.04.6 LTS
* ROS 2 foxy

## 著作権・ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
* このパッケージのコードは、下記のスライド(CC-BY-SA 4.0 by Ryuichi Ueda)のものを一部加筆し、本人の許可を得て自身の著作としたものです。
    * [ryuichiueda/my-slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

© 2023 yujiando11

















