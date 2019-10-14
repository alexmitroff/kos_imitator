from django.shortcuts import render


def import_test(request):
    return render(request, 'import.html', {'page_title': 'Test import | '})
