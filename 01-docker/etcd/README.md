# etcd Dockerfile
I have used debian:latest as base image to this build.
Firstly, we need to deploy the following:
  - git --> In order to clone the etcd source code from github
  - golang --> It is neccessary for etcd to work
  - make --> we will install etcd using make Makefile

next, we do a git clone from github etcd repo, and deploy it on /etcd

For the install, we change the current path to the deployed path (/etcd) and launch "make"

Finally, to achieve a default entrypoint to start the etcd server, we have to define it as CMD and not as ENTRYPOINT, because we wont be able to launch a "etcdctl" command later (A entrypoint cannot be overrided by a command and will be attached). Using CMD, we have a "etcd" as entrypoint, and we can later launch a "etcdctl" command in a run and it will work.

*Dont forget to add the etcdctl path in the ENV environment var
