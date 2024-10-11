# Query related to SQLModel  

### 1. Basic Selection.  
To start off, fetching all records from a table is straightforward:  
``items = session.exec(select(Item)).all()``

### 2. Filtering Records.  
Filter results using the ``.filter()`` method:  
``filtered_items = session.exec(select(Item).filter(Item.name == "widget")).all()``

### 3. Sorting Results.  
Sort the output with the ``.order_by()`` method:  
``sorted_items = session.exec(select(Item).order_by(Item.name)).all()``

### 4. Limiting and Offsetting.  
For pagination or limiting ``.limit() and .offset()`` method:  
``paginated_items = session.exec(select(Item).limit(5).offset(10)).all()``

### 5. Counting Records.  
Calculate the number of records that fit certain criteria:  
``count = session.exec(select(Item).filter(Item.name == "widget")).count()``

### 6. Using Joins.  
Fetch related data from multiple tables:  
``from sqlmodel import join``  
``items_with_details = session.exec(select(Item, Detail).join(Detail)).all()``  

### 7. Aggregations.  
Utilize functions like ``SUM()``, ``AVG()``, etc.:  
``from sqlmodel.functions import avg``  

``average_price = session.exec(select(avg(Item.price))).first()``  

### 8. Using OR Conditions  
Query using multiple conditions:  
``from sqlalchemy import or_``  

``items = session.exec(select(Item).filter(or_(Item.name == "widget", Item.price < 100))).all()``  

### 9. Update Queries  
Modify records based on certain conditions:  
``session.exec(select(Item).filter(Item.name == "widget")).update({"price": 150})``  
``session.commit()``  

### 10. Deleting Records  
Remove records as per certain criteria:  
``session.exec(select(Item).filter(Item.name == "obsolete-widget")).delete()``  
``session.commit()``  
