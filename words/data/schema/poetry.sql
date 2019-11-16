drop database if exists poetry_db;
create database if not exists poetry_db default character set utf8 collate utf8_general_ci;
use poetry_db;

drop table if exists t_article;
create table if not exists t_article (
    id bigint auto_increment, 
    title varchar(100) not null default '',
    author varchar(100) not null default '',
    time varchar(100) not null default '',
    content text not null,
    created datetime not null default '9999-12-31 23:59:59',
    updated datetime not null default '9999-12-31 23:59:59',
    unique index idx_id(id asc),
    primary key (id),
    unique key uqk1 (title, author, time)
)engine=InnoDB auto_increment=1;

drop table if exists t_article_words;
create table if not exists t_article_words (
    article_id bigint not null,
    words text not null,
    created datetime not null default '9999-12-31 23:59:59',
    updated datetime not null default '9999-12-31 23:59:59',
    primary key (article_id)
)engine=InnoDB;

drop table if exists t_word;
create table if not exists t_word(
    id bigint auto_increment,
    word varchar(50) not null,
    article_ids text not null,
    created datetime not null default '9999-12-31 23:59:59',
    updated datetime not null default '9999-12-31 23:59:59',
    unique index idx_word(word),
    primary key(id)
)engine=InnoDB auto_increment=1;

drop table if exists t_word_cloud;
create table if not exists t_word_cloud(
    id bigint auto_increment,
    word_id bigint not null,
    cloud_img blob not null,
    article_ids text not null,
    created datetime not null default '9999-12-31 23:59:59',
    updated datetime not null default '9999-12-31 23:59:59',
    index idx_id(word_id),
    primary key(id)
)engine=InnoDB auto_increment=1;
