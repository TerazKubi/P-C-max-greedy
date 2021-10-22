from generator import make_problem_instance

# albo parallel machines
def pc_max_greedy(proc_num, job_tim):
    d = {}
    #przygotowanie procesorow / slownika / dictionary
    for x in range(0, proc_num):
        d.update({str(x): []})

    #dodawanie procesow do pierwszych wolnych procesorow
    for job_time in job_tim:
        index = get_index_of_min_sum_list(d)
        d[str(index)].append(job_time)

    return d


def get_index_of_min_sum_list(di):
    sums = []   
    for i in range(0, len(di)):
        s = sum(di[str(i)])
        if s == 0:
            return i
        else: 
            sums.append(s)
    
    return sums.index(min(sums))



if __name__ == "__main__":
    proc_number=None
    job_number=None
    job_times=[]

    with open('m30.txt', 'r') as plik:
        proc_number=int(plik.readline())
        job_number=int(plik.readline())
        
        for line in plik:
            job_times.append(int(line))

    
    print("\n")
    print("Procesory: ", proc_number)
    print("Procesy: ", job_number)
    print("Dlugosci procesow: ", job_times, end='\n\n')


    #proc_number=5
    #job_number=20
    #job_times=[3, 2, 1, 5, 6, 7, 9, 3, 5, 6, 7, 8, 9, 2, 1, 5, 6, 8, 1, 2]

    slownik = pc_max_greedy(proc_number, job_times)
    print("Ustawienie procesow w procesorach po PCmax:")
    print(slownik, end='\n\n')


    #pokazanie wyniku
    l=[]
    for i in range(0, len(slownik)):
        l.append(sum(slownik[str(i)]))
    
    wynik = max(l)
    print("Wynik P||C max: ", wynik, end='\n\n')
