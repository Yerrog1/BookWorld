from datetime import datetime
import io
from django.core.mail import EmailMessage
from BookWorld.models import cart_total, Book
from BookWorld.models.invoice import Invoice
from BookWorld.models.invoiceItem import InvoiceItem
from reportlab.pdfgen import canvas


class UserOrder:
    def __init__(self, request, user, cart):
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
        self.invoice.date = datetime.now()
        self.invoice.save()
        self.addInvoiceItems()
        return True

    def sendMail(self):
        subject = 'Gracias por hacer un pedido en BookWorld'
        message = 'Hola, gracias por comprar en BookWorld. ¡Esperamos que disfrutes tus libros!'
        from_email = 'BookWorldMessages@gmail.com'
        recipient_list = [self.user.email]

        # Generar el archivo PDF
        pdf_bytes = io.BytesIO()
        canvas_obj = canvas.Canvas(pdf_bytes)
        self.header(canvas_obj)
        self.foot(canvas_obj)
        self.clientInformation(canvas_obj)
        self.products(canvas_obj)
        canvas_obj.save()

        # Crear el objeto EmailMessage con el archivo adjunto
        pdf = pdf_bytes.getvalue()
        email = EmailMessage(subject, message, from_email, recipient_list)
        email.attach('factura.pdf', pdf, 'application/pdf')

        # Enviar el correo electrónico
        email.send()

    def header(self, canvas_obj):
        logo = 'BookWorld/static/img/image2.png'
        canvas_obj.setFont('Helvetica-Bold', size=14)
        canvas_obj.line(50, 800, 525, 800)
        canvas_obj.drawString(55, 755, 'BookWorld')
        canvas_obj.drawString(240, 700, 'Listado de compras')
        canvas_obj.line(50, 695, 525, 695)
        canvas_obj.drawImage(logo, 450, 700, width=100, height=80)
        canvas_obj.setFont('Helvetica', size=9)

    def foot(self, canvas_obj):
        canvas_obj.line(50, 50, 525, 50)
        fecha = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
        canvas_obj.setFont('Helvetica-Oblique', size=7)
        canvas_obj.drawString(50, 40, str(fecha))
        canvas_obj.drawString(250, 40, str('Listado de compras'))
        canvas_obj.drawString(490, 40, str('Pagina %s' % canvas_obj.getPageNumber()))

    def clientInformation(self, canvas_obj):
        canvas_obj.setFont('Helvetica-Bold', size=9)
        canvas_obj.drawString(55, 680, 'DATOS CLIENTE')
        canvas_obj.drawString(400, 660, 'Nº Factura: ')
        canvas_obj.drawString(400, 645, 'Fecha Factura: ')
        canvas_obj.setFont('Helvetica', size=9)
        canvas_obj.drawString(55, 660, 'DNI/CIF: ' + str(self.user.dni))
        canvas_obj.drawString(55, 645, 'Nombre: ' + str(self.user.name))
        canvas_obj.drawString(55, 630, 'Dirección: ' + str(self.user.address))
        canvas_obj.drawString(480, 660, str(self.invoice.id))
        canvas_obj.drawString(480, 645, datetime.today().strftime('%d-%m-%Y'))
        canvas_obj.drawString(55, 615, 'Correo electronico: ' + str(self.user.email))
        canvas_obj.drawString(55, 600, 'Telefono: ' + str(self.user.phone))

    def products(self, canvas_obj):
        canvas_obj.line(50, 595, 525, 595)
        items = ["ISBN", "Titulo", "Autor", "Precio", "Cantidad"]
        canvas_obj.setFont('Helvetica-Bold', size=10)
        canvas_obj.drawString(70, 580, str(items[0]))
        canvas_obj.drawString(230, 580, str(items[1]))
        canvas_obj.drawString(380, 580, str(items[2]))
        canvas_obj.drawString(440, 580, str(items[3]))
        canvas_obj.drawString(480, 580, str(items[4]))
        canvas_obj.line(50, 575, 525, 575)
        canvas_obj.setFont('Helvetica', size=8)
        i = 55
        j = 565
        for isbn in self.cart.cart:
            if j <= 80:
                canvas_obj.showPage()
                self.header(canvas_obj)
                self.foot(canvas_obj)
                canvas_obj.setFont('Helvetica-Bold', size=10)
                canvas_obj.drawString(65, 675, str(items[0]))
                canvas_obj.drawString(150, 675, str(items[1]))
                canvas_obj.drawString(270, 675, str(items[2]))
                canvas_obj.drawString(370, 675, str(items[3]))
                canvas_obj.drawString(460, 675, str(items[4]))
                canvas_obj.line(50, 670, 525, 670)
                i = 55
                j = 660
            canvas_obj.setFont('Helvetica', size=7)
            book = Book.objects.get(isbn=isbn)
            canvas_obj.drawString(i, j, str(book.isbn))
            canvas_obj.drawString(i + 60, j, str(book.title))
            canvas_obj.drawString(i + 310, j, str(book.author))
            canvas_obj.drawString(i + 390, j, str(book.price))
            canvas_obj.drawString(i + 440, j, str(self.cart.cart[isbn]['quantity']))
            j -= 25

        canvas_obj.line(50, 80, 525, 80)
        canvas_obj.setFont('Helvetica-Bold', size=10)
        canvas_obj.drawString(400, 65, 'Total: ' + str(self.invoice.subtotal) + '€')
