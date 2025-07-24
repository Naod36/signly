from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import UploadedPDF
import base64
import os
from django.core.files.base import ContentFile
from django.templatetags.static import static
from django.http import FileResponse, Http404
from urllib.parse import urljoin




def home(request):
    return render(request, 'theme/home.html')  # ← change this

def upload(request):
    if request.method == 'POST':
        obj = UploadedPDF.objects.create(pdf=request.FILES['pdf'])
        request.session["pdf_id"] = obj.pk  # store PDF ID in session
        return redirect('draw_signature')  # or wherever
    return render(request, 'theme/upload.html')

def view_pdf(request, pk):
    pdf = get_object_or_404(UploadedPDF, pk=pk)
    raw_signature_path = request.session.get("signature_path")
    if raw_signature_path:
        # Normalize slashes for URLs
        signature_path = raw_signature_path.replace("\\", "/")
        signature_url = urljoin(settings.MEDIA_URL, signature_path)
    else:
        signature_url = None

    # 👇 Add this line to extract just the filename
    pdf_filename = os.path.basename(pdf.pdf.name)

    return render(request, 'theme/view_pdf.html', {
        "signature_url": signature_url,
        'pdf': pdf,
        'pdf_filename': pdf_filename,  # ✅ Add this
        
    })

    

def draw_signature(request):
    if request.method == "POST":
        signature_data = request.POST.get("signature_data")
        pdf_id = request.session.get("pdf_id")  # grab from session
       
        if signature_data and pdf_id:
            format, imgstr = signature_data.split(";base64,")
            ext = format.split("/")[-1]
            signature_file = ContentFile(base64.b64decode(imgstr), name="signature." + ext)

            signature_filename = f"signature.{ext}"
            signature_folder = "signatures"
            signature_path = os.path.join(signature_folder, signature_filename)
            
            print("✅ Saving signature path to session:", signature_path)  # Add this

            full_path = os.path.join(settings.MEDIA_ROOT, signature_path)

            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "wb") as f:
                f.write(signature_file.read())
            # ✅ Store clean, URL-ready relative path in session
            relative_path = os.path.relpath(full_path, settings.MEDIA_ROOT).replace("\\", "/")
            request.session["signature_path"] = relative_path

            request.session["signature_path"] = signature_path
            
            print("✅ Final saved relative path:", relative_path)

            return redirect("view_pdf", pk=pdf_id)
    return render(request, "theme/draw_signature.html")

# def serve_pdf(request, filename):
#     file_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', filename)
#     if os.path.exists(file_path):
#         return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
#     raise Http404("PDF not found")

# def serve_pdf(request, filename):
#     file_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', filename)
#     if os.path.exists(file_path):
#         return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
#     else:
#         return HttpResponseNotFound("PDF not found")
