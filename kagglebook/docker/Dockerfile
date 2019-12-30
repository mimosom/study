# cf. https://github.com/ghmagazine/kagglebook

FROM ubuntu:18.04
RUN apt-get -y update && apt-get -y upgrade

# Install requirements
RUN apt-get install -y \
    git \
    wget \
    build-essential \
    libatlas-base-dev \
    python3-dev

# Install anaconda3
RUN wget --quiet https://repo.continuum.io/archive/Anaconda3-2019.03-Linux-x86_64.sh \
    -O lib/anaconda.sh && \
    chmod +x lib/anaconda.sh && \
    /bin/bash lib/anaconda.sh -b && \
    echo export PATH=~/anaconda3/bin:$PATH >> ~/.bashrc

# Install python packages
RUN ~/anaconda3/bin/pip install \
    scikit-learn==0.21.2 \
    xgboost==0.81 \
    lightgbm==2.2.2 \
    tensorflow==1.14.0 \
    keras==2.2.4 \
    hyperopt==0.1.1 \
    bhtsne==0.1.9 \
    rgf_python==3.4.0 \
    umap-learn==0.3.
