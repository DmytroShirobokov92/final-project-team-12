from setuptools import setup, find_packages

setup(
    name="final_project_team_12",
    version="0.1.0",
    packages=find_packages(include=['include', 'include.*']),
    install_requires=[
        'colorama==0.4.6'
    ],
    entry_points={
        'console_scripts': [
            'bot = bot:main',
        ],
    },
    author="team-12",
    author_email="team-12@gmail.com",
    description="Python package for managing contacts and notes",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
