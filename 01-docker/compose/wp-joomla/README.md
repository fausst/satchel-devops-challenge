# WP-Joomla
To achieve this i have used a nginx-proxy as a proxy container: jwilder/nginx-proxy
With it, i have added 2 services, joomla and wordpress, and declared the environment var VIRTUAL_HOST pointing to the names configured in /etc/hosts.
In this way i have now 2 containers added to a proxy server serving on port 80.
2 more services has been declared in compose-file as databases for joomla and wordpress, and has been isolated in a specific network and persisted in a specific volume.
For the proxy to work, both networks has been added in the compose-file too.
At the end, i have the following containers:

$ docker ps
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                NAMES
f0e8a4efdb39        joomla:latest         "/entrypoint.sh apac…"   11 minutes ago      Up 11 minutes       80/tcp               composejoomla_joomla_1
4e255b0d9132        wordpress:latest      "docker-entrypoint.s…"   11 minutes ago      Up 11 minutes       80/tcp               composejoomla_wordpress_1
04e2445d767d        mariadb:10.2          "docker-entrypoint.s…"   11 minutes ago      Up 11 minutes       3306/tcp             composejoomla_db_joomla_1
41ad28ebd149        mariadb:10.2          "docker-entrypoint.s…"   11 minutes ago      Up 11 minutes       3306/tcp             composejoomla_db_wordpress_1
3c046f73cca4        jwilder/nginx-proxy   "/app/docker-entrypo…"   11 minutes ago      Up 11 minutes       0.0.0.0:80->80/tcp   composejoomla_nginx-proxy_1


And the services are accesibles in the following URLs:
joomla --> http://myjoomla.local/
wordpress --> http://mywordpress.local/
