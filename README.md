Enviroment library

absl-py                 1.1.0
aiocontextvars          0.2.2
aiohttp                 3.8.1
aiosignal               1.2.0
asgiref                 3.5.2
astor                   0.8.1
astunparse              1.6.3
async-timeout           4.0.1
asynctest               0.13.0
attrs                   21.4.0
blinker                 1.4
brotlipy                0.7.0
cachetools              4.2.4
certifi                 2022.6.15
cffi                    1.15.0
charset-normalizer      2.0.12
click                   8.0.4
colorama                0.4.5
concurrent-videocapture 0.0.2
contextvars             2.4
cryptography            3.4.8
dataclasses             0.8
Django                  3.2.14
easydict                1.9
frozenlist              1.2.0
gast                    0.3.3
google-auth             1.35.0
google-auth-oauthlib    0.4.6
google-pasta            0.2.0
grpcio                  1.47.0
h5py                    2.10.0
idna                    3.3
image                   1.5.33
immutables              0.18
importlib-metadata      4.11.3
importlib-resources     5.4.0
Keras                   2.4.0
Keras-Applications      1.0.8
Keras-Preprocessing     1.1.2
loguru                  0.6.0
lxml                    4.9.1
Markdown                3.3.7
mkl-fft                 1.3.1
mkl-random              1.2.2
mkl-service             2.4.0
msgpack                 1.0.2
multidict               5.1.0
numpy                   1.18.5
oauthlib                3.2.0
onnx                    1.13.0
onnxconverter-common    1.13.0
opencv-python           4.6.0.66
opt-einsum              3.3.0
packaging               22.0
Pillow                  9.2.0
pip                     21.2.4
protobuf                3.20.3
psutil                  5.9.1
pyasn1                  0.4.8
pyasn1-modules          0.2.8
pycparser               2.21
PyJWT                   2.1.0
pyOpenSSL               21.0.0
pyreadline              2.1
PySocks                 1.7.1
pytz                    2022.1
PyYAML                  6.0
requests                2.28.0
requests-oauthlib       1.3.1
rsa                     4.8
scipy                   1.4.1
setuptools              61.2.0
signalrcore             0.9.5
six                     1.16.0
sqlparse                0.4.2
tensorboard             2.11.0
tensorboard-data-server 0.6.1
tensorboard-plugin-wit  1.8.1
tensorflow              2.3.0
tensorflow-estimator    2.3.0
termcolor               1.1.0
tqdm                    4.64.0
typing_extensions       4.1.1
urllib3                 1.26.9
websocket-client        1.0.0
Werkzeug                2.0.3
wheel                   0.37.1
win-inet-pton           1.1.0
win32-setctime          1.1.0
wincertstore            0.2
wrapt                   1.14.1
yarl                    1.6.3
zipp                    3.8.0

(qm-env) C:\Users\melek.turan>pip install onnxruntime
Collecting onnxruntime
  Using cached onnxruntime-1.13.1-cp37-cp37m-win_amd64.whl (5.9 MB)
Requirement already satisfied: protobuf in c:\users\melek.turan\anaconda3\envs\qm-env\lib\site-packages (from onnxruntime) (3.20.3)
Requirement already satisfied: packaging in c:\users\melek.turan\anaconda3\envs\qm-env\lib\site-packages (from onnxruntime) (22.0)
Collecting flatbuffers
  Downloading flatbuffers-23.1.4-py2.py3-none-any.whl (26 kB)
Collecting sympy
  Using cached sympy-1.10.1-py3-none-any.whl (6.4 MB)
Collecting numpy>=1.21.6
  Using cached numpy-1.21.6-cp37-cp37m-win_amd64.whl (14.0 MB)
Collecting coloredlogs
  Using cached coloredlogs-15.0.1-py2.py3-none-any.whl (46 kB)
Collecting humanfriendly>=9.1
  Using cached humanfriendly-10.0-py2.py3-none-any.whl (86 kB)
