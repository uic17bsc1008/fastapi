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
