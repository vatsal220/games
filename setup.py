from setuptools import setup, find_packages

setup(
    name = 'gamse',
    version = '0.1',
    author = 'Vatsal Patel',
    license = 'Vatsal',
    description = 'Games to Play',
    long_description = open('README.md').read(),
    long_description_content_type = "text/markdown",
    python_requires = '>=3.7',
    install_requires = [
        'numpy',
    ],
    packages = find_packages(),
    entry_points = {
        'console_scripts' : [
            'tictactoe = games.entrypoints:tictactoe_game',
            'rps = games.entrypoints:rps_game',
            'connect4 = games.entrypoints:connect4_game'
        ]
    },
    package_data = {
        'games' : [
            './tictactoe/*',
            './rockpaperscizors/*',
            './connect4/*',
            './sudoku/*',
            './snake/*'
        ]
    },
    include_package_data = True,
)
