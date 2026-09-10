import urllib.request
import json

# 1. La URL de tu endpoint
url = "http://127.0.0.1:8000/api/rutas/buscar-rutas/"

# 2. Los datos a enviar (Punto A: Mariscal Castilla, Punto B: Plaza de Armas)
# Nota: Usé coordenadas aproximadas de Arequipa. 
payload = {
    "punto_a": {"lat": -16.3925, "lng": -71.5180}, 
    "punto_b": {"lat": -16.3988, "lng": -71.5369}
}

# Preparar la solicitud
data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})

print(f"📡 Enviando solicitud a {url}...")
print(f"📍 Puntos: {payload}")

try:
    # 3. Enviar la solicitud y recibir respuesta
    with urllib.request.urlopen(req) as response:
        resultado = json.loads(response.read().decode('utf-8'))
        
        print("\n✅ ¡RESPUESTA RECIBIDA!")
        print(f"Rutas encontradas: {len(resultado)}")
        
        # Mostrar detalles bonitos
        for ruta in resultado:
            print(f"------------------------------------------------")
            print(f"🚍 Empresa: {ruta.get('empresa')}")
            print(f"🛣️  Ruta:    {ruta.get('nombre_ruta')} ({ruta.get('sentido')})")
            print(f"🎨 Color:   {ruta.get('color')}")
            print(f"📍 Coordenadas (puntos para dibujar): {len(ruta.get('coordenadas', []))} puntos")

except urllib.error.HTTPError as e:
    print(f"\n❌ Error del servidor: {e.code}")
    print(e.read().decode())
except Exception as e:
    print(f"\n❌ Error de conexión: {e}")