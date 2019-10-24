- Para crear requirements.txt:
	* pipreqs "C:\Users\Daniel Smith\Desktop\Learn\Make Money with ML - Siraj Raval\Week 5\Single\Coffee-Rust-Detection\app"
	* pip install -r requirements.txt
- Correr Flask:
	* set FLASK_APP=app.py
	* flask run

- Stripe:
	* set STRIPE_PUBLISHABLE_KEY=pk_test_YyqRFSGJHGZhLeyKIIrqXQBd005AXscUC6
	* set STRIPE_SECRET_KEY=sk_test_6JolluUm8aEb5Axu1twu37Aa00KQmuZu4G

- Upload to Heroku
	* heroku login
	* check if requirements is ok
	* create a virtual env
	* pip install -r requirements.txt

	* reference: https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0