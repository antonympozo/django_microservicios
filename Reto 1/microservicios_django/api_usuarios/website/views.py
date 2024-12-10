import pandas as pd
from django.shortcuts import render
from django.contrib import messages
import requests

def upload_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        
        try:
            # Leer el archivo CSV
            df = pd.read_csv(csv_file)
            
            # Verificar las columnas requeridas
            required_columns = ['nombre', 'apellido_paterno', 'apellido_materno', 
                              'edad', 'nombre_cuenta', 'contrasena']
            
            if not all(col in df.columns for col in required_columns):
                messages.error(request, 'El archivo CSV no tiene todas las columnas requeridas')
                return render(request, 'website/upload.html')
            
            # Procesar cada fila
            success_count = 0
            error_count = 0
            
            for _, row in df.iterrows():
                user_data = {
                    'nombre': row['nombre'],
                    'apellido_paterno': row['apellido_paterno'],
                    'apellido_materno': row['apellido_materno'],
                    'edad': int(row['edad']),
                    'nombre_cuenta': row['nombre_cuenta'],
                    'contrasena': row['contrasena']
                }
                
                # Hacer la petición POST al API
                response = requests.post(
                    'http://localhost:8000/api/usuarios',
                    json=user_data
                )
                
                if response.status_code == 200:
                    success_count += 1
                else:
                    error_count += 1
            
            messages.success(request, 
                f'Proceso completado. {success_count} usuarios creados, {error_count} errores.')
            
        except Exception as e:
            messages.error(request, f'Error al procesar el archivo: {str(e)}')
    
    return render(request, 'website/upload.html')