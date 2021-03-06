from setuptools import setup, find_packages

setup(
    name             = 'niaimage2latex',
    version          = '2.0',
    description      = 'Extract equations from images',
    author           = 'Hyeon Jun Choi',
    author_email     = 'guswns2936@hanmail.net',
    url              = '',
    download_url     = '',
    install_requires = ['Keras-Preprocessing', 'Markdown', 'Pillow>=8.1.0', 'PyQt5', 'PyQt5-Qt5', 'PyQt5-sip',
                        'PyQtWebEngine', 'PyQtWebEngine-Qt5', 'PyWavelets', 'PyYAML>=5.4.1', 'Pygments', 'Shapely',
                        'Werkzeug', 'absl-py', 'albumentations>=0.5.2', 'astunparse', 'bleach', 'cachetools',
                        'certifi', 'chardet>=3.0.4', 'click', 'colorama', 'cycler', 'decorator', 'docutils',
                        'einops>=0.3.0', 'entmax', 'filelock', 'flatbuffers', 'gast', 'google-auth',
                        'google-auth-oauthlib', 'google-pasta', 'grpcio', 'h5py', 'huggingface-hub',
                        'idna', 'imageio', 'imagesize>=1.2.0', 'imgaug', 'importlib-metadata', 'joblib',
                        'keras-nightly', 'keyring', 'kiwisolver', 'latex2mathml', 'libclang', 'matplotlib', 'munch>=2.5.0',
                        'natsort', 'networkx', 'numpy>=1.19.5', 'oauthlib', 'opencv-python>=4.1.1.26', 'opencv-python-headless>=4.1.1.26',
                        'opt-einsum', 'packaging', 'pandas>=1.0.0', 'pip', 'pkginfo', 'protobuf', 'pyasn1',
                        'pyasn1-modules', 'pynput', 'pyparsing', 'python-Levenshtein>=0.12.2', 'python-dateutil', 'pytz',
                        'pywin32-ctypes', 'readme-renderer', 'regex', 'requests>=2.25.1', 'requests-oauthlib',
                        'requests-toolbelt', 'rfc3986', 'rsa', 'sacremoses', 'scikit-image', 'scipy',
                        'screeninfo', 'setuptools', 'six', 'termcolor', 'tifffile', 'timm==0.4.5', 'tokenizers==0.9.4',
                        'torch==1.9.0', 'torchtext==0.10.0', 'torchvision==0.10.0', 'tqdm>=4.47.0', 'transformers>=4.2.2', 'twine', 'typing-extensions',
                        'urllib3', 'webencodings', 'wheel', 'wrapt', 'x-transformers==0.15.0', 'zipp'],
    packages         = find_packages(),
    keywords         = ['latex', 'mathml', 'ocr'],
    python_requires  = '>=3',
    include_package_data=True,
    package_data     = {},
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ]
)
