### 1. Basic Selection.  
To start off, fetching all records from a table is straightforward:  
``items = session.exec(select(Item)).all()``

### 2. Filtering Records.  
Filter results using the ``.filter()`` method:  
``filtered_items = session.exec(select(Item).filter(Item.name == "widget")).all()``


