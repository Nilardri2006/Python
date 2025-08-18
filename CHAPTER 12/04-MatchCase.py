def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not-found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

print (http_status(200))
print (http_status(100))