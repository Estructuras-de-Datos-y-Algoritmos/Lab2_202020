import pytest
import config as cf
from DataStructures import arraylist as slt
import csv



def cmpfunction (element1, element2):
    if element1["movie_id"] == element2["movie_id"]:
        return 0
    elif element1["movie_id"] < element2["movie_id"]:
        return -1
    else:
        return 1

#@pytest.fixture
def lst ():
    lst = slt.newList(cmpfunction)
    return lst


"""print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")"""

def test_load_file(file,lst,sep=","): #Cargar archivos en lista
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                slt.addLast(lst, row)

def test_list_movies():
    list1= lst["elements"]
    list2= lst["elements"]
    final_lst_movies= lst["elements"]
    file = 'Data/theMoviesdb/MoviesCastingRaw-small.csv'
    file2 = 'Data/theMoviesdb/SmallMoviesDetailsCleaned.csv'
    loadCSVFile(file,list1)
    loadCSVFile(file2,list2)
    for i in range(0,len(list1)):
        tuple_= (list1[i],list2[i])
        final.append(tuple_)
    return final_lst_movies

#@pytest.fixture
def movies(lst):
    nuevas_movies = lst["elements"]
    return(nuevas_movies)

def test_empty (lst):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0

def test_addFirst (lst, movies):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addFirst (lst, movies[1])
    assert slt.size(lst) == 1
    slt.addFirst (lst, movies[2])
    assert slt.size(lst) == 2
    movie = slt.firstElement(lst)
    assert movie == movies[2]


lst=lst()
movies=movies(lst)
test_load_file(lst)
print(movies)


