#!/usr/bin/expect

# Note: Before running this script, install 'expect': sudo apt install expect

#variables
set password "123456"
set database "agora_db"
set username "agora_admin"

#checks the number of connections to the database
#spawn psql -U postgres -W -c "SELECT * FROM pg_stat_activity WHERE datname = \'${database}\';" 
spawn psql -U postgres
expect "Password for user postgres: "
send -- "$password\r"

#remove all the connections to the database
expect "postgres=# "
send "SELECT pg_terminate_backend (pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = \'${database}\';\r"

#drop the database
expect "postgres=# "
send "drop database ${database};\r"

#create new database
expect "postgres=# "
send "create database ${database};\r"

#create new user
expect "postgres=# "
send "create user ${username} with password '123456';\r"

#grant USAGE permission to user
expect "postgres=# "
send "GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO ${username};\r"

#grant EXECUTE permission to user
expect "postgres=# "
send "GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO ${username};\r"

#grand SELECT, INSERT, UPDATE, and DELETE permissions to user
expect "postgres=# "
send "GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO ${username};\r"

#grant permission to create TEMP to user
expect "postgres=# "
send "GRANT TEMP ON DATABASE ${database} TO ${username};\r"

expect "postgres=# "
send "\\q\r"

expect eof