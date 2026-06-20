from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import requests

from .models import Lead


# ---------------- N8N AUTOMATION ----------------

def send_to_n8n(lead):
    url = "http://localhost:5678/webhook-test/new-lead"
    data = {
        "name": lead.name,
        "email": lead.email,
        "phone": lead.phone,
        "company": lead.company,
        "message": lead.message,
        "status": lead.status,
    }
    try:
        response = requests.post(url, json=data, timeout=10)
        print("N8N RESPONSE:", response.status_code)
        print(response.text)
    except Exception as e:
        print("N8N ERROR:", e)


# ---------------- DASHBOARD ----------------

@login_required
def dashboard(request):
    search = request.GET.get('search', '')
    status = request.GET.get('status', 'all')

    leads = Lead.objects.all().order_by('-id')

    if status != "all":
        leads = leads.filter(status=status)

    if search:
        leads = leads.filter(name__icontains=search) | \
                leads.filter(email__icontains=search) | \
                leads.filter(company__icontains=search)

    paginator = Paginator(leads, 5)
    page = request.GET.get('page')
    leads = paginator.get_page(page)

    context = {
        "leads": leads,
        "search_query": search,
        "status_filter": status,

        "total_leads": Lead.objects.count(),
        "new_leads": Lead.objects.filter(status="new").count(),
        "contacted": Lead.objects.filter(status="contacted").count(),
        "in_progress": Lead.objects.filter(status="progress").count(),  # ✅ ADDED
        "converted": Lead.objects.filter(status="converted").count(),
    }

    return render(request, "leads/dashboard.html", context)


# ---------------- CONTACT FORM ----------------

@login_required
def contact(request):
    if request.method == "POST":
        lead = Lead.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            company=request.POST['company'],
            message=request.POST['message'],
            status="new"
        )
        send_to_n8n(lead)
        return redirect("dashboard")

    return render(request, "leads/contact.html")


# ---------------- STATUS CYCLE ----------------

@login_required
def update_status(request, id):
    lead = get_object_or_404(Lead, id=id)

    # ✅ FIXED: new → contacted → in_progress → converted → new
    cycle = {
        "new": "contacted",
        "contacted": "progress",
        "progress": "converted",
        "converted": "new",
    }
    lead.status = cycle.get(lead.status, "new")
    lead.save()
    send_to_n8n(lead)

    return redirect("dashboard")


# ---------------- EDIT ----------------

@login_required
def edit_lead(request, id):
    lead = get_object_or_404(Lead, id=id)

    if request.method == "POST":
        lead.name = request.POST['name']
        lead.email = request.POST['email']
        lead.phone = request.POST['phone']
        lead.company = request.POST['company']
        lead.message = request.POST['message']
        lead.status = request.POST['status']
        lead.save()
        send_to_n8n(lead)
        return redirect("dashboard")

    return render(request, "leads/edit_lead.html", {"lead": lead})


# ---------------- DELETE ----------------

@login_required
def delete_lead(request, id):
    lead = get_object_or_404(Lead, id=id)
    lead.delete()
    return redirect("dashboard")