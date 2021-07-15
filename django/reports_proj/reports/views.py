from django.shortcuts import render,HttpResponse,get_object_or_404
from profiles.models import Profile
from django.http import JsonResponse
from .utils import get_report_image
from .models import Report
from django.views.generic import ListView,DetailView,TemplateView
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from sales.models import Sale,Position,CSV
import csv
from products.models import Product
from customers.models import Customer
from django.utils.dateparse import parse_date
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def create_repo_view(request):
    if request.method=='GET':
        return HttpResponse('Im working')
    
    if request.is_ajax():
        # print('In ajax')
        name=request.POST.get('name')
        remarks=request.POST.get('remarks')
        image=request.POST.get('image')
        img=get_report_image(image)
        author=Profile.objects.get(user=request.user)
        Report.objects.create(name=name,remarks=remarks,image=img,author=author)
        
    
        return JsonResponse({'msg':'send'})
    return JsonResponse({'none':'none'})


class ReportListView(LoginRequiredMixin,ListView):
    model = Report
    template_name = "reports/main.html"
    ordering=['-created']


class ReportDetailView(LoginRequiredMixin,DetailView):
    model = Report
    template_name = "reports/detail.html"


class UploadTemplateView(LoginRequiredMixin,TemplateView):
    template_name = "reports/from_file.html"

def csv_upload_view(request):
    
    if request.method=='POST':
        csv_file_name=request.FILES.get('file').name
        csv_file=request.FILES.get('file')
        obj,cre=CSV.objects.get_or_create(file_name=csv_file_name)

        if cre:
            obj.csv_file=csv_file
            obj.save()
            with open(obj.csv_file.path,'r') as f:
                reader=csv.reader(f)
                reader.__next__()
                for row in reader:
                    # print(row,type(row))
                    data=';'.join(row)
                    data=data.split(';')
                    # print(data)
                    # print(len(data))
                    if(len(data) >2):
                        transaction_id=data[1]
                        product=data[2]
                        quantity=int(data[3])
                        customer=data[4]
                        date=parse_date(data[5])
                        print(transaction_id,product,quantity,customer,date)
                    
                    try:
                        product_obj = Product.objects.get(name__iexact=product)
                    
                    except Product.DoesNotExist:

                        product_obj = None
                    
                    if product_obj is not None:

                        customer_obj,_ = Customer.objects.get_or_create(name=customer)
                        salesam_obj = Profile.objects.get(user=request.user)
                        position_obj=Position.objects.create(product=product_obj,quantity=quantity,created=date)

                        sale_obj,__=Sale.objects.get_or_create(transaction_id=transaction_id,customer=customer_obj,salesman=salesam_obj,created=date)

                        sale_obj.positions.add(position_obj)
                        sale_obj.save()
                        return JsonResponse({'ex':False})
        else:
            return JsonResponse({'ex':True})
    return HttpResponse('file being sent')



def render_pdf_view(request,pk):

    obj=get_object_or_404(Report,pk=pk)

    template_path = 'reports/pdf.html'

    context = {'obj':obj}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    
    template = get_template(template_path)
    
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response