from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'ecommerce_secret'

# Sample product data
products = [
    {'id': 1, 'name': 'Laptop', 'price': 1000},
    {'id': 2, 'name': 'Smartphone', 'price': 500},
    {'id': 3, 'name': 'Headphones', 'price': 150}
]

# Home page showing the list of products
@app.route('/')
def home():
    return render_template('home.html', products=products)

# Add product to cart
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    product = next((item for item in products if item['id'] == product_id), None)
    if product:
        session['cart'].append(product)
    return redirect(url_for('home'))

# View cart
@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

# Checkout route
@app.route('/checkout')
def checkout():
    session.pop('cart', None)  # Clear the cart after checkout
    return 'Thank you for your purchase!'

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
