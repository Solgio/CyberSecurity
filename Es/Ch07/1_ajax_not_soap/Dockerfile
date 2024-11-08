FROM php:5.6-apache

MAINTAINER Zane Durkin <zane@neverlanctf.com>
RUN sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list && \
    sed -i '/security.debian.org/d' /etc/apt/sources.list && \
    sed -i '/stretch-updates/d' /etc/apt/sources.list
RUN apt-get update --fix-missing
RUN a2enmod rewrite

COPY web/ /var/www/html
