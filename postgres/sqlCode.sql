
create table categories(
    id serial primary key ,
    category varchar(100) not null
);

create table sub_categories(
    id serial primary key ,
    category_id int not null ,
    sub_category varchar(100) not null ,
    foreign key (category_id) references categories(id)
);

alter table sub_categories add column href varchar(200);
alter table categories add column href varchar(200);

create table products (
    id serial primary key,
    title varchar(100) not null,
    image varchar(100),
    price float not null ,
    descripts text not null ,
    city varchar(50) not null ,
    sub_category_id bigint not null ,
    foreign key (sub_category_id) references  sub_categories(id)
);

-- select * from categories;
-- inner join sub_categories on categories.id = sub_categories.category_id;

-- INSERT INTO products (title, image, price, descripts, city, sub_category_id) VALUES ;

-- select title,price,descripts,image,sub_category from products
-- inner join sub_categories on sub_category_id = sub_categories.id

-- INSERT INTO sub_categories(category_id, sub_category, href) VALUES(%i,%s,%s);




