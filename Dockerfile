#FROM pytorch/pytorch:1.4-cuda10.1-cudnn7-runtime
FROM pytorch/pytorch:1.9.0-cuda11.1-cudnn8-runtime
ENV PYTHONUNBUFFERED 1

COPY . /app/coral-ocr
WORKDIR /app/coral-ocr
RUN chmod -R 777 .

RUN  sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y libsm6
RUN apt-get install -y libxrender1
RUN apt-get install -y --no-install-recommends 	autoconf automake bzip2 dpkg-dev file g++ gcc imagemagick libbz2-dev libc6-dev libcurl4-openssl-dev libdb-dev libevent-dev libffi-dev libgdbm-dev libglib2.0-dev libgmp-dev libjpeg-dev libkrb5-dev liblzma-dev libmagickcore-dev libmagickwand-dev libmaxminddb-dev libncurses5-dev libncursesw5-dev 	libpng-dev libpq-dev libreadline-dev libsqlite3-dev libssl-dev 	libtool libwebp-dev libxml2-dev libxslt-dev libyaml-dev patch unzip xz-utils zlib1g-dev ffmpeg libsm6 libxext6

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

RUN pip install --upgrade pip && pip --default-timeout=1000 install  -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
RUN pip install "paddleocr>=2.0.1" -i https://pypi.tuna.tsinghua.edu.cn/simple

ENTRYPOINT ["gunicorn","-c", "gunicorn.py", "app:app"]
