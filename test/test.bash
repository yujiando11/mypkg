#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'season:
      ・春:少しずつ暖かくなり過ごしやすいです。桜の花が咲きます。
      ・夏:雨がたくさん降る時期があり、その後暑さが増します。夏祭りや花火があります。
      ・秋:暑さがやわらぎます。紅葉がよく見られます。
      ・冬:気温が下がり、寒さが増します。雪景色が見られます。'
