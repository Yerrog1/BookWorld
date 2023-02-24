def cart_total(request):
    total = 0
    if "cart" in request.session.keys():
        for key, value in request.session['cart'].items():
            total += int(value['acumulated'])
    return {'cart_total': total}








