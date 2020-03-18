from django.shortcuts import render
import csv,io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from webapp.models import Contact
from webapp.admin import ContactAdmin
# Create your views here.

@permission_required('admin.can_add_log_entry')
def contact_upload(request):
    template = "contact_upload.html"
    # return render(request,'myapp/contact_upload.html')

    prompt = {
        'order':'Order of the CSV should be first_name,last_name,email,ip_address,message'

    }
    if request.method == 'GET':
        return render(request,template,prompt)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file')
    data_set=csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string,delimiter=',',quotechar="|"):
        _,created = Contact.objects.update_or_create(
            first_name=column[0],
            last_name=column[1],
            email=column[2],
            ip_address=column[3],
            message=column[4],


        )
    context = {}
    return render(request,template,context)


def retrieve_data_view(request):
    contact=Contact.objects.all()
    return render(request,'index.html',{'contact':contact})