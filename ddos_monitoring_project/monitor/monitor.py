import psutil
import time
import json

def get_system_metrics():
    """Obtiene las métricas del sistema como uso de CPU y memoria."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    return {
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage
    }

def log_metrics():
    """Registra las métricas en un archivo JSON."""
    with open('metrics_log.json', 'a') as log_file:
        while True:
            metrics = get_system_metrics()
            log_file.write(json.dumps(metrics) + '\n')
            log_file.flush()  # Asegúrate de que se escriba inmediatamente
            time.sleep(5)  # Espera 5 segundos antes de la siguiente medición

if __name__ == '__main__':
    log_metrics()
