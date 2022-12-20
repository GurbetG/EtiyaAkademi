select * from categories
insert into categories (name,type)
			values('tablet','teknoloji')
			
select * from customers
insert into customers(name,surname,email)
			values('Gurbet','Guclu','gurbet@gmail.com')
	
update customers 
	set surname='Guclu' where id=4
	
update customers 
	set name='Atilla' where id=5
	
delete from customers where id=6

select * from cities
select name as Şehir from cities

select * from order_details
select * from products
select * from categories

select categories.id as "Kategori_id", categories.name as "Kategori Adı",products.name as "Urun Adı", 
	products.stock as "Urun Adedi" from categories 
	inner join products on products.category_id=categories.id
	
	
