# example_xarm_utils_py

Pythonラッパーパッケージ  
xArm6のMoveIt2操作用C++ユーティリティ（xarm_utils_cpp）のPythonバインディングを用いたサンプル実装です。

---

## 概要

- `xarm_utils_cpp` のpybind11ラッパーを利用して、PythonからROS2のMoveIt2経由でxArm6を操作します
- Pythonの `rclpy` ノードを用いてC++ノードと連携
- 基本的な動作例を `example_xarm_utils.py` に実装

---

## ファイル構成
```
example_xarm_utils_py/
├── example_xarm_utils_py/
│ ├── init.py
│ └── example_xarm_utils.py # メインのサンプルコード
├── package.xml
├── setup.py
├── setup.cfg
└── README.md
```

## インストール方法

ROS2ワークスペースのルートで以下を実行します。

```bash
cd <your_ros2_workspace>/src
git clone git@github.com:Amos2610/example_xarm_utils_py.git
cd <your_ros2_workspace>
colcon build --packages-select example_xarm_utils_py
source install/setup.bash
```

## 実行方法
xArm6を操作するためのノードを起動します。

```bash
ros2 run example_xarm_utils_py example_xarm_utils_py
```

## 使い方サンプル
以下のように、PythonスクリプトからxArm6を操作できます。
example_xarm_utils_py/example_xarm_utils.pyより抜粋：
```python
import rclpy
from xarm_utils_py import XArmUtils , Node


class ExampleXArmUtils:
    def __init__(self):
        node = Node("example_xarm_utils")

        self.xarm = XArmUtils(node, "xarm6")

    def run(self):
        # set planning pipeline
        self.xarm.set_planning_pipeline("stomp") # stomp or ompl

        # set target joint values
        joint_values = [0.916, 0.724, -1.700, 0.001, 0.977, -0.67] # 任意の関節角度を設定
        self.xarm.set_joint_value_target(joint_values)
        if self.xarm.plan(): # プランニングを実行
            print(f"Plan success for joint values: {joint_values}")
            if self.xarm.execute(): # プランが成功したら実行
                print("Execution success")
            else:
                print("Execution failed")
        else:
            print("Plan failed for joint values:", joint_values)

        # Move to initial position
        print("Moved to initial position")
        self.xarm.move_to_initial()
        rclpy.shutdown()

def main():
    example = ExampleXArmUtils()
    example.run()

if __name__ == '__main__':
    main()
```
