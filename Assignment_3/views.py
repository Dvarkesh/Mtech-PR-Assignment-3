from django.shortcuts import render, HttpResponse,redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
import pandas as pd
import os,csv
from django.conf import settings
from django.contrib import messages
from os import path
media = settings.MEDIA_ROOT

# Create your views here.
def home(request):
    return render(request,'home.html')


def upload(request):
    if request.method == "POST" and request.FILES:
        uploaded_file = request.FILES["userFile"]
        if uploaded_file.name.split(".")[1] not in ['csv']:
            messages.add_message(request, messages.ERROR, 'Only csv file allowed!')
            return render(request,'home.html')
        fs = FileSystemStorage()
        os.chdir(media)
        if not path.exists(uploaded_file.name) :
            fs.save(uploaded_file.name,uploaded_file)
        return render(request,'upload.html',{'upload_file':uploaded_file.name})
    return render(request,'home.html')


def process(request):

    if request.method == "POST" :
        file_name = request.POST.get('file_name')
        if request.POST.get('print'):
            fields = [] 
            rows = [] 
            with open(path.join(media,file_name), 'r') as csvfile:
                # creating a csv reader object 
                csvreader = csv.reader(csvfile) 
      
                # extracting field names through first row 
                fields = next(csvreader) 
            
                # extracting each data row one by one 
                i=0
                for row in csvreader:
                    if i==5:
                        break
                    else:
                        rows.append(row)
                    i+=1 
            
            return render(request,'process.html',{'fields':fields,'rows':rows,'file_name':file_name})
        elif request.POST.get('summary'):
            data = pd.read_csv(path.join(media,file_name))
            col = data.columns
            df = pd.DataFrame(data)
            r, c = df.shape 
            d = {}
            for i in col:
                d[i] = df[i].dtype
            
            return render(request,'process.html',{'col':c,'row':r,'col_type':d,'file_name':file_name})
        else:
            return render(request,'home.html')
    
        return render(request,'process.html',{'file_name':file_name})
    return render(request,'upload.html')
    
        


        # csv = pd.read_csv(file)
        # print(csv.head())
        

    
    """
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['userFile']
        fs = FileSystemStorage()
        url = fs.save(uploaded_file.name,uploaded_file)
        context['url'] = fs.url(url)
    return render(request,'upload.html', context)
    """


# summary = df.describe()
            # print(col)
            # for i in col:
            #     print(data[i].mean())
            # 'tables':[summary.to_html()]x
            # print(csv_reader)
            
# csv_reader = csv.DictReader(csv_file)
                # print(csv_reader)
                # line_count = 0
                # header = {}
                # for row in csv_reader:
                #     if line_count == 0:
                #         print(row)
                #     line_count+=1
                #         print(f'Column names are {", ".join(row)}')
                #         line_count += 1
                #         print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
                #         line_count += 1
                #     print(f'Processed {line_count} lines.')
        #                 {% for i in df %}
        #     <tr>
        #         {% for col in df.columns %}
        #             <td>
        #                 {{ df.iloc[0][col]}}
        #             </td>
        #         {% endfor %}
        #     </tr>
        # {% endfor %} 

    #      {% for table in tables %}
    # {{ table | safe }}
    # {% endfor %}