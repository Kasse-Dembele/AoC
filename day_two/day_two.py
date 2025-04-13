def parse_input_file():
    with open("input.txt",'r') as file:
        matrice = []
        for line in file:
            report = line.split()
            matrice.append(report)
        return matrice

def get_ordering_type(prev, next):
    if prev > next:
        return "desc"
    else:
        return "asc"
def is_safe(report):
    acc = int(report.pop(0))
    ordering_type = get_ordering_type(acc,int(report[0]))
    i = 0
    is_still_safe = True
    while i < len(report) and is_still_safe:
        step = abs(int(report[i]) - acc)

        print(step)
        if ( 1 <= step <= 3 ) and ordering_type == get_ordering_type(acc,int(report[i])):
            acc = int(report[i])
            i +=1
        else:

            is_still_safe=False
    return is_still_safe



def count_safe_reports(matrice_report):
    cpt = 0
    for report in matrice_report:
        if is_safe(report):
            cpt = cpt +1
    return cpt



if __name__=="__main__":
   matrice_input = parse_input_file()
   print(matrice_input)
   #print(is_safe(['42', '43', '45', '48', '49']))
   total = count_safe_reports(matrice_input)
   print("Total number of safe reports", total)
