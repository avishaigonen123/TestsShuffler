from setuptools import setup, find_packages

setup(
    name='TestsShuffler',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'blinker==1.7.0',
        'click==8.1.7',
        'colorama==0.4.6',
        'Flask==3.0.0',
        'itsdangerous==2.1.2',
        'Jinja2==3.1.2',
        'MarkupSafe==2.1.3',
        'numpy==1.26.2',
        'opencv-python==4.8.1.78',
        'packaging==23.2',
        'pdf2image==1.16.3',
        'Pillow==10.0.0',
        'PyPDF4==1.27.0',
        'pytesseract==0.3.10',
        'Werkzeug==3.0.1',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
		'run-server=TestsShuffler.server.server.py:__main__'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
