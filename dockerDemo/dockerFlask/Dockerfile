FROM python:3.7
LABEL maintainer="1392133729@qq.com"
WORKDIR /app
ADD . /app
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple flask
EXPOSE 5003
CMD ["python", "app.py"]
