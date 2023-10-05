Description:

    A delivery restaurant chain has many locations where they prepare 
    orders for customers. Each customer wants to receive a receipt with 
    their order that contains detailed information about the order. 
    The kitchen staff also wants a receipt so they don't forget to put 
    everything they need when preparing and packing the order. 
    Our task is to help them both by writing a service to generate receipts.
    
    The service creates orders in the database for all printers of the outlet 
    specified in the order and sets asynchronous tasks to generate PDFs 
    for these orders. If there are no printers in the outlet, an error is returned. 
    If orders for this branch have already been created, an error 
    is returned (the order number is passed).

Two endpoints:

    post: creation of a new order and asynchronous creation of a pdf file
    
    get: a list of orders that have already been generated for a specific 
    printer is requested, after which a PDF file for each order is downloaded 
    and sent to print (the "status" field in the order is changed)

TECHNOLOGY STACK:

    Django Rest framework
    
    PostgreSQL
    
    Docker
    
    Celery
    
    Redis
    
    Swagger
    
    Converter html to pdf

LAUNCH:

    clone this repo
    
    create a dotenv file using an example from the repository
    
    run command in virtual envoriment "pip install -r requirements.txt"
    
    python manage.py migrate
    
    python manage.py createsuperuser
    
    python manage.py loaddata printer_fixtures.json
    
    docker-compose up
    
    python manage.py runserver & celery -A Main_app worker --loglevel=info
    
    OR:
    
    in two different terminals:
    
    python manage.py runserver
    
    celery -A Main_app worker --loglevel=info
