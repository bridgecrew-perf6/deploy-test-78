from setuptools import setup, find_packages

setup(
    name="sunny_bikes",
    packages=find_packages(exclude='tests'),
    version="0.1.0",
    install_requires=[
        "Flask==1.0.2",
    ],
    extras_require={
        "dev": [
            "flake8==3.8.4",
            "pytest==5.4.3",
        ]
    },
    python_requires=">=3.7",
)
