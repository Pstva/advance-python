FROM ubuntu:latest

RUN apt-get update && apt-get install -y apt-utils apt-transport-https && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get -y install python3 pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install aiohttp aiofiles requests

ARG USER_ID
ARG GROUP_ID
RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user

WORKDIR workspace/
CMD ["bash"]
