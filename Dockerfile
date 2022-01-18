FROM python:3.9-slim-bullseye AS pybuild

RUN apt-get -y update \
&& apt-get -y install gcc \
&& apt-get -y clean

FROM pybuild AS pyprod

COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN rm requirements.txt

FROM pyprod AS pydev
RUN pip3 install jupyterlab
EXPOSE 8888
ENTRYPOINT ["jupyter", "lab","--ip=0.0.0.0","--allow-root"]

WORKDIR /home