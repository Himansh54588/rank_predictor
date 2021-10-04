import pickle
import json
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
poly_reg_gen = PolynomialFeatures(degree = 4)

__category = None
__data_columns = None
__modelgen = None
__modelews = None
__modelobc = None
__modelsc = None
__modelst = None


def get_rank(category,marks):
    load_saved_artifacts()
    if category=="General":
        return int(__modelgen.predict(poly_reg_gen.fit_transform([[marks]])))
    elif category=="Ews":
        return int(__modelews.predict(poly_reg_gen.fit_transform([[marks]])))
    elif category=="Obc":
        return int(__modelobc.predict(poly_reg_gen.fit_transform([[marks]])))
    elif category=="Sc":
        return int(__modelsc.predict(poly_reg_gen.fit_transform([[marks]])))
    elif category=="St":
        return int(__modelst.predict(poly_reg_gen.fit_transform([[marks]])))




def get_category():
    load_saved_artifacts()
    return __category


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __category

    with open("./artifacts/category.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __category = __data_columns 

    global __modelgen
    global __modelews
    global __modelobc
    global __modelsc
    global __modelst
    if __modelgen is None:
        with open('./artifacts/general.pickle', 'rb') as f1:
            __modelgen = pickle.load(f1)
    if __modelobc is None:
        with open('./artifacts/obc.pickle', 'rb') as f2:
            __modelobc = pickle.load(f2)
    if __modelews is None:
        with open('./artifacts/ews.pickle', 'rb') as f3:
            __modelews = pickle.load(f3)
    if __modelsc is None:
        with open('./artifacts/sc.pickle', 'rb') as f4:
            __modelsc = pickle.load(f4)
    if __modelst is None:
        with open('./artifacts/st.pickle', 'rb') as f5:
            __modelst = pickle.load(f5)



    print("loading saved artifacts...done")

# def get_location_names():
#     return __locations

# def get_data_columns():
#     return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_category())
    print(get_rank("Obc" ,120))
    