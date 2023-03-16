FROM ubuntu:latest

RUN apt-get update && apt-get install -y apt-utils apt-transport-https && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get -y install python3 pip && \
    apt-get install -y --no-install-recommends texlive-latex-recommended texlive-fonts-recommended && \
    apt-get install -y --no-install-recommends texlive-latex-extra texlive-fonts-extra texlive-lang-all && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get -y install python3-dev graphviz libgraphviz-dev pkg-config

RUN pip install --upgrade pip
RUN pip install networkx pygraphviz
RUN pip install --index-url https://test.pypi.org/simple/ --no-deps hw1_pestova


ARG USER_ID
ARG GROUP_ID
RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user

WORKDIR workspace/
CMD ["bash"]
