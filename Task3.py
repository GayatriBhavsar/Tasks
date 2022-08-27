import logging

logging.basicConfig(filename="task3.log", level= logging.INFO,format='%(asctime)s %(levelname)s %(name)s %(message)s')

class Task3:
    logging.info("we are now in Task3 class")

    #creating method to extract all dict elements
    def extract_dict_ele(self, l):
        self.l = l
        logging.info('we are accessing extract_dict_ele method')
        try:
            li = []
            for i in l:
                if type(i) == dict:
                    li.append(i)
            return li
        except Exception as e:
            logging.exception(e)

    #creating method to extract all tuple elements
    def extract_tuple_ele(self, l):
        self.l = l
        logging.info("we are accessing the extract_tuple_ele method")
        try:
            li =[]
            for i in l:
                if type(i) == tuple:
                    li.append(i)
            return li
        except Exception as e:
            logging.exception(e)

    #create a method to extract all numerical data from the given data
    def extract_numericData(self , l):
        self.l = l
        logging.info("we are accessing the extract_numericalData method ")
        try:
            li = []
            for i in l:
                if type(i) == int:
                    li.append(i)
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            li.append(j)
                if type(i) == dict:
                    for k, m in i.items():
                        if type(k) == int:
                            li.append(k)
                        if type(m) == int:
                            li.append(m)
            return li
        except Exception as e:
            logging.exception(e)

    #creating a method to do summation of all numerical data from given data
    def summation_numericData(self ,l):
        self.l = l
        logging.info("we are accessing the summation_numericData method ")
        try:
            sum = 0
            for i in l:
                if type(i) == int:
                    sum = sum + i
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            sum = sum + j
                if type(i) == dict:
                    for k, m in i.items():
                        if type(k) == int:
                            sum = sum + k
                        if type(m) == int:
                            sum = sum + m
                        if type(m) == list or type(m) == tuple:
                            for q in m:
                                sum = sum + q
            return sum
        except Exception as e:
            logging.exception(e)

    #creating method to take out odd values from given data
    def extract_oddVal(self, l):
        self.l = l
        logging.info("we are accessing the extract_oddVal method")
        try:
            li = []
            for i in l:
                if i % 2 != 0:
                    li.append(i)
            return li
        except Exception as e:
            logging.exception(e)
    #creating methof to find the ouccrances of all elements in given data
    def ouccrance_of_elements(self , l):
        self.l = l
        logging.info("we are accessing the ouccrance_of_elements method")
        try:
            li =[]
            oc =[]

            for i in l:
                if type(i) == list or  type(i) == set or  type(i) == tuple:
                    for j in i :
                        li.append(j)
                if type(i) == dict:
                    for j, k in i.items():
                        li.append(j)
                        li.append(k)
            #return li
            for i in set(li):
                a = (i, ':', li.count(i))
                oc.append(a)
            return oc
        except Exception as e:
            logging.exception(e)

    #creating method to find out number of keys in given data
    def number_of_keys(self, l):
        self.l = l
        logging.info("we are accessing the number_of_keys method")
        try:
            count = 0
            for i in l:
                if type(i) == dict:
                    count = len(list(i))
            return count
        except Exception as e:
            logging.exception(e)
    #creating method to filter out all string elements from given data
    def etract_stringData(self, l):
        self.l = l
        logging.info("we are accessing the extract_stringDAta method")
        try:
            li = []
            for i in l:
                if type(i) == str:
                    li.append(i)
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str:
                            li.append(j)
                if type(i) == dict:
                    for k, m in i.items():
                        if type(k) == str:
                            li.append(k)
                        if type(m) == str:
                            li.append(m)
            return li
        except Exception as e:
            logging.exception(e)

    #creating method to extract alphanumeric data from given data
    def etract_alphnumData(self,l):
        self.l = l
        logging.info("we are accessing the etract_alphnumData method ")
        try:
            li = []
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str:
                            if j.isalnum() == True:
                                # print(j)
                                li.append(j)
                if type(i) == dict:
                    for m, k in i.items():
                        if type(m) == str:
                            if m.isalnum() == True:
                                li.append(m)
                        if type(k) == str:
                            if k.isalnum() == True:
                                li.append(k)
            return li
        except Exception as e:
            logging.info(e)
    #creating method to do to the multiplication of all numeric data in given data
    def multiplication_of_numData(self,l):
        self.l = l
        logging.info("we are accessing multiplication_of_numData method")
        try:
            mul = 1
            for i in l:
                mul = mul * i
            return mul
        except Exception as e:
            logging.exception(e)
    #creating method to create a flat list of given data by unrapping all data
    def unrapping_all_data(self,l):
        self.l = l
        logging.info("we are accessing the unrapping_all_data method")
        try:
            li = []
            for i in l:
                    if type(i) == list or type(i) == tuple or type(i) == set:
                        for j in i:
                            li.append(j)
                    if type(i) == dict:
                        for m, k in i.items():
                            li.append(m)
                            li.append(k)
            return li
        except Exception as e:
            logging.exception(e)

l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
var_li = Task3()

logging.info(f"extracted dict elements from given data:, {var_li.extract_dict_ele(l)}")
logging.info(f"extracted tuple elements from given data is :, {var_li.extract_tuple_ele(l)}")
logging.info(f"extracted numerical data from given data is:, {var_li.extract_numericData(l)}")
logging.info(f"summation of all numerical data from given data is:, {var_li.summation_numericData(l)}")
logging.info(f"extracted odd values from given data: {var_li.extract_oddVal(var_li.extract_numericData(l))}")
logging.info(f"ouccrances of elements in given data: {var_li.ouccrance_of_elements(l)}")
logging.info(f"number of keys in dict elements of given data: {var_li.ouccrance_of_elements(l)}")
logging.info(f"count of keys from dictionary element in given data: {var_li.number_of_keys(l)}")
logging.info(f"string elements from the given data: {var_li.etract_stringData(l)}")
logging.info(f"extracted alphnumeric data from given data : {var_li.extract_numericData(l)}")
logging.info(f"multiplcation of all numeric data from given data is: {var_li.multiplication_of_numData(var_li.extract_numericData(l))}")
logging.info(f"flat list after unrapping the all data: {var_li.unrapping_all_data(l)}")