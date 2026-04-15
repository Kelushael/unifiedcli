from setuptools import setup, find_packages

setup(
    name="unified-platform",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.1.0",
        "fastapi>=0.100.0",
        "uvicorn>=0.23.0",
        "requests>=2.31.0",
        "pydantic>=2.0.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "unified-cli=unified.cli:main",
        ],
    },
    python_requires=">=3.10",
)
