# Modern and Editable Tables Using Grid.js

This is an update to an earlier post on [interactive tables using DataTables.js](https://github.com/GitauHarrison/beautiful-flask-tables). In this update, you will see how to use the more modern [Grid.js](https://gridjs.io/) library to create more good-looking and very interactive tables. Additionaly, you will get to see how you can make a data column editable and the changes made saved to the database instantly.

![Gridjs table](/app/static/images/gridjs_tables.gif)

## Overview

Datatable.js relies heavily on JQuery. Most front-end frameworks currently are able to bypass the use of JQuery, making it obsolete, though it still has its use cases. With that said, there is a need to update the original project which relied on JQuery to create tables.

## Tools Used
- Flask microframework
- Python for programming
- Grid.js for interactive tables
- SQLite for database

## Implementation

Add both the CSS and JS files to your template:

```html
<link href="https://unpkg.com/gridjs/dist/theme/mermaid.min.css" rel="stylesheet" />
<script src="https://unpkg.com/gridjs/dist/gridjs.umd.js"></script>
```

Add Grid.js to your specific table:

```html
<div id="table"></div>

<script>
  new gridjs.Grid({
    data: [
      { name: 'John', age: '25', city: 'New York' },
      { name: 'Jane', age: '24', city: 'London' },
      { name: 'Joe', age: '23', city: 'Paris' },
    ],
    columns: [
      { name: 'name', label: 'Name' },
      { name: 'age', label: 'Age' },
      { name: 'city', label: 'City' },
    ],
  }).render(document.getElementById('table'));
</script>
```

That's it! You do not need to define a `table` element.

## Bootstrap Table

This is your normal table, styled to the taste of bootstrap. You will notice that when you load the bootstrap table, the page will momentarily remain blank. This is because **all the data** from the database, which could be in tens or hundreds of thousands, have to be loaded. Thereafter, the table with its content will be displayed. 

Ideally, this table is suitable for only small amounts of data. The user experience working with large amounts of data is not good at all.

## Basic Table

This table improves the bootstrap table by adding a bit of iteractivity. For example, you will notice that the table data is paginated, and there is a search bar with excellent search functionality. However, just like the bootstrap table, all data need to be loaded before the table is displayed.

## Ajax Table

This table is a slight improvement to the basic table. The table schema is displayed first before the data. Once all the data has been loaded, then you will see the needed data.

## Server-side Table

To solve the slight lag issue experienced in all the previous three tables, the server-side example shifts the loading of data to the server's side. Data will be displayed based on request. For example, if data on page 5 is needed, only page 5 data will be loaded and susbsequently displayed. The loading of data is dependant on the request.

## Editable Table

Depending on the use case, there are times when you would like to edit data directly from the table. In this table example, you will notice that two columns (Name and Address) have fields whose data can be altered. Pressing "Enter" will automatically save the changes to the database.

Now, this feature is not a Grid.js feature. It is implemented using the  [contentEditable](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/contenteditable) attribute that all modern browsers support.


## Testing the Application Locally

If you are interested in testing the application, you can use the following commands to run the application:

1. Clone this repository:

    `$ git clone https://github.com/GitauHarrison/interactive-tables-with-gridjs.git`
    <br>

2. Change directory to access the application:

    `$ cd interactive-tables-with-gridjs`
    <br>

3. Create and activate the virtual environment:

    `$ mkvirtualenv gridjs`
    <br>

4. Install dependencies:

    `(gridjs) $ pip3 install -r requirements.txt`
    <br>
5. Run the application:

    `(gridjs) $ flask run`
    <br>
6. Open the application in your browser running on local port 5000:

    - [x] [Chrome](http://127.0.0.1:5000/)
    - [x] [Firefox](http://127.0.0.1:5000/)
    - [x] [Safari](http://127.0.0.1:5000/)


## Reference

If you would like to understand how to use Grid.js, you can read the [interactive tables with Grid.js](https://github.com/GitauHarrison/notes/blob/master/flask_tables/gridjs.md) article.