# MariaDB backup job
In order to resolve this exercise, i have created another service for the backup to work.
In this service, installed with mariadb:10.2, the backup is launched with mysqldump tool and connecting to the remote database. In addition, a new directory is created to generate the backup.
To copy the backup to my local machine path, i have used a bind mount to a "./backup" directory from the reciently created in the container machine.

Finally, i have launched a "docker-compose up" command and proved the backup is generated correctly in the local path.
