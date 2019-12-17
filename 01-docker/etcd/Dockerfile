FROM debian:latest

RUN apt-get update
RUN apt-get install -y git golang make

RUN git clone https://github.com/etcd-io/etcd.git

WORKDIR /etcd

ENV PATH="/etcd/bin:${PATH}"

RUN make 

CMD ["etcd"]
