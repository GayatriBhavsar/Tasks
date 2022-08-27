import logging

logging.basicConfig(filename="list.log", level=logging.INFO,format='%(asctime)s %(levelname)s %(name)s %(message)s')

class ListTask:
    logging.info("we are acessing the listTask class now")

    def __list__(self, l, a , lis):
        self.l = l
        self.a = a
        self.lis = lis
    #creating method to reverse the list
    def reverse_list(self, l):
        self.l = l
        logging.info("we are in reverse_list method")
        try:
            self.lis = l[::-1]
            return self.lis
        except Exception as e:
            logging.exception(e)

    #creating method for checking the element is present in the list
    def access_list_element(self,l,access_val ):
        self.l = l
        self.access_val = access_val
        logging.info("we are in access_list_element method")
        try:
            for i in l:
                if i == access_val:
                    return True, i
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if j == access_val:
                            return True, j
                if type(i) == dict:
                    for n, k in i.items():
                        if n == access_val:
                            return True, n
                        if type(k) == int:
                            for s in k:
                                if s == access_val:
                                    return True, s
                        else:
                            if k == access_val:
                                return True, k
        except Exception as e:
            logging.exception(e)

    #creating method to extract the dict elements Keys and value
    def extract_dict_elements(self, l):
        logging.info("we are in the extract_dict_elements method")
        self.l = l
        try:
            for i in l:
                if type(i) == dict:
                    return i.keys(), i.values()
        except Exception as e:
            logging.exception(e)

    #creating method to extract all list elements from given data
    def extract_listData(self, l):
        self.l = l

        logging.info("we are in the extract_listData method")
        try:
            li = []
            for i in l:
                if type(i) == list:
                    li.append(i)
                if type(i) == dict:
                    for j, k in i.items():
                        if type(k) == list:
                            li.append(k)
            return li
        except Exception as e:
            logging.exception(e)

var_list = ListTask()

o_list = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
logging.info(f"output for reverse list function is:, {var_list.reverse_list(o_list)}")
logging.info(f"given element is present in list:{var_list.access_list_element(o_list,'key1')}")
logging.info(f"dictionary elements are:,{var_list.extract_dict_elements(o_list)} ")
logging.info(f"list elements from the given data:, {var_list.extract_listData(o_list)}")