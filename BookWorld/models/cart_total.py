def cart_total(request):
    total = 0
    if "cart" in request.session.keys():
        for key, value in request.session['cart'].items():
            total += value['price'] * value['quantity']
            total = round(total, 2)
    return {'cart_total': total}








