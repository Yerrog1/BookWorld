import datetime

from PyQt6 import QtSql

from BookWorld.models import cart_total, Book
from BookWorld.models.invoice import Invoice
from BookWorld.models.invoiceItem import InvoiceItem
from django.core.mail import send_mail
class UserSession:
    def __init__(self,request, user, cart):
        self.request = request
        self.user = user
        self.cart = cart
        self.invoice = None

    def addInvoiceItems(self):
        for isbn in self.cart.cart:
            invoiceItem = InvoiceItem()
            invoiceItem.invoice = self.invoice
            invoiceItem.isbn = Book.objects.get(isbn=isbn)
            invoiceItem.title = self.cart.cart[isbn]['name']
            invoiceItem.quantity = self.cart.cart[isbn]['quantity']
            invoiceItem.price = self.cart.cart[isbn]['price']
            invoiceItem.total = self.cart.cart[isbn]['subtotal']
            invoiceItem.save()

    def saveInvoice(self):
        self.invoice = Invoice()
        self.invoice.user = self.user
        self.invoice.subtotal = cart_total(self.request)['cart_total']
        self.invoice.date = datetime.date.today()
        self.invoice.save()
        self.addInvoiceItems()
        return True

    def sendMail(self):
        subject = 'Gracias por hacer un pedido en BookWorld'
        message = 'Hola, gracias por comprar en BookWorld. ¡Esperamos que disfrutes tus libros!'

        from_email = 'BookWorldMessages@gmail.com'
        recipient_list = [self.user.email]

        # Enviar el correo electrónico
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
