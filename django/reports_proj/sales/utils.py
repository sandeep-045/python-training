from profiles.models import Profile
from customers.models import Customer
from io import BytesIO
import base64
import matplotlib.pyplot as plt

def get_salesman(val):
    return Profile.objects.get(id=val).user.username

def get_customer(val):
    return Customer.objects.get(id=val).name


def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph

def get_key(res_by):

    if res_by == '#1':
        return 'transaction_id'
    elif res_by == '#2':
        return 'created'


def get_chart(chart_type,data,results_by,**kwargs):
    plt.switch_backend('AGG')
    
    fig=plt.figure(figsize=(10,4))
    
    key=get_key(results_by)
    # print(data)
    d=data.groupby(key,as_index=False)['total_price'].agg('sum')
    if chart_type =='#1':
        # print('bar chart')
        plt.bar(d[key],d['total_price'])

    elif chart_type =='#2':
        # print('pie')
        
        plt.pie(data=d,x='total_price',labels=d[key].values)
    
    elif chart_type=='#3':
        # print('line')
        plt.plot(d[key],d['total_price'],color='red',marker='*',linestyle='dotted')
    
    else:
        print('Wrong Choice')
    plt.tight_layout()
    chart=get_graph()
    return chart