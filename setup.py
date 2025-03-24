from setuptools import setup, find_packages

setup(
    name="m2f2_rcnn",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "torch",
        "torchvision",
        "opencv-python",
        "numpy",
        "Pillow"
    ]
)
