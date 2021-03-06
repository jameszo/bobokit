# Linux Command Memo

## Linux

```
ssh -i xxx_rsa user@host
scp [可选参数] file_source file_target
uptime

printf "%x\n"  3046 
iconv -s -c -f UTF8 -t GBK src.csv > dec.csv

df -h
du -h -d 1 /
jobs -l
fg %<number>
bg %<number>

diff -rq  <path> <path> > difftxt
find . -size +100M
grep 'model name' /proc/cpuinfo | wc -l
grep -ABC
grep -v
awk -F "[分隔符 分隔符]" '{print $1,"=",$2;}' filename
sed -i "" 's/webmobileapi\.bainianaolai\.com/m\.bainianaolai\.com/g' `grep "webmobileapi.bainianaolai.com" -rl .`
gzip -dc myfile.gz | grep abc

curl -d 'jsondata={"uid":"324","valid_flag":1}' "http://api.customer.liangcheng.idc/memberlq/api/customer/updateVipUserStatus.aj" -X POST

firewall-cmd --add-port=20070/tcp --permanent
firewall-cmd --reload
firewall-cmd --zone=public --add-port=80/tcp --permanent
firewall-cmd --query-port=6379/tcp
```

## Git

```
git clone --depth=1 <repository>
git branch <name>
git checkout <name>
git branch -d <name>
git merge <name>
git pull origin master --allow-unrelated-histories
git submodule add <repository>

git fetch --all
git reset --hard origin/master

git remote -v
git remote add upstream git@github.com:xxx/xxx.git

git fetch upstream
git merge upstream/master

```

## SVN

```
svn co <url> <path> --username  --password

svn status
svn diff -r <number>:<number>
svn merge <url>@xxx <url>@xxx <path>
svn merge -r <version>:<version>

svn resolve  --accept <option> <path>
svn resolve –-accept working a.txt
svn resolve --accept=theirs-conflict file.c

svn st | awk '{if($1=="?") {print $2}}' | xargs svn add
```

## Docker

```
docker export <CONTAINER ID> > my_container.tar
cat my_container.tar |docker import - image_name:tag

docker run -v <host dir>:<container dir> -p <container port>:<host port> -it centos:centos6 /bin/bash
docker run --name gdb --security-opt seccomp=unconfined -v /Users/James/code:/data -it centos:centos6 /bin/bash
docker run --privileged -ti --name test  docker.io/centos:7  /usr/sbin/init
docker run --rm -it redis_master:1.0 bash

docker@xhyve:~$ sudo mkdir /sys/fs/cgroup/systemd
docker@xhyve:~$ sudo mount -t cgroup -o none,name=systemd cgroup /sys/fs/cgroup/systemd

docker save -o dockerimg_base_server.tar base_server
docker load -i quay.io-calico-node-1.tar

docker images -f "dangling=true"
docker build -f Redis.Dockerfile -t cluster_redis:1.0 .

docker volume ls -qf dangling=true | xargs docker volume rm

docker-machine scp host1:/tmp/a host2:/tmp/b
docker cp 容器名：要拷贝的文件在容器里面的路径  要拷贝到宿主机的相应路径
```

# Vim

```
:so $MYVIMRC

/<search string>\c

ctrl+v：矩形选择

% 当前完整的文件名
%:h 文件名的头部，即文件目录.例如../path/test.c就会为../path
%:t 文件名的尾部.例如../path/test.c就会为test.c
%:r 无扩展名的文件名.例如../path/test就会成为test
%:e 扩展名

vimdiff:
       ]c    跳到下一个不同处
       [c    跳到上一个不同处
       dp   put
       do   get
       zo   打开折叠(l也可以打开折叠）
       zc   关闭当前折叠
       zm  关闭所有折叠
       zr   打开所有折叠

:%s/\(world\), change \(mind\)/\2, change \1/
:%s/_\([a-z]\)/\U\1/g
let i=997|g/abcdefg/s//\=i/|let i=i-1

:%!xxd
:e ++enc=gbk
```

## Maven

```
mvn package -DskipTests

mvn archetype:generate -DgroupId=<name> -DartifactId=<name> -DinteractiveMode=false

mvn test -Dtest=MyClassTest#*test*

mvn spring-boot:run

mvn dependency:tree

mvn exec:java -Dexec.mainClass="com.vineetmanohar.module.Main"
```

## MySQL

```
create user 'testuser'@'127.0.0.1' identified by '123456';
grant all privileges on db_test.* to 'testuser'@'127.0.0.1';
flush privileges;

source  file.sql

mysqldump -h192.168.32.88 -uliangcheng -p0324LiangCheng2017 -d --all-databases > bainianaolai.sql

show variables like 'character_%';
set @@character_set_connection=utf8;

pager cat > file

sudo /usr/local/mysql/support-files/mysql.server start
```

## Mac

```
sudo spctl --master-disable
```

## Spring

```
spring init -dweb,data-jpa,h2,thymeleaf --build maven demo
```

## Item2

```
输入打头几个字母，然后输入command+; iterm2将自动列出之前输入过的类似命令。

输入command+shift+h，iterm2将自动列出剪切板的历史记录。

```
