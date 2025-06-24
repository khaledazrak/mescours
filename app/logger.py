import datetime

def log_request(request, response):
    log = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "method": request.method,
        "url": str(request.url),
        "status_code": response.status_code
    }
    print(log)

