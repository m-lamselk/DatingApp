from django.shortcuts import render

def main(request):

    profiles = [
    {"first_name": "John", "last_name": "Smith", "gender": 0, "age": 25},
    {"first_name": "Alice", "last_name": "Johnson", "gender": 1, "age": 30},
    {"first_name": "Michael", "last_name": "Brown", "gender": 0, "age": 35},
    {"first_name": "Emily", "last_name": "Davis", "gender": 2, "age": 28},
    {"first_name": "David", "last_name": "Wilson", "gender": 0, "age": 40}
    ]

    return render(request, 'index.html', {"profiles": profiles})