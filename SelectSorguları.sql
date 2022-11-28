--select
select * from order_details;
select order_id,product_id from order_details;
select * from addresses;
select id, name from addresses ;
select * from shippers;
select telephone, name from shippers;
--orderBy
select * from products order by stock;
select * from products order by stock desc;
select * from customers order by name,surname;

select * from brands;
select * from brands order by name asc;

--where

select * from brands where type='spor';
select * from payments where type='cash';
select * from payments where count >'50000';
select * from discount where type='%20'
select * from discount where value='100';

-- where IN()
select * from sellers where follower_count in(400,500)
select * from sellers where name in('Zara Aş','nike.aş')
select * from sellers where rating in ('7','8.5','9')

--between
select * from sellers where follower_count between 500 and 1000
select * from shopping_cart where quantity >=7 and quantity<=15
select * from shopping_cart where quantity between 5 and 10

--and, or, not
select * from brands where type='spor'and name='adidas';
select * from discount where type='%30' or value='100'
select * from discount where not id>4

--like(%j%)
select * from sellers where name like('%ar%')
select * from sellers where rating like('%8%')
select * from sellers where LOWER(name) like('%za%')
select * from sellers where LOWER(name) like('_a%')








