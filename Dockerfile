
FROM centos:latest

MAINTAINER blx

RUN yum -y install httpd; systemctl enable httpd.service

RUN yum -y install mariadb-server mariadb; systemctl enable mariadb.service

RUN yum clean all

EXPOSE 80

CMD ["/usr/sbin/init"]


