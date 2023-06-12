from django.shortcuts import render
from django.http import FileResponse
from django.db import connection





def index(request):
    if request.method == 'POST':
        inicio = request.POST.get('inicio')
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        creado = request.POST.get('fecha')

        fecha_asistencia = inicio.split("/")
        fecha_var = fecha_asistencia[0]
        fecha_var2 = fecha_asistencia[1]

        mesesDic = {
            "01":'Enero',
            "02":'Febrero',
            "03":'Marzo',
            "04":'Abril',
            "05":'Mayo',
            "06":'Junio',
            "07":'Julio ',
            "08":'Agosto',
            "09":'Septiembre',
            "10":'Octubre',
            "11":'Noviembre',
            "12":'Diciembre'
        }
        mes = mesesDic[str(fecha_var)][:9]

        
        # #? Nombre Del Documento
        import xlsxwriter
        workbook = xlsxwriter.Workbook('Asistencia.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.set_column(4, 20, 5)
        worksheet.set_column(3, 0, 12)
        worksheet.set_column(1, 3, 20)
        worksheet.set_column(0, 0, 2)
        worksheet.set_column(3, 3, 7)
        worksheet.set_column(2, 2, 0)
        # #? Orientacion De La Pagina
        worksheet.set_landscape()
        worksheet.protect('Construm@s0000')

        

        # Tamaño De Letra
        font_size = workbook.add_format()
        font_size.set_font_size(8)
        font_size.set_align('center')
        

        # Tamaño De Letra
        font_size2 = workbook.add_format()
        font_size2.set_font_size(7.2)
        font_size2.set_align('left')
        font_size2.set_border(1)
        

        # Tamaño De Letra
        font_size3 = workbook.add_format()
        font_size3.set_font_size(8)
        font_size3.set_align('left')
        font_size3.set_border(1)

        # Tamaño De Letra
        font_size4 = workbook.add_format()
        font_size4.set_font_size(8)
        font_size4.set_align('center')
        font_size4.set_border(1)

        
        # Datos Incrustados En El XLSX
        worksheet.write('J1',titulo.upper(),font_size)
        worksheet.write('J2','PERIODO DEL 11 AL 25 DE '+ mes.upper() + ' DEL AÑO 20'+ fecha_var2 ,font_size)
        worksheet.write('B2',subtitulo ,font_size)
        worksheet.write('R1','SISTEMA v1.0' ,font_size)
        worksheet.write('R2','CREADO EL: '+creado ,font_size)



        worksheet.write('B66','_____________',font_size)
        worksheet.write('B67','ELABORADO' ,font_size)
        worksheet.write('B68','IRIS MENDOZA',font_size)
        
        worksheet.write('I66','_________________',font_size)
        worksheet.write('I67','ING. TEDDI GARCIA ' ,font_size)
        worksheet.write('I68','GERENTE DE PRODUCCIÓN: ' ,font_size)


        worksheet.write('R66','_____________________',font_size)
        worksheet.write('R67','LICDA. HILDA VALENCIA' ,font_size)
        worksheet.write('R68','JEFE DE ADMINISTRACIÓN' ,font_size)

        altura_titulo = '4'
        altura_columna = 4

        def empleado_function():
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT DISTINCT numero_empleado, nombre, estatus,estado_empleado FROM asistencia_empleados
                    INNER JOIN asistencia_empleado_datos ON asistencia_empleado_datos.id = asistencia_empleados.nombre_empleado_id
                    WHERE NOT estado_empleado = 0
                """)
                empleado = cursor.fetchall()
            worksheet.write('A'+altura_titulo, 'N°: ',font_size3)
            id_nombre = [item[0] for item in empleado]
            worksheet.write_column(altura_columna, 0, id_nombre,font_size2)

            worksheet.write('B'+altura_titulo, 'NOMBRE:',font_size3)
            id_nombre = [item[1] for item in empleado]
            worksheet.write_column(altura_columna, 1, id_nombre,font_size2)

            worksheet.write('D'+altura_titulo, 'ESTATUS:',font_size3)
            id_nombre = [item[2] for item in empleado]
            worksheet.write_column(altura_columna, 3, id_nombre,font_size2)
        empleado_function()

        def all_fechas():
            
            def fecha11():
                with connection.cursor() as cursor:
                    cursor.execute(F"""
                        SELECT titulo_asistencia, fecha,estados FROM asistencia_asistencia_empleado
                        LEFT JOIN asistencia_asistencia ON asistencia_asistencia.id = asistencia_asistencia_empleado.asistencia_id
                        LEFT JOIN asistencia_empleados ON asistencia_empleados.id = asistencia_asistencia_empleado.empleados_id
						INNER JOIN asistencia_empleado_datos ON asistencia_empleado_datos.id = asistencia_empleados.nombre_empleado_id
                        WHERE NOT estado_empleado = 0 AND fecha = '11/{inicio}' ORDER BY numero_empleado
                    """)
                    asistencia11 = cursor.fetchall()

                fecha = [item[0] == 'DIA - 11' for item in asistencia11]

                if fecha:
                    worksheet.write('E'+altura_titulo, 'DIA 11:',font_size4)
                    nombre = [item[2] for item in asistencia11]
                    worksheet.write_column(altura_columna, 4, nombre,font_size4)
            fecha11()

            def fecha12():
                with connection.cursor() as cursor:
                    cursor.execute(f"""
                        SELECT titulo_asistencia, fecha,estados FROM asistencia_asistencia_empleado
                        LEFT JOIN asistencia_asistencia ON asistencia_asistencia.id = asistencia_asistencia_empleado.asistencia_id
                        LEFT JOIN asistencia_empleados ON asistencia_empleados.id = asistencia_asistencia_empleado.empleados_id
						INNER JOIN asistencia_empleado_datos ON asistencia_empleado_datos.id = asistencia_empleados.nombre_empleado_id
                        WHERE NOT estado_empleado = 0 AND fecha = '12/{inicio}' ORDER BY numero_empleado
                    """)
                    asistencia11 = cursor.fetchall()

                fecha = [item[0] == 'DIA - 12' for item in asistencia11]
                if fecha:
                    worksheet.write('F'+altura_titulo, 'DIA 12:',font_size4)
                    nombre = [item[2] for item in asistencia11]
                    worksheet.write_column(altura_columna, 5, nombre,font_size4)
            fecha12()

            def fecha13():
                with connection.cursor() as cursor:
                    cursor.execute(f"""
                        SELECT titulo_asistencia, fecha,estados FROM asistencia_asistencia_empleado
                        LEFT JOIN asistencia_asistencia ON asistencia_asistencia.id = asistencia_asistencia_empleado.asistencia_id
                        LEFT JOIN asistencia_empleados ON asistencia_empleados.id = asistencia_asistencia_empleado.empleados_id
						INNER JOIN asistencia_empleado_datos ON asistencia_empleado_datos.id = asistencia_empleados.nombre_empleado_id
                        WHERE NOT estado_empleado = 0 AND fecha = '13/{inicio}' ORDER BY numero_empleado
                    """)
                    asistencia11 = cursor.fetchall()

                fecha = [item[0] == 'DIA - 13' for item in asistencia11]

                if fecha:
                    worksheet.write('G'+altura_titulo, 'DIA 13:',font_size4)
                    nombre = [item[2] for item in asistencia11]
                    worksheet.write_column(altura_columna, 6, nombre,font_size4)
            fecha13()

            def fecha14():
                with connection.cursor() as cursor:
                    cursor.execute(f"""
                        SELECT titulo_asistencia, fecha,estados FROM asistencia_asistencia_empleado
                        LEFT JOIN asistencia_asistencia ON asistencia_asistencia.id = asistencia_asistencia_empleado.asistencia_id
                        LEFT JOIN asistencia_empleados ON asistencia_empleados.id = asistencia_asistencia_empleado.empleados_id
						INNER JOIN asistencia_empleado_datos ON asistencia_empleado_datos.id = asistencia_empleados.nombre_empleado_id
                        WHERE NOT estado_empleado = 0 AND fecha = '14/{inicio}' ORDER BY numero_empleado
                    """)
                    asistencia11 = cursor.fetchall()

                fecha = [item[0] == 'DIA - 14' for item in asistencia11]
                if fecha:
                    worksheet.write('H'+altura_titulo, 'DIA 14:',font_size4)
                    nombre = [item[2] for item in asistencia11]
                    worksheet.write_column(altura_columna, 7, nombre,font_size4)
            fecha14()

            def fecha15():
                with connection.cursor() as cursor:
                    cursor.execute(f"""
                        SELECT titulo_asistencia, fecha,estados FROM asistencia_asistencia_empleado
                        LEFT JOIN asistencia_asistencia ON asistencia_asistencia.id = asistencia_asistencia_empleado.asistencia_id
                        LEFT JOIN asistencia_empleados ON asistencia_empleados.id = asistencia_asistencia_empleado.empleados_id
						INNER JOIN asistencia_empleado_datos ON asistencia_empleado_datos.id = asistencia_empleados.nombre_empleado_id
                        WHERE NOT estado_empleado = 0 AND fecha = '15/{inicio}' ORDER BY numero_empleado
                    """)
                    asistencia11 = cursor.fetchall()

                fecha = [item[0] == 'DIA - 15' for item in asistencia11]
                if fecha:
                    worksheet.write('I'+altura_titulo, 'DIA 15:',font_size4)
                    nombre = [item[2] for item in asistencia11]
                    worksheet.write_column(altura_columna, 8, nombre,font_size4)
            fecha15()

            def fecha16():
                with connection.cursor() as cursor:
                    cursor.execute(f"""
                        SELECT titulo_asistencia, fecha,estados FROM asistencia_asistencia_empleado
                        LEFT JOIN asistencia_asistencia ON asistencia_asistencia.id = asistencia_asistencia_empleado.asistencia_id
                        LEFT JOIN asistencia_empleados ON asistencia_empleados.id = asistencia_asistencia_empleado.empleados_id
						INNER JOIN asistencia_empleado_datos ON asistencia_empleado_datos.id = asistencia_empleados.nombre_empleado_id
                        WHERE NOT estado_empleado = 0 AND fecha = '16/{inicio}' ORDER BY numero_empleado
                    """)
                    asistencia11 = cursor.fetchall()

                fecha = [item[0] == 'DIA - 16' for item in asistencia11]
                if fecha:
                    worksheet.write('J'+altura_titulo, 'DIA 16:',font_size4)
                    nombre = [item[2] for item in asistencia11]
                    worksheet.write_column(altura_columna, 9, nombre,font_size4)
            fecha16()

            def fecha17():
                with connection.cursor() as cursor:
                    cursor.execute(f"""
                        SELECT titulo_asistencia, fecha,estados FROM asistencia_asistencia_empleado
                        LEFT JOIN asistencia_asistencia ON asistencia_asistencia.id = asistencia_asistencia_empleado.asistencia_id
                        LEFT JOIN asistencia_empleados ON asistencia_empleados.id = asistencia_asistencia_empleado.empleados_id
						INNER JOIN asistencia_empleado_datos ON asistencia_empleado_datos.id = asistencia_empleados.nombre_empleado_id
                        WHERE NOT estado_empleado = 0 AND fecha = '17/{inicio}' ORDER BY numero_empleado
                    """)
                    asistencia11 = cursor.fetchall()

                fecha = [item[0] == 'DIA - 17' for item in asistencia11]
                if fecha:
                    worksheet.write('K'+altura_titulo, 'DIA 17:',font_size4)
                    nombre = [item[2] for item in asistencia11]
                    worksheet.write_column(altura_columna, 10, nombre,font_size4)
            fecha17()

            def fecha18():
                with connection.cursor() as cursor:
                    cursor.execute(f"""
                        SELECT titulo_asistencia, fecha,estados FROM asistencia_asistencia_empleado
                        LEFT JOIN asistencia_asistencia ON asistencia_asistencia.id = asistencia_asistencia_empleado.asistencia_id
                        LEFT JOIN asistencia_empleados ON asistencia_empleados.id = asistencia_asistencia_empleado.empleados_id
						INNER JOIN asistencia_empleado_datos ON asistencia_empleado_datos.id = asistencia_empleados.nombre_empleado_id
                        WHERE NOT estado_empleado = 0 AND fecha = '18/{inicio}' ORDER BY numero_empleado
                    """)
                    asistencia11 = cursor.fetchall()

                fecha = [item[0] == 'DIA - 18' for item in asistencia11]
                if fecha:
                    worksheet.write('L'+altura_titulo, 'DIA 18:',font_size4)
                    nombre = [item[2] for item in asistencia11]
                    worksheet.write_column(altura_columna, 11, nombre,font_size4)
            fecha18()

            def fecha19():
                with connection.cursor() as cursor:
                    cursor.execute(f"""
                        SELECT titulo_asistencia, fecha,estados FROM asistencia_asistencia_empleado
                        LEFT JOIN asistencia_asistencia ON asistencia_asistencia.id = asistencia_asistencia_empleado.asistencia_id
                        LEFT JOIN asistencia_empleados ON asistencia_empleados.id = asistencia_asistencia_empleado.empleados_id
						INNER JOIN asistencia_empleado_datos ON asistencia_empleado_datos.id = asistencia_empleados.nombre_empleado_id
                        WHERE NOT estado_empleado = 0 AND fecha = '19/{inicio}' ORDER BY numero_empleado
                    """)
                    asistencia11 = cursor.fetchall()

                fecha = [item[0] == 'DIA - 19' for item in asistencia11]
                if fecha:
                    worksheet.write('M'+altura_titulo, 'DIA 19:',font_size4)
                    nombre = [item[2] for item in asistencia11]
                    worksheet.write_column(altura_columna, 12, nombre,font_size4)
            fecha19()

            def fecha20():
                with connection.cursor() as cursor:
                    cursor.execute(f"""
                        SELECT titulo_asistencia, fecha,estados FROM asistencia_asistencia_empleado
                        LEFT JOIN asistencia_asistencia ON asistencia_asistencia.id = asistencia_asistencia_empleado.asistencia_id
                        LEFT JOIN asistencia_empleados ON asistencia_empleados.id = asistencia_asistencia_empleado.empleados_id
						INNER JOIN asistencia_empleado_datos ON asistencia_empleado_datos.id = asistencia_empleados.nombre_empleado_id
                        WHERE NOT estado_empleado = 0 AND fecha = '20/{inicio}' ORDER BY numero_empleado
                    """)
                    asistencia11 = cursor.fetchall()

                fecha = [item[0] == 'DIA - 20' for item in asistencia11]
                if fecha:
                    worksheet.write('N'+altura_titulo, 'DIA 20:',font_size4)
                    nombre = [item[2] for item in asistencia11]
                    worksheet.write_column(altura_columna, 13, nombre,font_size4)
            fecha20()

            def fecha21():
                with connection.cursor() as cursor:
                    cursor.execute(f"""
                        SELECT titulo_asistencia, fecha,estados FROM asistencia_asistencia_empleado
                        LEFT JOIN asistencia_asistencia ON asistencia_asistencia.id = asistencia_asistencia_empleado.asistencia_id
                        LEFT JOIN asistencia_empleados ON asistencia_empleados.id = asistencia_asistencia_empleado.empleados_id
						INNER JOIN asistencia_empleado_datos ON asistencia_empleado_datos.id = asistencia_empleados.nombre_empleado_id
                        WHERE NOT estado_empleado = 0 AND fecha = '21/{inicio}' ORDER BY numero_empleado
                    """)
                    asistencia11 = cursor.fetchall()

                fecha = [item[0] == 'DIA - 21' for item in asistencia11]
                if fecha:
                    worksheet.write('O'+altura_titulo, 'DIA 21:',font_size4)
                    nombre = [item[2] for item in asistencia11]
                    worksheet.write_column(altura_columna, 14, nombre,font_size4)
            fecha21()

            def fecha22():
                with connection.cursor() as cursor:
                    cursor.execute(f"""
                        SELECT titulo_asistencia, fecha,estados FROM asistencia_asistencia_empleado
                        LEFT JOIN asistencia_asistencia ON asistencia_asistencia.id = asistencia_asistencia_empleado.asistencia_id
                        LEFT JOIN asistencia_empleados ON asistencia_empleados.id = asistencia_asistencia_empleado.empleados_id
						INNER JOIN asistencia_empleado_datos ON asistencia_empleado_datos.id = asistencia_empleados.nombre_empleado_id
                        WHERE NOT estado_empleado = 0 AND fecha = '22/{inicio}' ORDER BY numero_empleado
                    """)
                    asistencia11 = cursor.fetchall()

                fecha = [item[0] == 'DIA - 22' for item in asistencia11]
                if fecha:
                    worksheet.write('P'+altura_titulo, 'DIA 22:',font_size4)
                    nombre = [item[2] for item in asistencia11]
                    worksheet.write_column(altura_columna, 15, nombre,font_size4)
            fecha22()

            def fecha23():
                with connection.cursor() as cursor:
                    cursor.execute(f"""
                        SELECT titulo_asistencia, fecha,estados FROM asistencia_asistencia_empleado
                        LEFT JOIN asistencia_asistencia ON asistencia_asistencia.id = asistencia_asistencia_empleado.asistencia_id
                        LEFT JOIN asistencia_empleados ON asistencia_empleados.id = asistencia_asistencia_empleado.empleados_id
						INNER JOIN asistencia_empleado_datos ON asistencia_empleado_datos.id = asistencia_empleados.nombre_empleado_id
                        WHERE NOT estado_empleado = 0 AND fecha = '23/{inicio}' ORDER BY numero_empleado
                    """)
                    asistencia11 = cursor.fetchall()

                fecha = [item[0] == 'DIA - 23' for item in asistencia11]
                if fecha:
                    worksheet.write('Q'+altura_titulo, 'DIA 23:',font_size4)
                    nombre = [item[2] for item in asistencia11]
                    worksheet.write_column(altura_columna, 16, nombre,font_size4)
            fecha23()

            def fecha24():
                with connection.cursor() as cursor:
                    cursor.execute(f"""
                        SELECT titulo_asistencia, fecha,estados FROM asistencia_asistencia_empleado
                        LEFT JOIN asistencia_asistencia ON asistencia_asistencia.id = asistencia_asistencia_empleado.asistencia_id
                        LEFT JOIN asistencia_empleados ON asistencia_empleados.id = asistencia_asistencia_empleado.empleados_id
						INNER JOIN asistencia_empleado_datos ON asistencia_empleado_datos.id = asistencia_empleados.nombre_empleado_id
                        WHERE NOT estado_empleado = 0 AND fecha = '24/{inicio}' ORDER BY numero_empleado
                    """)
                    asistencia11 = cursor.fetchall()

                fecha = [item[0] == 'DIA - 24' for item in asistencia11]
                if fecha:
                    worksheet.write('R'+altura_titulo, 'DIA 24:',font_size4)
                    nombre = [item[2] for item in asistencia11]
                    worksheet.write_column(altura_columna, 17, nombre,font_size4)
            fecha24()

            def fecha25():
                with connection.cursor() as cursor:
                    cursor.execute(f"""
                        SELECT titulo_asistencia, fecha,estados FROM asistencia_asistencia_empleado
                        LEFT JOIN asistencia_asistencia ON asistencia_asistencia.id = asistencia_asistencia_empleado.asistencia_id
                        LEFT JOIN asistencia_empleados ON asistencia_empleados.id = asistencia_asistencia_empleado.empleados_id
						INNER JOIN asistencia_empleado_datos ON asistencia_empleado_datos.id = asistencia_empleados.nombre_empleado_id
                        WHERE NOT estado_empleado = 0 AND fecha = '25/{inicio}' ORDER BY numero_empleado
                    """)
                    asistencia11 = cursor.fetchall()

                fecha = [item[0] == 'DIA - 25' for item in asistencia11]
                if fecha:
                    worksheet.write('S'+altura_titulo, 'DIA 25:',font_size4)
                    nombre = [item[2] for item in asistencia11]
                    worksheet.write_column(altura_columna, 18, nombre,font_size4)
            fecha25()

        all_fechas()
        workbook.close()

        def create_pdf():
            import win32com
            from win32com import client
            import os
            import pythoncom
            #currentDir = os.path.abspath('.')
            currentDir = os.getcwd()
            xlApp = win32com.client.Dispatch("Excel.Application",pythoncom.CoInitialize())
            books = xlApp.Workbooks.Open(os.path.join(currentDir,"Asistencia.xlsx"))    
            ws = books.Worksheets[0]
            ws.Visible = 1
            ws.ExportAsFixedFormat(0,os.path.join(currentDir,"Asistencia"))
            books.Close()
        create_pdf()
        return FileResponse(open('Asistencia.pdf', 'rb'), content_type='application/pdf')
    return render(request,'index.html')