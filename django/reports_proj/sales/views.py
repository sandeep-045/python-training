from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Sale
from .forms import SalesSearchForm
import pandas as pd
from reports.forms import ReportForm
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
    sales_df=None
    positions_df=None
    merged_df=None
    df=None
    chart=None
    no_data=None
    search_form=SalesSearchForm(request.POST or None)
    report_form=ReportForm()
    
    qs=Sale.objects.all()

    if request.method=='POST':
        date_from  = request.POST.get('date_from')
        date_to    = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        results_type = request.POST.get('results_type')
        sale_qs    = Sale.objects.filter(created__date__gte = date_from,created__date__lte= date_to)
        if len(sale_qs)>0:
            sales_df=pd.DataFrame(sale_qs.values())
            
            sales_df['customer_id']=sales_df['customer_id'].apply(get_customer)
            sales_df['salesman_id']=sales_df['salesman_id'].apply(get_salesman)
            sales_df['created']=sales_df['created'].apply(lambda x:x.strftime('%Y-%m-%d'))
            sales_df['updated']=sales_df['updated'].apply(lambda x:x.strftime('%Y-%m-%d'))
            sales_df.rename(columns={'customer_id':'customer','salesman_id':'salesman','id':'sales_id'},inplace=True)
            
            
            
            positions_data=[]
            for sale in sale_qs:
                for pos in sale.get_positions():
                    obj={
                        'position_id':pos.id,
                        'product':pos.product.name,
                        'quantity':pos.quantity,
                        'price':pos.price,
                        'sales_id':pos.get_sales_id(),
                    }
                
                positions_data.append(obj)
            
            positions_df=pd.DataFrame(positions_data)
            merged_df=pd.merge(sales_df,positions_df,on='sales_id')
            # print(merged_df)
            df= merged_df.groupby('transaction_id',as_index=False)['price'].agg('sum')

            chart=get_chart(chart_type,sales_df,results_type)

            merged_df=merged_df.to_html()
            sales_df = sales_df.to_html()
            positions_df=positions_df.to_html()
            df=df.to_html()
            
        else:
            no_data="You Don't have any data in this date range"
    
    context={'search_form':search_form,'sdf':sales_df,'pdf':positions_df,'mdf':merged_df,'df':df,'chart':chart,'report_form':report_form,'no_data':no_data}
    return render(request,'sales/home.html',context)


class SaleListView(LoginRequiredMixin,ListView):
    model = Sale
    context_object_name='sales'
    template_name = "sales/main.html"

class SaleDetailView(LoginRequiredMixin,DetailView):
    model=Sale
    template_name='sales/detail.html'