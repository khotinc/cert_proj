FROM devopsedu/webapp
ADD  05_Php/website/ /var/www/html
EXPOSE 80
RUN rm /var/www/html/index.html
CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]
