import random

def make_problem_instance():
    processors_number = random.randint(10, 30)
    process_number = int(processors_number * (random.random() * float(3) + 1))
    process_length_list = []
    for proc in range(0, process_number):
        length = random.randint(5, 35)
        process_length_list.append(length)
    print("processors: ", processors_number)
    print("how much process: ", process_number)
    #print(process_length_list)
    #process_length_list.sort()

    file_output = [processors_number, process_number] + process_length_list
    print(file_output)



    plik = open('instancja.txt', 'w')
    for x in file_output:
        plik.write(str(x) + '\n')

    plik.close()


