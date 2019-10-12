#!/usr/bin/expect -f
set port 3306
set user james
set host 192.168.0.1
set password 123
set timeout -1

spawn mysql -h$host -u$user -p
expect "*assword:*"
send "$password\r"
interact
expect eof
