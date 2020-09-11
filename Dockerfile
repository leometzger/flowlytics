FROM centos/python-36-centos7 

COPY requirements.txt /app/requirements.txt

WORKDIR /silk
RUN yum -y install epel-release \
  && yum -y update epel-release \
  && yum -y install wget \
  && yum -y install libuv1 \
  && yum -y install libuv1-dev \
  && yum -y install centos-release-scl-rh \
  && wget --no-check-certificate https://forensics.cert.org/cert-forensics-tools-release-el7.rpm \
  && yum -y install cert-forensics-tools-release-el7.rpm \
  && yum -y install libfixbuf \
  && yum -y install silk-common silk-analysis \
  && chmod go+rx /var/silk /var/silk/data

# Copy files
COPY silk/silk.conf /var/silk/data/silk.conf
COPY silk/sensors.conf /var/silk/sensors.conf

# Python part
COPY ./src /src

WORKDIR /src
RUN python -m venv venv \
  && /src/venv/bin/pip install -r requirements.txt


