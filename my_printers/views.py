from django.shortcuts import render

printers = [
    {
        'id': '1',
        'name': 'EPSON',
        'model': 'ET-2820'
    },
    {
        'id': '2',
        'name': 'HP',
        'model': 'OfficeJet 8015e'
    },
    {
        'id': '3',
        'name': 'CANON',
        'model': 'Pixma TS3350'
    }
]


def printer_list(request):
    context = {'printer_list': printers}
    return render(request, 'my_printers/printer_list.html', context)


def printer_view(request, pk):
    printer_obj = None
    for printer in printers:
        if printer['id'] == pk:
            printer_obj = printer
    context = {'printer': printer_obj}
    return render(request, 'my_printers/printer_view.html', context)
