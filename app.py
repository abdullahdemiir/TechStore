from flask import Flask, render_template, url_for, request, session, redirect
import uuid

app = Flask(__name__)
app.secret_key = 'supersecretkey'
email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    categories = ['Cars', 'Aircrafts', 'Boats', 'Educational Vehicles']
    return render_template('products.html', categories=categories)

@app.route('/academy')
def academy():
    return render_template('academy.html')

@app.route('/academy/cars')
def academy_cars():
    return render_template('academy_cars.html')

@app.route('/academy/educational-vehicles')
def academy_educational_vehicles():
    return render_template('academy_educational_vehicles.html')

@app.route('/academy/boats')
def academy_boats():
    return render_template('academy_boats.html')

@app.route('/academy/aircrafts')
def academy_aircrafts():
    return render_template('academy_aircrafts.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        feedback_message = f"Thank you, {name}! We have received your message about '{subject}'. We'll get back to you soon."
        return render_template('feedback.html', message=feedback_message)
    return render_template('contact.html')

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_name = request.form['product_name']
    price = float(request.form['price'])
    quantity = request.form.get('quantity')
    if not quantity or not quantity.isdigit() or int(quantity) < 1:
        flash("Please enter a valid quantity (1 or more).")
        return redirect(url_for('products'))

    quantity = int(quantity)
    image = request.form.get('image', 'default.jpg')

    if 'cart' not in session:
        session['cart'] = []

    cart = session['cart']
    for item in cart:
        if item['name'] == product_name:
            item['quantity'] += quantity
            item['total_price'] = item['quantity'] * item['price']
            break
    else:
        cart.append({'name': product_name, 'price': price, 'quantity': quantity, 'total_price': price * quantity, 'image': image})

    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    total = sum(item['total_price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    product_name = request.form['product_name']
    cart = session.get('cart', [])
    cart = [item for item in cart if item['name'] != product_name]
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/checkout')
def checkout():
    cart = session.get('cart', [])
    total = sum(item['total_price'] for item in cart)
    return render_template('checkout.html', cart=cart, total=total)

@app.route('/submit_order', methods=['POST'])
def submit_order():
    name = request.form['name']
    address = request.form['address']
    city = request.form['city']
    postal_code = request.form['postal_code']
    country = request.form['country']
    total_amount = sum(item['total_price'] for item in session.get('cart', []))
    session.pop('cart', None)
    return redirect(url_for('order_confirmation', name=name, address=address, city=city, postal_code=postal_code, country=country, total_amount=total_amount))

@app.route('/order_confirmation')
def order_confirmation():
    name = request.args.get('name')
    address = request.args.get('address')
    city = request.args.get('city')
    postal_code = request.args.get('postal_code')
    country = request.args.get('country')
    total_amount = request.args.get('total_amount')
    order_number = str(uuid.uuid4())
    return render_template('order_confirmation.html', order_number=order_number, shipping_address=f"{address}, {city}, {postal_code}, {country}", total_amount=total_amount, name=name)

if __name__ == '__main__':
    app.run(debug=True)
