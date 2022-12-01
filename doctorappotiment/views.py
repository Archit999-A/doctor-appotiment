from django.shortcuts import render

# Create your views here.
datab={"viral":"Dr.Khurana","orthopadic":"Dr.Muna bhai","Heart disease":"Dr.Circuit","Gyneocologist":"Dr.Jonny Sins"}
def coll(request):
    return render(request,'doct.html')

def find(request):
    name=request.GET["nam"]
    da=request.GET["dat"]
    di=request.GET["dis"] 
    if di in datab:
        f=datab[di]
        return render(request,'appot.html',{'na':name,'doctor':f})

