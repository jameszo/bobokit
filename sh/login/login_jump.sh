#!/usr/bin/expect -f
set port 22
set user 
set host 
set passphrase 
set password
set timeout -1

spawn ssh -i /Users/James/.ssh/rsa.txt $user@$host
expect "*passphrase*"
send "$passphrase\r"
expect "*password*"
send "$password\r"
interact
expect eof
