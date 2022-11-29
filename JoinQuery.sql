select * from addresses
select * from street
select * from cities
select * from countries

--1-müşteri tam adresi
select ad.customer_id Musteri, ad.name Adres, st.name SokakAdi, ci.name ŞehirAdı ,
		co.name ÜlkeAdi from street st 
			inner join cities ci on st.city_id=ci.id
			inner join countries co on ci.country_id=co.id
			inner join addresses ad on ad.street_id=st.id
			
select * from customers
select * from products
select * from orders
select * from order_details

--2-Aynı ürünü sipariş etmiş olan müşterileri
select customers.name, customers.surname, products.name from orders 
					inner join order_details on order_details.order_id=orders.id
					inner join customers on orders.customer_id=customers.id
					inner join products on order_details.product_id=products.id
					
select *from sellers
select * from sellers_order_details

--3-siparişlerdeki satıcılar
select * from sellers
	left join sellers_order_details on sellers.id=sellers_order_details.sellers_id
	
--4-satıcıların ürünleri
select * from sellers
	right join products_sellers on sellers.id=products_sellers.seller_id
					
select * from brands
select * from products_brands
select * from products

--5-ürünlerin markaları
select * from brands
full outer join products_brands on 
			products_brands.brand_id=brands.id
			
--6-ürünlerin fiyatları ve markaları
select products.name,brands.name, products.unit_price from brands
			full outer join products_brands on products_brands.brand_id=brands.id
			inner join products on products_brands.product_id=products.id
			
--7-ürünlerin markaları			
select * from brands
		inner join products_brands on products_brands.brand_id=brands.id
		inner join products on products_brands.product_id=products.id
		
--8-sepete atılan ürünler
select * from shopping_cart
	inner join products on shopping_cart.product_id=products.id
	
--9-siparişlerin ödeme türleri
select payments.type, payments.name, orders.id from payments
	inner join orders on payments.order_id=orders.id
	
--10-indirimden faydalanan müşteriler
select * from discount
	inner join orders on discount.id=orders.discount_id
	inner join customers on orders.customer_id=customers.id
	
--11-indirime giren ürünlerin isimleri
select discount.type indirimOrani,products.name Urun, products.unit_price urunFiyatı from discount
	inner join orders on discount.id=orders.discount_id
	inner join customers on orders.customer_id=customers.id
	inner join order_details on order_details.order_id=orders.id
	inner join products on order_details.product_id=products.id
	
--12-Hangi MÜşteri hangi siparişini hangi kargo firması ile gönderildi?
select order_details.order_id siparişId,products.name UrunAdı, customers.name MusteriAdı,
	customers.surname MusteriSoyadı,orders.order_time SiparişTarihi,shippers.name from shippers
		inner join order_details on shippers.id=order_details.shipper_id
		inner join products on order_details.product_id=products.id
		inner join orders on order_details.order_id=orders.id
		inner join customers on orders.customer_id=customers.id
	
--13-iade edilen ürünler		
select refunds.description iadeNedeni, products.name Ürün from refunds
	inner join order_details on refunds.order_details_id=order_details.id
	inner join products on order_details.product_id=products.id
	
--14-iade edilen ürünler
select refunds.description iadeNedeni, products.name Ürün from refunds
	right join order_details on refunds.order_details_id=order_details.id
	full outer join products on order_details.product_id=products.id
	
--15-iade edilen ürünler
select refunds.description iadeNedeni, products.name Ürün from refunds
	full outer join order_details on refunds.order_details_id=order_details.id
	left join products on order_details.product_id=products.id

	
	



		


					
					
			

			
