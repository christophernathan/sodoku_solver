from setuptools import setup, find_packages

setup(
    name="sudoku_solver",
    version="1.0",
    description="sudoku demo and game",
    author="Christopher Nathan",
    author_email="christophernathan1217@gmail.com",
    url="https://github.com/christophernathan/sudoku_solver",
    packages=find_packages(),
    install_requires=[
       # 'requests', 'requests-mock', 'python-dotenv', 'pandas', 'pytest'
    ],
    entry_points={
        "console_scripts": [
         #   "bot = bot.__main__:bot"
        ]
    },
)