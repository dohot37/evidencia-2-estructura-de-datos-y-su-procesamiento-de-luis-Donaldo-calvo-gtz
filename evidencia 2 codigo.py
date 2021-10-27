import pandas as pd
import time 
import datetime 
import csv

materiales = {}
switchG = True
separador = ("*" * 50)
folio = 0

while switchG:
    print(separador)
    print("**MENÚ PRINCIPAL**")
    print("|1. Registro de una Venta|")
    print("|2. Consultar una Venta  |")
    print("|3. Reporte de Ventas    |")
    print("|4. Salir                |")
    
    eleccion = int(input("¿Qué opción elegira? "))
    
    if eleccion == 1:
        switchA = True
        while switchA:
            descripcion = input("Dame su Descripcion Producto: ")
            cantidad_piezas = int(input("Dame su Cantidad de Piezas a Vender: "))
            precio_venta = float(input("Dame su Precio Venta: "))
            monto_total = cantidad_piezas * precio_venta
            print(f"El monto total a pagar es de ${monto_total}")
            fecha_venta = datetime.date.today()
            folio = folio + 1 
            materiales[folio] = [fecha_venta,descripcion,cantidad_piezas,precio_venta,monto_total]
            print("**VENTA AGREGADA**")
            decision = int(input("¿Quiere seguir introduciendo productos? 1)Si 2)No "))
            if decision == 2:
                switchA = False
    elif eleccion == 2:
        materiales_ventas = pd.DataFrame(materiales,index = ["Fecha de venta","Descripcion","Cantidad Piezas Vendidas","Precio Unitario de Venta","Monto total de la venta"])
        print(materiales_ventas)
        materiales_ventas.to_csv (r'llantas_Ventas.csv',index=True, header=True)

    elif eleccion == 3:
        
        materiales_vv = materiales_ventas
        montototal=0
        fecha_consulta = input("Ingrese la fecha de la venta que desea consultar (DD/MM/YYYY): ")
        fecha_procesada = datetime.datetime.strptime(fecha_consulta,"%d/%m/%Y").date()
        ventasfecha = materiales_vv.loc["Fecha de venta"]
        print(ventasfecha)
        for x in ventasfecha:
            if fecha_procesada == x:
                monto = materiales_vv.loc["Monto total de la venta"]
                for y in monto:
                    montototal = montototal+y
                    print(f"El Monto Total de {fecha_consulta} fue de {montototal}")
    elif eleccion == 4:
        witchG = False
        print("SALIDA DEL PROGRAMA")
    else:
        print("Esta opción no es válida")
