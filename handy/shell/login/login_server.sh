#!/usr/bin/expect -f
set port 22
set user james
set host 192.168.0.1
set password 123
set timeout -1

spawn ssh -p$port $user@$host
expect "*assword:*"
send "$password\r"
interact
expect eof
