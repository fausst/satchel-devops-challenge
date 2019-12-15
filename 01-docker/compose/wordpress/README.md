# Wordpress with MariaDB stack
This compose file have 2 services:
  - db --> mariadb
  - wordpress

The goal of this excercise has been acomplished by:
Persistence: In this case I used db_data for volume persistence in the mariadb database. Any changes do
ne by wordpress will be permanent saved in this volume.
Networking: I have created a isolated newtork for this project called "isolated_nw" and it is shared by
 both db and wordpress services, using the default "brigde"  driver.

The solution has been started and tested with the following URL:
- http://localhost:8000
