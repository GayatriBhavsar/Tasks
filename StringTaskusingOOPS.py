import logging
logging.basicConfig(filename="str.log", level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

class stringgs:
    logging.info("we are acessing string class now")
    #creating method to extract the data from string

    def extract_data(self,str):
        self.str = str
        logging.info("we are in extract_data method")
        try:
            a = str[1:300:3]
            #logging.info("the extracted data is", a)
            return a
        except Exception as e:
            logging.error(e)

    #creating method reverse a string without using reverse function

    def string_reverse(self, s):
        self.s = s
        logging.info("we are in string_reverse method")
        try:
            a = s[::-1]
            return a
        except Exception as e:
            logging.exception(e)

    #creating method to split the string after convert it into upper case

    def Upper_split(self, m):
        self.m = m
        logging.info("we are in upper_split method")
        try:
            a = m.upper()
            a.split()
            return a
            #logging.info(a)
        except Exception as e:
            logging.exception(e)

    #creating a method to convert whole string in to lower case

    def Lower_case(self, s):
        self.s = s
        logging.info("we are in Lower_case method")
        try:
            a = s.lower()
            return a
        except Exception as e:
            logging.exception(e)

    #creating a method to capitaliza whole string

    def Cap_string(self, s):
        self.s = s
        logging.info("we are in the Cap_string method")
        try:
            a = s.capitalize()
            return a
        except Exception as e:
            logging.exception(e)

    #creating a method to check a string is alphanumeric and alphabetic

    def alnum_alpha(self, s):
        self.s = s
        l = []
        logging.info("we are in the alnum_alpha method")
        try:
            a = s.isalnum()
            l.append(a)
            a = s.isalpha()
            l.append(a)
            return l
        except Exception as e:
            logging.exception(e)

    #creating a method for example of expand tab

    def ex_expandtab(self,s):
        self.s = s
        logging.info("we are in ex_expandtab method")
        try:
            a = s.expandtabs()
            return a
        except Exception as e:
            logging.exception(e)

    #creating a method for strip , lstrip, rstrip

    def strip_string(self,s):
        self.s = s
        l = []
        logging.info("we are in strip_string method")
        try:
            a = s.strip()
            l.append(a)
            a = s.lstrip()
            l.append(a)
            a = s.rstrip()
            l.append(a)
            return l
        except Exception as e:
            logging.exception(e)

    #creating a method for replacing a charactor in string

    def replace_char(self,s,old_char,new_char):
        self.s = s
        self.old_char = old_char
        self.new_char = new_char
        logging.info("we are in the replace_char method")
        try:
            a = s.replace(old_char, new_char)
            return a
        except Exception as e:
            logging.exception(e)

    #creating a method to give example of center function of string

    def cen_string(self, s, size, char):
        self.s = s
        self.size = size
        self.char = char
        logging.info("we are cen_string method now")
        try:
            a = s.center(size, char)
            return a
        except Exception as e:
            logging.info(e)





l = stringgs()
str_var = stringgs()
r = "    iNeuron     "
cen_str = "iNeuron"
s = "I\tlove\tMumbai\tcity"
s1 = "this is My First Python programming class and _" \
     "i am learNING python string and its function"
logging.info(f"extracted data output _"
             f"is ,{str_var.extract_data(s1)}")
logging.info(f"output after reversing the string _"
             f"is, {str_var.string_reverse(s1)}")
logging.info(f"output after making string upper and then split _"
             f"is, {str_var.Upper_split(s1)}")
logging.info(f"output after converting string into lower case _"
             f"is, {str_var.Lower_case(s1)}")
logging.info(f"output after capitalize the whole string_"
             f"is, {str_var.Cap_string(s1)}")
logging.info(f"output for is string is alnumeric and is alphabetic _"
             f": {l.alnum_alpha(s1)}")
logging.info(f"example of expandtabs function is_"
             f":{str_var.ex_expandtab(s)}")
logging.info(f"output for strip function is:_"
             f"{l.strip_string(r)}")
logging.info(f"output for string replace function is_"
             f":,{str_var.replace_char(r,'N','W')}")
logging.info(f"output for string center function is_"
             f": {str_var.cen_string(cen_str,20,'*')} ")
