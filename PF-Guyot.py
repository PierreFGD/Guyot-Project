# -*- coding: utf-8 -*-
import os 
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import requests as req
import difflib
from urllib.parse import unquote
import re
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
"""
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
os.chdir(__location__)

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}

class Voltaire3000():
    def __init__(self,email = "email",password = "password"): 
        self.email = email
        self.__password = password
        self.connexion_voltaire(email,password)
        self.niveau()
        self.bot()

    def connexion_voltaire(self,email,password):
        """
        method connexion_voltaire; is use to connect to the voltaire application.
            arguments : email       [str] email of the user 
                        password    [str] password of the user
            return : NO RETURN
        """
        self.browser = webdriver.Chrome(desired_capabilities=caps)
        self.browser.get('https://www.projet-voltaire.fr/voltaire/com.woonoz.gwt.woonoz.Voltaire/Voltaire.html?returnUrl=www.projet-voltaire.fr/choix-parcours/&applicationCode=pv')
        time.sleep(1)
        id_user = self.browser.find_element_by_id("user_pseudonym")
        id_user.send_keys(email)                                                                                                                 
        mdp = self.browser.find_element_by_xpath("/html/body/div[4]/div[2]/form[1]/div/div/div/input[2]")
        mdp.send_keys(password)                                                                                                          
        connect_button = self.browser.find_element_by_xpath("/html/body/div[4]/div[2]/form[1]/div/div/div/button")
        connect_button.click()
        time.sleep(5)
    
    def niveau(self):
        """
        method niveau; is use to click on the available voltaire level.
            arguments : NO ARGUMENT
            return :    NO RETURN
        """
        for i in range(4,100):
            try:
                niveau = self.browser.find_element_by_xpath("/html/body/div[5]/div[3]/div[3]/div/div[2]/div["+ str(i) +"]/div/div[2]/div[3]/button[1]")
                niveau.click()
                print("AAAAAAA",i)
                break
            except:
                try:
                    niveau = self.browser.find_element_by_xpath("/html/body/div[5]/div[3]/div[3]/div[1]/div[2]/div[13]/div/div[2]/div[2]/button")
                    niveau.click()
                    print("BBBBB")
                    break
                except:
                    pass
                try:
                    niveau = self.browser.find_element_by_xpath("/html/body/div[5]/div[3]/div[3]/div/div[2]/div[11]/div/div[2]/div[2]/button")
                    niveau.click()
                    print("CCCCCCCC")
                    break
                except:
                    pass
        time.sleep(4)
                 
                    
                

    def bot(self):
        """
        method bot, is use to resolve the voltaire level, this method will get the responses and after that resolve each sentences.
            arguments : NO ARGUMENT
            return :    NO RETURN
        """
        reponses = self.data_network_spoiler()
        while True:
            try:
                try:
                    self.avoid_pop_up()
                except Exception as e:
                    print(e)
                    pass
                phrase = self.get_phrase()
                reponse = self.verif(phrase,reponses)
                print("Reponse: ",reponse)
                self.click_voltaire(reponse)
                time.sleep(50)
            except:
                self.reload()
  
    def click_voltaire(self,reponse):
        """
        method click_voltaire, is use to click and the right location or enter the right word to resolve the sentence.
            arguments : reponse     [str] reponse of the sentence
            return :    RETURN NOTHING
        """
        if self.type_question =="click":
            if reponse != "No_Error":
                reponse_liste = re.compile("(\W)",re.UNICODE).split(reponse)
                reponse_liste = remove_values_list(reponse_liste,'')
                mots = dict()
                i = 1
                while True :
                    try:
                        mots[i] = self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/span["+str(i)+"]")
                        i+=1
                    except Exception as e :
                        print(e)
                        break
                phrase_liste = []
                for i in range(1,len(mots)+1):
                    phrase_liste.append(mots[i].text)
                for i in range(0,len(phrase_liste)):
                    if phrase_liste[i] == "":
                        phrase_liste[i] = " "
                print(reponse_liste,"\n",phrase_liste)
                for j in range(0,len(phrase_liste)):
                    print("|",phrase_liste[j],"|",reponse_liste[j],"|")
                    if phrase_liste[j] != reponse_liste[j] and not ((phrase_liste[j].isspace() or phrase_liste[j] == "") and (reponse_liste[j].isspace() or reponse_liste[j] == "")):
                        mot_faux = self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/span["+str(j+1)+"]")
                        print("CLICK",mot_faux.text)
                        mot_faux.click()
                        time.sleep(2)
                        suivant_button = self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div/div[3]/div[2]/button")
                        suivant_button.click()
                        return()
            else:
                try: 
                    no_error_button = self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/button")
                    no_error_button.click()
                    time.sleep(2)
                    suivant_button = self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div/div[3]/div[2]/button")
                    suivant_button.click()
                    return()
                except:
                    no_error_button = self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/button[2]")
                    no_error_button.click()
                    time.sleep(2)
                    suivant_button = self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div/div[3]/div[2]/button")
                    suivant_button.click()
                    return()

        elif reponse != "No_Error":
            try:
                self.input_voltaire.send_keys(reponse)
                time.sleep(1)
                validation_button = self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div/div[2]/div[1]/div[2]/button")
                validation_button.click()
                time.sleep(1)
                time.sleep(2)
                suivant_button = self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div/div[3]/div[2]/button") 
                suivant_button.click()
                return()

            except Exception as e:
                print(e)
                pass
        else:
            self.reload()
            return()

        
    def reload(self):
        """
        method reload, is use to relaunch the program
            arguments : NO ARGUMENT
            return :    NO RETURN
        """
        self.browser.quit()
        self.connexion_voltaire(self.email,self.__password)
        self.niveau()
        self.bot()
        print("Reload Sucess !")

    def get_phrase(self):
        """
        method get_phrase, is use to get the sentence and the type (click sentence or input sentence)
            arguments : NO ARGUMENT
            return :    phrase  [str], the voltaire sentence
        """
        time.sleep(5)
        i = 1
        mots = dict()
        while True :
            try:
                mots[i] = self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/span["+str(i)+"]")
                i+=1
            except Exception as e :
                print(e)
                break
        try:
            self.input_voltaire = self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/input")
            self.type_question = "input"
        except:
            self.type_question = "click"

        phrase = ''
        for j in range(1,len(mots)+1):
            if mots[j].text != "":
                phrase += (mots[j].text)
            else:
                phrase += " "
        i = 0
        print(phrase)
        return(phrase)
        

    def data_network_spoiler(self):
        """
        method data_network_spoiler, is use to spoil the response data from voltaire network.
            arguments : NO ARGUMENT
            return : reponses   [list] list of voltaire correct sentences
        """
        browser_log = self.browser.get_log('performance') 
        events = [self.process_browser_log_entry(entry) for entry in browser_log]
        events = [event for event in events if 'Network.response' in event['method']]
        all_data = []
        for j in events:
            if "https://www.projet-voltaire.fr/services-pjv/gwt/WolLearningContentWebService" in str(j):    
                try : 
                    (print(str(j["params"]["response"]["url"])+"\n"))
                    all_data.append(self.browser.execute_cdp_cmd('Network.getResponseBody', {'requestId': j["params"]["requestId"]}))
                except Exception as e:
                    print("ERREUR CHARGEMENT",e)
                    pass
        max_data = all_data[0]         
        for data in all_data:
            if len(str(max_data)) < len(str(data)):
                max_data = data
        max_data = str(max_data)
        reponses = max_data.split('"')
        reponses = [x for x in reponses if "\\x3CB" in x]
        for i in range(0,len(reponses)):
            if "a)" in reponses[i]:
                print(reponses[i])
                a = re.search('a(.*?)b\)',reponses[i]).group(1)
                b = reponses[i].replace("a" + a,'')
                b = b.replace(")",'',1)
                b = b.replace("b",'',1)
                a = a.replace(")",'',1)
                a = translate_bytes_utf_8(a)
                b = translate_bytes_utf_8(b)
                print("a: ",a)
                print("b: ",b)
                print("\n")
                reponses.append(a)
                reponses.append(b)
            
            print(reponses[i])
            
        return(reponses)

    def process_browser_log_entry(self,entry):
        """
        method process_browser_log_entry, is use to load browser log entry.
            arguments : NO ARGUMENT
            return : reponses   [dict] dict of all informations about this entry
        """
        response = json.loads(entry['message'])['message']
        return(response)

    def verif(self,phrase,data):
        """
        method verif, is use to compare the voltaire sentence with our correct sentences list to get the right answser.
            arguments : phrase      [str] voltaire sentence
                        data        [list] list of voltaire correct sentences
            return :    result      [str] result, "No_error", the right sentence or the word to input.
        """
        if self.type_question == "click":
            possibilites = difflib.get_close_matches(phrase, data,n = 1,cutoff = 0.6)
            if len(possibilites) != 0:
                text_correction = (unquote(possibilites[0].replace("\\x", "%"))).replace('\\','')
                text_correction = text_correction.replace("<B>",'')
                text_correction = text_correction.replace("</B>",'')
                try:
                    text_correction = bytes(text_correction,"latin-1").decode("latin-1")
                except:
                    text_correction = translate_bytes_utf_8(text_correction)
                if text_correction[0] == ' ':
                    text_correction = text_correction.replace(' ','',1)
            else:
                text_correction = "No_Error"
            return(text_correction)
        else:
            possibilites = difflib.get_close_matches(phrase, data,n = 1,cutoff = 0.6)
            if len(possibilites) != 0:
                correction = (unquote(possibilites[0].replace("\\x", "%"))).replace('\\','')
                result = re.search('>(.*?)<', correction).group(1)
                try: 
                    result = bytes(result,"latin-1").decode("latin-1")
                except:
                    result = translate_bytes_utf_8(result)
            else:
                print("ERRO DATA NOT FOUND,\n Program is reloading...")
                self.reload()
            return(result)
    def avoid_pop_up(self):
        time.sleep(5)
        compris = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div/div[5]/button[1]")
        compris.click()
        time.sleep(2)

        rep1 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/div/div[1]/div/button[2]")
        rep2 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/div/div[2]/div/button[2]")
        rep3 = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/div/div[3]/div/button[2]")

        rep1.click()
        rep2.click()
        rep3.click()

        time.sleep(2)

        try:
            abandon = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div/div[5]/button[3]")
            abandon.click()
        except:
            sortir = self.browser.find_element_by_xpath("/html/body/div[7]/div/div/div/div[5]/button[3]")
            sortir.click()


def translate_bytes_utf_8(text):
    """
    function translate_bytes_utf_8, is use if the latin decode doesn't work, it will replace code to real letter and sign.
        arguments : text      [str] the text to translate
        return :    result    [str] the text translated
    """
    text = text.replace("\\",'')
    text = text.replace("xA0"," ")
    text = text.replace("&#x2011;","-")
    text = text.replace("x26#x2011;","‑")
    text = text.replace("x27","'")
    text = text.replace("x3C/Bx3E",'')
    text = text.replace("x3CBx3E",'')
    text = text.replace("x3Cbr/x3E",'')
    text = text.replace("-","‑")
    return(text)

def remove_values_list(liste, val):
    """
    function remoce_value_list, is use to remove a specific value from list
        arguments : liste   [list] the list wich you want to remove a value
                    val     [str] the value
        return :    [value for value in liste if value != val]      [list] the list without this value
    """
    return [value for value in liste if value != val]

if __name__ == "__main__": 

    f = open("config.txt",'r')                              # Open the config
    config = f.read().split('\n')                           
    email =  re.search('>(.*?)<', config[0]).group(1)       # Find email
    password =  re.search('>(.*?)<', config[1]).group(1)    # Find password
    f.close()
    voltaire = Voltaire3000(email=email,password=password)  # Call Voltaire3000






