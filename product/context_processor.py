from .cart_module import Cart

def cart_total_amount(request):
	if request.user.is_authenticated:
		cart = Cart(request)
		total_bill = 0.0
		for key, val in request.session['cart'].items():
			total_bill = total_bill + (float(val['price']))
		return {'cart_total_amount' : total_bill} 
	else:
		return {'cart_total_amount' : 0} 