# Jenkinsfile
In this task i have used a virtual machine, due to lack of resources in the ec2.micro jenkins server. The pipeline job in this server was failing with a "Out of memory" error:

fatal error: runtime: out of memory

So, in order to test the pipeline job, i have launched a jenkins installation in my Ubuntu 14.04 virtual machine (4gb memory) and is has worked.

For this pipeline job, i have configured the following:

- docker-hub jenkins credential. Needed for push the image in docker-hub
- docker-hub new repository: fausst/etcd
- In the jenkins task:
    - Configure a connection with my github repo ( It will do a initial code download)
    - TAG text var. This var will be asigned in the Jenkinsfile for tagging the image.


In the Jenkinsfile, there are 4 steps:

1.- Clone github repo
...
 > git checkout -f 2e0083b10e3d16bbaceaca15503ab6e9198b5cac # timeout=10
Commit message: "Jenkinsfile prueba"

2.- Build etcd with Dockerfile, and tag it
...
Successfully built 9b3e2fad326f
Successfully tagged fausst/etcd:my_tag

3.- Testing the build launching "etcdctl version":
...
[Pipeline] {
[Pipeline] sh (hide)
+ etcdctl version
etcdctl version: 3.5.0-pre
API version: 3.5
[Pipeline] }

4.- Push image in docker-hub
...
+ docker push registry.hub.docker.com/fausst/etcd:my_tag
The push refers to repository [registry.hub.docker.com/fausst/etcd]
...
my_tag: digest: sha256:23cf615d70389f4c02285d0f2bd10047db367d3a37825ecd3f6b0179caacc790 size: 1379
...
Finished: SUCCESS


The jenkins ec2 public IP: http://13.59.12.231:8080/ 
Docker-hub image: https://hub.docker.com/repository/docker/fausst/etcd 

