from flask import Blueprint, render_template, request, redirect, url_for
from models.purchase import Purchase
from models.payment import Payment
from models.delivery import Delivery
from extensions import db

order = Blueprint('order', __name__)

@order.route('/purchase', methods=['GET', 'POST'])
def purchase_book():
    if request.method == 'POST':
        book_id = request.form['book_id']
        buyer_id = request.form['buyer_id']
        purchase = Purchase(book_id=book_id, buyer_id=buyer_id)
        db.session.add(purchase)
        db.session.commit()
        return redirect(url_for('order.payment_page', purchase_id=purchase.id))
    return render_template('purchase.html')

@order.route('/payment/<int:purchase_id>', methods=['GET', 'POST'])
def payment_page(purchase_id):
    if request.method == 'POST':
        method = request.form['method']
        amount = request.form['amount']
        payment = Payment(purchase_id=purchase_id, method=method, amount=amount)
        db.session.add(payment)
        db.session.commit()
        return redirect(url_for('order.delivery_page', purchase_id=purchase_id))
    return render_template('payment.html', purchase_id=purchase_id)

@order.route('/delivery/<int:purchase_id>', methods=['GET', 'POST'])
def delivery_page(purchase_id):
    if request.method == 'POST':
        provider = request.form['provider']
        address = request.form['address']
        delivery = Delivery(purchase_id=purchase_id, provider=provider, address=address)
        db.session.add(delivery)
        db.session.commit()
        return "Orden completada"
    return render_template('delivery_options.html', purchase_id=purchase_id)
