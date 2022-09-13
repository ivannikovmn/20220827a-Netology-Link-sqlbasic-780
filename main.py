#https://replit.com/@815374/Python-sql-opdracht#main.py - выбор предлагает куда заходить
#https://replit.com/@Mist0098/SQL-and-Python#main.py код работает
# добавить help

import sqlite3
conn = sqlite3.connect('test.db')
print("""База успешно создана
...""") 

enterwoord = input("""Примеры команд, которые могут выполняться:
1view ... 25view - действия и что в rows
* columns - создать таблицы с атрибутами/столбцами
* rows  - вставить в таблицах строки/кортежи 
** 1update ... 2update - обновление в таблице rows
** 1delete ... 2delete - удаление в таблице rows
** stop - остановить программу
...
* - команды первой очереди
** - команды второй очереди
...
Введите команду: """)

while not enterwoord == 'stop':  
  if enterwoord == 'columns':
    #columns COMPANY
    conn.execute('''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY NOT NULL,
      Name TEXT NOT NULL,
      Age INT NOT NULL,
      Address CHAR(50),
      Salary REAL);   
      ''')    
    #ddl - create , after , drop
    #create - используется для создания объектов базы данных
    #<sqlbasic>
    #columns address 
    conn.execute('''CREATE TABLE address 
      (address_id INT PRIMARY KEY NOT NULL);   
      ''')      
    #columns category
    #--пусто 
    #columns city
    #--пусто 
    #columns customer
    conn.execute('''CREATE TABLE customer
      (customer_id INT PRIMARY KEY NOT NULL,
      last_name TEXT NOT NULL,
      first_name TEXT NOT NULL,
      email INT NOT NULL,
      password INT NOT NULL,
      address_id INT NOT NULL,
      born_date TIMESTAMP,
      create_date TIMESTAMP,
      deleted BOOLEAN NOT NULL DEFAULT FALSE); 
      ''')   
    #columns delivery 
    #должен быть создан тип данных на уровне доментов del_status
    conn.execute('''CREATE TABLE delivery 
      (delivery_id INT PRIMARY KEY NOT NULL,
      address_id INT REFERENCES address(address_id) NOT NULL,
      delivery_date DATE NOT NULL,
      time_range TEXT[] NOT NULL,
      staff_id INT REFERENCES staff(staff_id) NOT NULL,
      status del_status NOT NULL DEFAULT 'в обработке',
      last_update TIMESTAMP,
      create_date TIMESTAMP,
      deleted BOOLEAN NOT NULL DEFAULT FALSE);   
      ''')       
    #columns order_product_list
    conn.execute('''CREATE TABLE order_product_list
      (order_id INT NOT NULL,
      product_id INT NOT NULL,
      amount REAL);  
      ''')  
    #columns orders
    conn.execute('''CREATE TABLE orders 
      (order_id INT PRIMARY KEY NOT NULL,
      amount REAL,
      discount INT NOT NULL,
      customer_id INT NOT NULL,
      delivery_id INT NOT NULL,
      last_update TIMESTAMP,
      created_date TIMESTAMP,
      deleted BOOLEAN NOT NULL DEFAULT FALSE);   
      ''')     
    #columns product
    #--пусто     
    #columns staff
    conn.execute('''CREATE TABLE staff 
      (staff_id INT PRIMARY KEY NOT NULL,
      last_name TEXT NOT NULL,
      first_name TEXT NOT NULL,
      inn INT NOT NULL,
      unit_id INT NOT NULL,
      salary REAL,
      address_id INT NOT NULL,
      created_date TEXT NOT NULL);   
      ''')  
    #columns structure
    #--пусто        
    #</sqlbasic>
    #columns table_one и table_two 
    conn.execute('''CREATE TABLE table_one 
      (name_one varchar(25) not null);          
      ''')      
    conn.execute('''CREATE TABLE table_two 
      (name_two varchar(25) not null);          
      ''')     
    #after - используется для изменения объектов базы данных
    '''
    # Работает около DBeaver-PostgreSQL:
    alter table add constraint orders_delivery_fkey foreign key (delivery_id)
    	reference delivery(delivery_id)   
     ''' 
    conn = sqlite3.connect('test.db')  
    print ('таблицы с атрибутами успешно созданы')
    enterwoord = input("Введите ещё команду: ")
    #drop - используется для удаления объектов базы данных
    '''
    # Работает около DBeaver-PostgreSQL:
    # -- удалить базу данных:
    drop database postgres;
    # -- удалить таблицу:
    drop table product;
    # -- удалить индекс:
    drop index dob_idx on product;
    # -- удалить представление:
    drop view some_view;
    ''' 
  elif enterwoord == 'rows':  
    #rows COMPANY
    conn.execute("INSERT INTO COMPANY(ID,Name,Age,Address,Salary)\
      VALUES (1, 'Миша', 37, 'Алматы', 35.00)");
    conn.execute("INSERT INTO COMPANY(ID,Name,Age,Address,Salary) \
      VALUES (2, 'Даша', 35, 'Сан Хосе', 0.4)");
    conn.execute("INSERT INTO COMPANY(ID,Name,Age,Address,Salary) \
      VALUES (3, 'Оля', 30, 'Алматы', 35.00 )");
    #rows staff
    #dml - select , insert , update , delete,
    #insert - добавляет новые данные
    conn.execute("INSERT INTO staff(staff_id,last_name,first_name,inn,unit_id,salary,address_id,created_date)\
      VALUES (1, 'Hillyer', 'Mike', 775313475294, 1, 200000.00, 3,'2021-10-14 18:33:58.781')");
    conn.execute("INSERT INTO staff(staff_id,last_name,first_name,inn,unit_id,salary,address_id,created_date)\
      VALUES (2, 'Miller', 'Sandra', 775313475294, 3, 150000.00, 4,'2021-10-14 18:33:58.781')"); 
    #<sqlbasic>
    #rows address 
    conn.execute("INSERT INTO address(address_id)\
      VALUES (1)"); 
    #rows category
    #--пусто 
    #rows city
    #--пусто     
    #rows customer
    conn.execute("INSERT INTO customer(customer_id,last_name,first_name,email,password,address_id,born_date,create_date,deleted)\
      VALUES (1, 'Williams', 'Linda', 'linda.williams@sakilacustomer.org', 321152459, 7, '1954-10-12','2021-10-14 18:23:09.828',''), (2, 'Davis', 'Jennifer', 'jennifer.davis@sakilacustomer.org', 523065559, 10, '1976-01-07','2021-10-14 18:23:09.828',''), (210, 'Weiner', 'Ronald', 'ronald.weiner@sakilacustomer.org', 921172029, 324, '1956-06-05','2021-10-14 18:23:09.828','')"); 
    #rows delivery  
    #создадим таблицу по доставке товара
    conn.execute("INSERT INTO delivery(delivery_id,address_id,delivery_date,time_range,staff_id,status,last_update,create_date,deleted)\
      VALUES (0, '102', '2022.02.25', '10:00:00', 2, 150, 0,'',''), (1, '34', '2022.02.25', '10:00:00', 2, 0, 0,'',''), (2, '12', '2022.02.25', '10:00:00', 2, 200, 0,'',''), (3, '78', '2022.02.25', '10:00:00', 2, 0, 0,'',''), (4, '55', '2022.02.25', '10:00:00', 2, 300, 0,'','')");       
    #rows order_product_list
    conn.execute("INSERT INTO order_product_list(order_id,product_id,amount)\
      VALUES (81, 406,  2.00), (6102, 405,  1.00), (6102, 290,  2.00), (6102, 261,  4.00), (384, 329,  2.00), (384, 357,  4.00)");    
    #rows orders  
    conn.execute("INSERT INTO orders(order_id,amount,discount,customer_id,delivery_id,last_update,created_date,deleted)\
      VALUES (81, 484.03, 3, 361, 0, '2021-10-14 23:42:04.742', '2021-10-14 23:42:04.742',''), (6102, 872.03, 3, 367, 0, '2021-10-14 23:42:04.742', '2021-10-14 23:42:04.742',''), (8721, 484.03, 3, 210, 0, '2021-10-14 23:42:04.742', '2021-10-14 23:42:04.742',''), (8723, 96.03, 3, 210, 0, '2021-10-14 23:42:04.742', '2021-10-14 23:42:04.742','')");  
    #rows product
    #--пусто
    #rows staff (+)
    #--пусто 
    #rows structure
    #--пусто     
    #</sqlbasic>
    #rows table_one  и table_two
    conn.execute("INSERT INTO table_one (name_one)\
      values ('one'), ('two'), ('three'), ('four'), ('five')");     
    conn.execute("INSERT INTO table_two (name_two)\
      values ('four'), ('five'), ('six'), ('seven'), ('eight')");        
    #вставить данные в таблицу из другой таблицы около такого вида: INSERT INTO persons (last_name) SELECT last_name FROM customers;
    print('строки успешно добавлены в таблицы')
    conn.commit()
    enterwoord = input("Введите ещё команду: ")
      
  elif enterwoord == '1update':
    #update - изменяет существующие данные
    #company
    #в конкретной строке
    conn.execute("UPDATE COMPANY set Salary=25000.00 where ID = 1")
    #по всему атрибуту
    conn.execute("UPDATE COMPANY set Name='Человек'")
    '''
    # на второе нажатие run выходит через обновление базы выводит изменения
    conn.execute("UPDATE staff set salary=25000.12 where staff_id = 1")   
    conn.commit() 
    print('.salary:', row[5])
    '''  
  elif enterwoord == '2update':
    #orders
    # выходит test(1).db-journal, видимо работает с ошибками скрипт ниже
    conn.execute("update orders set delivery_id = 1 where order_id = 1")     
    print('обновление строк успешно завершено')   
    enterwoord = input("Введите ещё команду: ")
    
  elif enterwoord == '1delete':
    #delete - удаляет данные, желательно не исользовать, лучше с целью последующей аналитики помечать в соответствующем столбце что строка удалена
    #из конкретной строки
    conn.execute("DELETE from COMPANY where ID =2;")
    conn.commit()
    print('строка успешно удалена')
    enterwoord = input("Введите ещё команду: ")   
  elif enterwoord == '2delete':
    #все данные из таблицы
    conn.execute("DELETE from COMPANY;")
    conn.commit()
    print('все строки успешно удалены')
    enterwoord = input("Введите ещё команду: ")  

  elif enterwoord == '1view':  
    #print('Общее количество удаленных ячеек:', conn.total_changes)  
    #COMPANY
    cursor=conn.execute("SELECT Id, Name, Address, Salary from COMPANY")
    for row in cursor:
      print('ID:', row[0])
      print('Name:', row[1])
      print('Address:', row[2])
      print('Salary:', row[3])
    #staff
    #select - осуществляет выборку данных
    cursor=conn.execute("SELECT staff_id,last_name,first_name,inn,unit_id,salary,address_id,created_date from staff")
    for row in cursor:
      print('staff_id:', row[0])
      print('last_name:', row[1])
      print('first_name:', row[2])
      print('inn:', row[3])   
      print('unit_id:', row[4])    
      print('salary:', row[5])  
      print('address_id:', row[6])  
      print('created_date:', row[7])  
    #address 
    cursor=conn.execute("SELECT address_id from address")
    for row in cursor: 
      print('address_id:', row[0])    
    #delivery 
    cursor=conn.execute("SELECT delivery_id,address_id,delivery_date,time_range,staff_id,status,last_update,create_date,deleted from delivery")
    for row in cursor:
      print('delivery_id:', row[0])
      print('address_id:', row[1])   
      print('delivery_date:', row[2])    
      print('time_range:', row[3])   
      print('staff_id:', row[4])       
      print('status:', row[5])  
      print('last_update:', row[6])   
      print('create_date:', row[7])  
      print('deleted:', row[8])       
    print('операции выполнены успешно')
    conn.close()
    enterwoord = input("Введите ещё команду: ")
    
    
  elif enterwoord == '2view': 
    # -- вычтем налоги из зп сотрудника
    cursor=conn.execute('''
    SELECT staff_id , salary - (salary * 0.2) - (salary*0.13) - (salary * 0.08) 
    from staff
    ''')
    for row in cursor:
      print('staff_id:', row[0])
      print('last_name:', row[1])
    print('операции выполнены успешно')
    enterwoord = input("Введите ещё команду: ")
  elif enterwoord == '3view': 
    # -- получим пользователей, имена которых начинаются на M
    cursor=conn.execute('''
    select last_name , first_name 
    from staff 
    where first_name like 'M%'
    ''')
    for row in cursor:
      print('last_name:', row[0])
      print('first_name:', row[1])
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ")
  elif enterwoord == '4view': 
    # -- пполучим фамилии, который начинается на S и заканчиватеся на a
    cursor=conn.execute('''
    select first_name 
    from staff 
    where first_name like 'S%a'
    ''')
    for row in cursor:
      print('last_name:', row[0])
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ")  
  elif enterwoord == '5view': 
    # -- вывести текущую дату и время
    cursor=conn.execute('''
    SELECT datetime('now');
    ''')
    for row in cursor:
      print('Текущая дата и время', row[0])
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ")   
  elif enterwoord == '6view': 
    # -- преобразование числа в текст
    cursor=conn.execute('''
   select cast (100 as text);
    ''')
    for row in cursor:
      print('Текущая дата и время', row[0])
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ") 
    '''
    # Работает через DBeaver-PostgreSQL:
    # -- преобразование числа в текст
    select '01/01/2021'::date 
    # посмотреть тип данных у зн-ия 100(unteger)
    select pg_typeof(100);
    # посмотреть тип данных у зн-ия '100'(unknown)
    select pg_typeof('100');    
    # заменим первую букву имени на Х у пользователей с именами на M 
    select last_name , first_name, overlay (first_name placing 'X' from 1 for 1)
    from staff 
    where first_name like 'M%'
    # получить год из 15.02.2021
    select date_part('year','2021.02.15'::date) 
    # получить число из 15.02.2021		
    select date_part('day','2021.02.15'::date)  
    # получить месяц с учетом года из 15.02.2021
    select date_trunc('month','2021.02.15'::date) 
    # получить число с учетом года из 15.02.2021
    select date_trunc('day','2021.02.15'::date)     
    '''
  elif enterwoord == '7view': 
    # -- текущая дата и время
    cursor=conn.execute('''
   SELECT datetime('now');
    ''')
    for row in cursor:
      print('Текущая дата и время', row[0])
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ")  
  elif enterwoord == '8view': 
    # -- получим пользователей, имена которых не начинаются на M
    cursor=conn.execute('''
    select last_name , first_name 
    from staff 
    where first_name not like 'M%'
    ''')
    for row in cursor:
      print('last_name:', row[0])
      print('first_name:', row[1])
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ") 
    '''
    # Работает через DBeaver-PostgreSQL:
    # -- преобразование cтроку к дате
    select '01/01/2021'::date 
    # -- получим пользователей, имена которых начинаются на M или m
    select last_name , first_name 
    from staff 
    where first_name ilike 'm%'   
    #-- возращает положение указанной подстроки
    select strpos('Hello world', 'world')
    #-- возращает длину строки
    select character_length ('Hello world') 
    #-- заменяет подстроку, итог - Helmaxld
    select overlay('Hello world' placing 'max' from 5 for 5)
    -- извлекает подстроку, итог - world:
    select substring('Hello world!'from 7 for 5) 
    '''    
  elif enterwoord == '9view': 
    # -- вывести все записи таблицы
    cursor=conn.execute('''
    select * from staff;
    ''')
    for row in cursor:
      print('staff_id:', row[0])
      print('last_name:', row[1])
      print('first_name:', row[2])
      print('inn:', row[3])   
      print('unit_id:', row[4])    
      print('salary:', row[5])  
      print('address_id:', row[6])  
      print('created_date:', row[7]) 
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ")     
  elif enterwoord == '10view': 
    # -- вывести количество записей в таблице. Можно например так получить ответ сколько было платжей, если скажем место staff использовать orders o
    cursor=conn.execute('''
    select count (*) from staff;
    ''')
    for row in cursor:
      print('Кол-во записей в таблице:', row[0]) 
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ")      
  elif enterwoord == '11view': 
    # -- получить данные по таблице delivery
    cursor=conn.execute('''
    select * from delivery;
    ''')
    for row in cursor:
      print('delivery_id:', row[0])
      print('address_id:', row[1])   
      print('delivery_date:', row[2])    
      print('time_range:', row[3])   
      print('staff_id:', row[4])       
      print('status:', row[5])  
      print('last_update:', row[6])   
      print('create_date:', row[7])  
      print('deleted:', row[8])    
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ")      
  elif enterwoord == '12view': 
    # -- получить данные по таблице orders
    cursor=conn.execute('''
    select * from orders;
    ''')
    for row in cursor:
      print('delivery_id:', row[0])
      print('order_id:', row[1])   
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ") 
  elif enterwoord == '13view': 
    # -- получить данные по таблице table_one  и table_two
    cursor=conn.execute('''
    select * from table_one;
    ''')
    for row in cursor:
      print('table_one:', row[0])
    cursor=conn.execute('''
    select * from table_two;
    ''')
    for row in cursor:
      print('table_two:', row[0])        
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ") 
    enterwoord = input("Введите ещё команду: ") 
  elif enterwoord == '14view': 
    # -- получить данные по таблице table_one  и table_two
    # inner join - выводит одинаковые данные для table_one  и table_two
    cursor=conn.execute('''
    select t1.name_one, t2.name_two
    from table_one t1
    inner join table_two t2 on t1.name_one = t2.name_two
    ''')
    for row in cursor:
      print('inner join:', row[0])     
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ") 
  elif enterwoord == '15view': 
    # -- получить данные по таблице table_one  и table_two
    # left join - выводит table_one  c обогащением от table_two
    cursor=conn.execute('''
    select t1.name_one, t2.name_two
    from table_one t1
    left join table_two t2 on t1.name_one = t2.name_two
    ''')
    for row in cursor:
      print('left join:', row[0])     
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ") 
    '''
    # Работает через DBeaver-PostgreSQL:    
    # -- получить данные по таблице table_one  и table_two
    # right join - выводит table_two c обогащением от table_one
    select t1.name_one, t2.name_two
    from table_one t1
    right join table_two t2 on t1.name_one = t2.name_two
    # -- full join - выводит все данные table_two и table_one
    select t1.name_one, t2.name_two
    from table_one t1
    full join table_two t2 on t1.name_one = t2.name_two    
    # -- full join - выводит уникальные данные table_two и table_one
    select t1.name_one, t2.name_two
    from table_one t1
    full join table_two t2 on t1.name_one = t2.name_two  
    where t1.name_one is null or t2.name_two is null
    '''    
  elif enterwoord == '16view': 
    # -- получить данные по таблице table_one  и table_two
    # cross join - выводяться через перемножение комбинации зн-ий  table_one и table_two
    cursor=conn.execute('''
    select t1.name_one, t2.name_two
    from table_one t1
    cross join table_two t2 
    ''')
    for row in cursor:
      print('cross join:', row[0])    
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ")   
  elif enterwoord == '17view': 
    # --соединение данных в таблице orders с таблицей delivery по delivery_id b вывод order_id 
    # o - Это алиас(краткое название таблицы orders)
    cursor=conn.execute('''
    select o.order_id
    from orders o
    join delivery d on o.delivery_id = d.delivery_id
    ''')
    for row in cursor:
      print('o.order_id:', row[0])          
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ")   
  elif enterwoord == '18view': 
    # -- получим все возможные комбинации имен пользователей, так, что бы имя А не было равно имени А
    cursor=conn.execute('''
    select s.first_name , s2.first_name 
    from staff s 
    cross join staff s2 
    where s.first_name != s2.first_name 
    ''')
    for row in cursor:
      print('s.first_name:', row[0])    
      print('s2.first_name :', row[1])     
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ")   
  elif enterwoord == '19view': 
    # -- получим список заказов по которым присуствует доставка
    cursor=conn.execute('''
    select o.order_id , d.delivery_id 
    from orders o
    left join delivery d on d.delivery_id = o.delivery_id 
    where d.delivery_id is not null 
    ''')
    for row in cursor:
      print('o.order_id:', row[0])       
      print('d.delivery_id:', row[1])      
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ")
  elif enterwoord == '20view': 
    #агрегатные ф-ции
    #sum - возвращает общую сумму числового столбца
    #count - возвращает кол-во строк, соответствующих задаанному критерию
    #avg - возращает среднее зн-ие числового столбца
    #min - возращает наименьшее зн-ие выбранного столбца
    #max - возвращает наибольшее зн-ие выбранного столбца
    #group by - данные по группам
    # в даннном примере выводятся но не видно явно как посчитал sum, avg, max
    cursor=conn.execute('''
    select delivery_id, count(staff_id), sum(status), avg(status), max(status)
    from delivery
    group by delivery_id;
    ''')
    for row in cursor:
      print('delivery_i:', row[0])       
      print('count(staff_id):', row[1])  
      print('sum(status):', row[2])     
      print('avg(status):', row[3])    
      print('max(status):', row[4])
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ")    
  elif enterwoord == '21view': 
    #-- проверка выводяться ли данные, которые были добавлены в таблицу-строки для "22view"
    cursor=conn.execute("SELECT order_id,amount,discount,customer_id,delivery_id,last_update,created_date,deleted from orders")
    for row in cursor:
      print('order_id:', row[0])
      print('amount:', row[1])   
      print('discount:', row[2])    
      print('customer_id:', row[3])   
      print('delivery_id:', row[4])       
      print('last_update:', row[5])  
      print('created_date:', row[6])   
      print('deleted:', row[7])       
    print('операции выполнены успешно')  
    cursor=conn.execute("SELECT customer_id,last_name,first_name,email,password,address_id,born_date,create_date,deleted from customer")
    for row in cursor:
      print('customer_id:', row[0])
      print('last_name:', row[1])   
      print('first_name:', row[2])    
      print('email:', row[3])   
      print('password:', row[4])       
      print('address_id:', row[5])  
      print('born_date:', row[6])   
      print('create_date:', row[7])  
      print('deleted:', row[8])       
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ")       
  elif enterwoord == '22view': 
    #-- получим данные по сумме платежей, min, max платежу и кол-ву платежей по каждому пользователю
    cursor=conn.execute('''
    select c.last_name , c.first_name , sum(amount), min(amount), max(amount), avg(amount)
    from customer c
    join orders o on o.customer_id = c.customer_id
    group by c.customer_id 
    ''')
    for row in cursor:
      print('last_name:', row[0])       
      print('first_name:', row[1])  
      print('sum:', row[2])  
      print('min:', row[3]) 
      print('max:', row[4]) 
      print('avg:', row[5]) 
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ")
  elif enterwoord == '23view': 
    #-- получим данные по сумме платежей, min, max платежу и кол-ву платежей по каждому пользователю
    #-- по каждому пользователю, при этом размер платежа должен быть более 100 и сумма платежа 
    #-- должна быть быть более 20000
    cursor=conn.execute('''
    select c.last_name , c.first_name , sum(amount), min(amount), max(amount), avg(amount)
    from customer c
    join orders o on o.customer_id = c.customer_id
    where amount > 100
    group by c.customer_id 
    having sum(amount) > 20000
    ''')
    for row in cursor:
      print('last_name:', row[0])       
      print('first_name:', row[1])  
      print('sum:', row[2])  
      print('min:', row[3]) 
      print('max:', row[4]) 
      print('avg:', row[5]) 
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ")
    '''
    # Работает через DBeaver-PostgreSQL и скорей всего через sqlite3:
    # order by 2 desc - сортируем от большего к меньшего в категории
    # 
    -- написать запрос и по результату ответить на вопрос: в какой категории находится больше всего товаров?
    # concat - соединение, например как фамилия и имя concat(c.last_name, ' ', c.first_name) чтобы сравнить с 'Williams Linda'
    select c.category, count(*)
    from product p
    join category c on c.category_id = p.category_id 
    group by  c.category_id 
    order by 2 desc   
    -- cколько черепах купила Williams Linda
    select sum(opl.amount)
    from customer c 
    join orders o on o.customer_id  = c.customer_id
    join order_product_list opl on opl.order_id = o.order_id 
    join product p on opl.product_id = p.product_id
    where concat(c.last_name, ' ', c.first_name) = 'Williams Linda' and p.product = 'Черепаха'    
    '''
  elif enterwoord == '24view': 
    #-- найдём процентное отношение суммы платежей каждого пользователя к общей сумме платежей всех пользователей
    cursor=conn.execute('''
    select customer_id, sum(amount)/
    (select sum(amount) from orders)
    from orders 
    group by customer_id 
    ''')
    for row in cursor:
      print('customer_id:', row[0])       
      print('?column?:', row[1])  
    print('операции выполнены успешно')    
    enterwoord = input("Введите ещё команду: ")    
    '''
    # Работает через DBeaver-PostgreSQL:
    #-- найдём сумму платежей пользоватлей, чья фамилия начинается на букву "A"
    select o.customer_id, concat, sum(amount)
    from orders o
    join (select customer_id, concat(last_name,'',first_name)
    	from customer
    	where left(last_name,1)='A') t 
    on t.customer_id=o.customer_id 
    group by o.customer_id, concat   
    #-- найдём сумму платежей пользоватлей, чья фамилия начинается на букву "A"
    select customer_id, sum(amount)
    from orders 
    where customer_id in(
    	select customer_id 
    	from customer 
    	where left(last_name,1)='A')
    group by customer_id 
    '''
  elif enterwoord == '25view': 
    #-- проверка выводяться ли данные, которые были добавлены в таблицу-строки order_product_list
    cursor=conn.execute("SELECT order_id,product_id,amount from order_product_list")
    for row in cursor:
      print('order_id:', row[0])
      print('amount:', row[1])   
      print('discount:', row[2])        
    print('операции выполнены успешно') 
    enterwoord = input("Введите ещё команду: ")  
    '''
    # Работает через DBeaver-PostgreSQL и скорей всего через sqlite3:
    # -- Отношение стоимости товара к единице стоимости этих товаров (подзапросы)
    # -- product таблицу создать
    # вариант 1:
    select t.product_id, sum / price
    from (select opl.product_id , sum(o.amount)
    from orders o
    join order_product_list opl on o.order_id = opl.order_id 
    group by opl.product_id) t
    join (select product_id , price  
    from product p) t2 on t2.product_id = t.product_id
     # вариант 2:
    select t.product_id, sum / (select price from product p where p.product_id = t.product_id)
    from (select opl.product_id , sum(o.amount)
    from orders o
    join order_product_list opl on o.order_id = opl.order_id 
    group by opl.product_id) t    
    '''
    '''
    # Работает через DBeaver-PostgreSQL:
    # -- Нумерация строк в рамках окна
    select order_id, customer_id, amount,
    	row_number () over (partition by customer_id order by amount)
    from orders 
    offset 25    
    # -- получим каждый 10 заказ пользователя в порядке идентификаторов заказов:
    select *
    from (
    	select order_id, customer_id, amount,
    		row_number() over(partition by customer_id order by order_id)
    	from orders) t 
    where row_number % 10 =0    
    # -- отношение стоимости товаров к единице стоимости этих товаров
    # -- distinct - убирает дублирующие строки
    select distinct opl.product_id , sum (o.amount) over (partition by p.product_id) / price
    from orders o
    join order_product_list opl on o.order_id=opl.order_id 
    join product p on p.product_id = opl.product_id 
    # -- получим данные о каждом 1000 заказе
    # -- over - открытие оконной ф-ции
    select *
    from (
    select order_id ,customer_id ,amount ,
    	row_number () over (order by order_id)
    from orders) t
    where t.row_number % 1000 = 0
    # -- получим накопительную сумму платежей по каждому пользователю
    select order_id , customer_id , amount ,
    	sum(amount) over (partition by customer_id order by order_id)
    from orders 
    # -- получим накопительный avg платежей по каждому пользователю
    select order_id , customer_id , amount ,
    	avg(amount) over (partition by customer_id order by order_id)
    from orders    
    '''
    '''
    # Скорей всего работает через DBeaver-PostgreSQL похоже при открытом доступе записей в схемы:
    #-- при тесте от 24view с добавлением вначале create view customers_sum_avg as второй раз не запускается, в первый данные не отображатся 
    #-- получим информацию по ФИО клиента, сумму платежей и кол-во товаров по каждой категории и разместим запрос в представлении:
    create view customers_sum_avg as
      select c.last_name, c.first_name, c2.category, sum(o.amount), count(o.order_id)
      from orders o
      join order_product_list opl on opl.order_id=o.order_id 
      join product p on p.product_id = opl.product_id 
      join category c2 on c2.category_id = p.category_id 
      join customer c on c.customer_id = o.customer_id 
      group by c.last_name, c.first_name, o.customer_id, p.category_id, c2.category 
      order by o.customer_id 
     #-- получим информацию по ФИО клиента, сумму платежей и кол-во товаров по каждой категории и разместим запрос в материализованном представлении:
    create materialized view customers_sum_avg as
    	select c.last_name, c.first_name, c2.category, sum(o.amount), count(o.order_id)
    	from orders o
    	join order_product_list opl on opl.order_id=o.order_id 
    	join product p on p.product_id = opl.product_id 
    	join category c2 on c2.category_id = p.category_id 
    	join customer c on c.customer_id = o.customer_id 
    	group by c.last_name, c.first_name, o.customer_id, p.category_id, c2.category 
    	order by o.customer_id    
    #-- Нужно постоянно получать данные по последнему заказу пользователя
    create view task_1 as
    select *
    from (
    select order_id , customer_id , amount , 
    	row_number () over (partition by customer_id order by order_id desc)
    from orders) t 
    where row_number = 1
    select * from task_1
    #--то же с материализованным представлением (Будет работать, если обновлены данные  материализованном представлением)
    create materialized view task_2 as
    select *
    from (
    select order_id , customer_id , amount , 
    	row_number () over (partition by customer_id order by order_id desc)
    from orders) t 
    where row_number = 1
    with no data
    select * from task_2
    #--обновим данные в материализованном представлением
    refresh materialized view task_2
    #--удалим материализованное представление
    drop materialized view task_2     
    #
    select round(count(*)::numeric/sum(count(*)) over () * 100,3)
    from product p group by category_id 
    order by 1 desc
    '''
  
antwoord = input("""...
Спасибо за использование программы, всего доброго!""")