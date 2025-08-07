import rclpy
from xarm_utils_py import XArmUtils , Node


class ExampleXArmUtils:
    def __init__(self):
        node = Node("example_xarm_utils")

        self.xarm = XArmUtils(node, "xarm6")
        self.target_joint_values = [
            [0.916, 0.724, -1.700, 0.001, 0.977, -0.67],
            [0.916, -0.724, -1.700, 0.001, 0.977, -0.67],
            [-0.916, 0.724, -1.700, 0.001, 0.977, -0.67],
            [-0.105, 0.115, -0.425, -0.231, 0.0151, 0.208],
            [0.916, 0.724, -1.700, 0.001, 0.977, -0.67],
        ]

    def run(self):
        self.count = 0
        for joint_values in self.target_joint_values:
            self.count += 1
            if self.count % 2 == 0:
                self.xarm.set_planning_pipeline("ompl")
            else:
                self.xarm.set_planning_pipeline("stomp")
            self.xarm.set_joint_value_target(joint_values)
            if self.xarm.plan():
                print(f"Plan success for joint values: {joint_values}")
                if self.xarm.execute():
                    print("Execution success")
                else:
                    print("Execution failed")
            else:
                print("Plan failed for joint values:", joint_values)
        print("Moved to initial position")
        self.xarm.move_to_initial()
        rclpy.shutdown()

def main():
    example = ExampleXArmUtils()
    example.run()

if __name__ == '__main__':
    main()
