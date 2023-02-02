from rest_framework.generics import ListAPIView
from openpyxl.workbook import Workbook
from django.http import HttpResponse
from openpyxl.writer.excel import save_virtual_workbook
import sqlite3


class ReportViewSet(ListAPIView):

    def get(self, request, format=None):

        wb = Workbook()
        with sqlite3.connect('db.sqlite3') as db:
            cursor = db.cursor()
            db_select_query = """SELECT DISTINCT model FROM robots_robot"""
            cursor.execute(db_select_query)
            records = cursor.fetchall()
            for row in records:
                cursor.execute(
                    f"SELECT model, version, COUNT(created) FROM robots_robot WHERE model = '{row[0]}' Group by version")
                rec = cursor.fetchall()
                ws = wb.create_sheet(row[0])
                ws.title = row[0]
                ws['A1'] = 'Модель'
                ws['B1'] = 'Версия'
                ws['C1'] = 'Количество за неделю'
                #todo поправить ширину колонки С
                for data in rec:
                    ws.append(data)
        std = wb.get_sheet_by_name('Sheet')
        wb.remove_sheet(std)
        response = HttpResponse(content=save_virtual_workbook(wb), content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=Production_report.xlsx'
        return response
