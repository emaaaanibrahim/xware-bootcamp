# Day 5
# Install Postgresql
>>> sudo apt update
>>>sudo apt update
>>>sudo apt install postgresql postgresql-contrib
>>>sudo systemctl start postgresql.service
>>>service postgresql  status
>>>sudo -u postgres psql
>>>\password
>>>sudo systemctl restart postgresql
# Install pgAdmin
>>> sudo apt update
>>> sudo curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add
>>> sudo curl sudo sh -c 'echo deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/focal pgadmin4 main > /etc/apt/sources.list.d/pgadmin4.list && apt update'
