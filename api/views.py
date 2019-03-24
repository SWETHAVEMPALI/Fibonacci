from django.contrib import messages
from django.shortcuts import render
import time

def get_nth_number(num):
    if num < 2:
        return 1
    else:
        prev_number = 1
        current_number = 1
        for i in range(2, num):
            temp = prev_number + current_number
            prev_number = current_number
            current_number = temp
        return current_number

def index(request):
    start_time, nthNumber, time_taken = time.time(), 0, 0
    input_number = request.GET.get('input_number')
    if input_number:
        try:
            input_number = int(input_number)
            nthNumber = get_nth_number(input_number)
            end_time = time.time() - start_time
            time_taken = str(end_time)
        except ValueError:
            messages.warning(request, 'Input has to be a number')
    return render(request, 'index.html', {'nthNumber': nthNumber,'time_taken': time_taken})

