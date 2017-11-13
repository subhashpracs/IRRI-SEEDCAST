from django.shortcuts import render
import xlwt
from django.utils.translation import ugettext
import io
from SeedCast import resources
import xlsxwriter
from django.http import HttpResponse, request
from django.contrib.auth.models import User


#actions = [export_csv, export_xls, export_xlsx]

# Create your views here.


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_style.font.italic = True

    columns = ['Username', 'First name', 'Last name', 'Email address', ]

#  'shop_name', 'licence_num', 'company_type', 'dealer_name', 'contact_num', 'address', 'state', 'district', 'block', 'spo', 'date', 'pincode'
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_xls(request):
    dealer_resource = resources.DealerResource()
    dataset = dealer_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Dealers_List.xlsx"'
    return response
    #output = io.BytesIO()
    # workbook = xlsxwriter.Workbook('Dealers_list.xlsx')
    #
    # worksheet = workbook.add_worksheet("Dealers_Registration")
    #
    # title = workbook.add_format({
    #     'bold': True,
    #     'font_size': 15,
    #     'align': 'center',
    #     'valign': 'vcenter'
    # })
    #
    # header = workbook.add_format({
    #     'bg_color': '#F7F7F7',
    #     'color': 'black',
    #     'align': 'center',
    #     'valign': 'top',
    #     'border': 1
    # })
    # worksheet.write(0, 0, ugettext("ID"), header)
    # worksheet.write(0, 1, ugettext("Shop Name"), header)
    # worksheet.write(0, 2, ugettext("Licence Number"), header)
    # worksheet.write(0, 3, ugettext("Company Type"), header)
    # worksheet.write(0, 4, ugettext("Dealer Name"), header)
    # worksheet.write(0, 5, ugettext("Contact Number"), header)
    # worksheet.write(0, 6, ugettext("Address"), header)
    # worksheet.write(0, 7, ugettext("State"), header)
    # worksheet.write(0, 8, ugettext("District"), header)
    # worksheet.write(0, 9, ugettext("Block"), header)
    # worksheet.write(0, 10, ugettext("SPO"), header)
    # worksheet.write(0, 11, ugettext("Date"), header)
    # worksheet.write(0, 12, ugettext("PinCode"), header)



    # worksheet.write(0, 0, "ID", header)
    # worksheet.write(0, 1, "Shop Name", header)
    # worksheet.write(0, 2, "Licence Number", header)
    # worksheet.write(0, 3, "Company Type", header)
    # worksheet.write(0, 4, "Dealer Name", header)
    # worksheet.write(0, 5, "Contact Number", header)
    # worksheet.write(0, 6, "Address", header)
    # worksheet.write(0, 7, "State", header)
    # worksheet.write(0, 8, "District", header)
    # worksheet.write(0, 9, "Block", header)
    # worksheet.write(0, 10, "SPO", header)
    # worksheet.write(0, 11, "Date", header)
    # worksheet.write(0, 12, "PinCode", header)

    #Data to be added here...

    # workbook.close()
    # xlsx_data = output.getvalue()
    # #xlsx_data contains the Excel file
    # return xlsx_data
    #




