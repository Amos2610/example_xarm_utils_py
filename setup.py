from setuptools import setup

package_name = 'example_xarm_utils_py'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Soma Fumoto',
    maintainer_email='g5mcb011@eng.kitakyu-u.ac.jp',
    description='Python CLI for xarm_utils_cpp (pybind11 bridge)',
    entry_points={
        'console_scripts': [
            'example_xarm_utils_py = example_xarm_utils_py.example_xarm_utils:main',
        ],
    },
)