Requirement already satisfied: pyreadline in c:\users\melek.turan\anaconda3\envs\qm-env\lib\site-packages (from humanfriendly>=9.1->coloredlogs->onnxruntime) (2.1)
Collecting mpmath>=0.19
  Using cached mpmath-1.2.1-py3-none-any.whl (532 kB)
Installing collected packages: mpmath, humanfriendly, sympy, numpy, flatbuffers, coloredlogs, onnxruntime
  Attempting uninstall: numpy
    Found existing installation: numpy 1.18.5
    Uninstalling numpy-1.18.5:
      Successfully uninstalled numpy-1.18.5
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
tensorflow 2.3.0 requires numpy<1.19.0,>=1.16.0, but you have numpy 1.21.6 which is incompatible.
Successfully installed coloredlogs-15.0.1 flatbuffers-23.1.4 humanfriendly-10.0 mpmath-1.2.1 numpy-1.21.6 onnxruntime-1.13.1 sympy-1.10.1

(qm-env) C:\Users\melek.turan>pip list
Package                 Version
----------------------- ---------
absl-py                 1.1.0
aiocontextvars          0.2.2
aiohttp                 3.8.1
aiosignal               1.2.0
asgiref                 3.5.2
astor                   0.8.1
astunparse              1.6.3
async-timeout           4.0.1
asynctest               0.13.0
attrs                   21.4.0
blinker                 1.4
brotlipy                0.7.0
cachetools              4.2.4
certifi                 2022.6.15
cffi                    1.15.0
charset-normalizer      2.0.12
click                   8.0.4
colorama                0.4.5
coloredlogs             15.0.1
concurrent-videocapture 0.0.2
contextvars             2.4
cryptography            3.4.8
dataclasses             0.8
Django                  3.2.14
easydict                1.9
flatbuffers             23.1.4
frozenlist              1.2.0
gast                    0.3.3
google-auth             1.35.0
google-auth-oauthlib    0.4.6
google-pasta            0.2.0
grpcio                  1.47.0
h5py                    2.10.0
humanfriendly           10.0
idna                    3.3
image                   1.5.33
immutables              0.18
importlib-metadata      4.11.3
importlib-resources     5.4.0
Keras                   2.4.0
Keras-Applications      1.0.8
Keras-Preprocessing     1.1.2
loguru                  0.6.0
lxml                    4.9.1
Markdown                3.3.7
mkl-fft                 1.3.1
mkl-random              1.2.2
mkl-service             2.4.0
mpmath                  1.2.1
msgpack                 1.0.2
multidict               5.1.0
numpy                   1.21.6
oauthlib                3.2.0
onnx                    1.13.0
onnxconverter-common    1.13.0
onnxruntime             1.13.1
opencv-python           4.6.0.66
opt-einsum              3.3.0
packaging               22.0
Pillow                  9.2.0
pip                     21.2.4
protobuf                3.20.3
psutil                  5.9.1
pyasn1                  0.4.8
pyasn1-modules          0.2.8
pycparser               2.21
PyJWT                   2.1.0
pyOpenSSL               21.0.0
pyreadline              2.1
PySocks                 1.7.1
pytz                    2022.1
PyYAML                  6.0
requests                2.28.0
requests-oauthlib       1.3.1
rsa                     4.8
scipy                   1.4.1
setuptools              61.2.0
signalrcore             0.9.5
six                     1.16.0
sqlparse                0.4.2
sympy                   1.10.1
tensorboard             2.11.0
tensorboard-data-server 0.6.1
tensorboard-plugin-wit  1.8.1
tensorflow              2.3.0
tensorflow-estimator    2.3.0
termcolor               1.1.0
tqdm                    4.64.0
typing_extensions       4.1.1
urllib3                 1.26.9
websocket-client        1.0.0
Werkzeug                2.0.3
wheel                   0.37.1
win-inet-pton           1.1.0
win32-setctime          1.1.0
wincertstore            0.2
wrapt                   1.14.1
yarl                    1.6.3
zipp                    3.8.0

onnx_convert dosyası çalıştırılarak dönüşüm gerçekleştirilir.

Cuda 10.1 cudnn cudart64_101

Onnx_run ile test gerçekleştirilir.
