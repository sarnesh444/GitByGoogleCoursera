import psutil

def check_cpu_usage(percent):
    usage=psutil.cpu_percent()
    return usage<percent

if not check_cpu_usage(75):
    print("ERROR! CPU is overloaded")
else:
    print("CPU is'nt under stress")
    print("this line has been added")
