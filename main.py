# colocar em inglês

import requests
import json
from bs4 import BeautifulSoup
import re, os, json, traceback, sys, shutil
from time import sleep
from datetime import date, datetime

# creating the project's main class
class ConsultProcess():
    
    def create_diretory_search_process(self):
        diretory_actual= os.getcwdb()
        self.diretory_search_process = 'diretory_search_process'

        # create directory of project 
        try:
            if not os.path.exists(self.diretory_search_process):
                os.makedirs(self.diretory_search_process)
        except:
            print("Error the create directory ")
        
        #the json to make queries
        
                
    # function that extracts the values           
    def execute_search_process(self):
        # save the values in file json
        with open('arquivos_de_consulta.json', 'r') as file_json:
            archive = json.load(file_json)
            
        # variables used to capture site values
        consults = archive['valores_consulta']
        
        for consult in consults:
            list_processes = consult['numero_processo']
            for number_processes in list_processes:
                self.number_process = number_processes
                print(f"Número do processo: {self.number_process}")
            self.cnpj = consult['cnpj']
            print(f"CNPJ: {self.cnpj}")
            self.name_part = consult['nome_da_parte']
            print(f"Número da Parte Interessada: {self.name_part}")
            
        
        # url for in use in requests
        url = 'https://eproc.trf2.jus.br/eproc/externo_controlador.php?acao=processo_consulta_publica'

        # making the arrangements for making the request to the site
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            # exibir header of page
            response = requests.get(url,headers )
            if response.status_code == 200:
                print("The request was successful")
                page_conteud = response.content
                soup = BeautifulSoup(page_conteud, 'html.parser')
                print(soup)
                
                # Initializing page extraction
                consult_tag = soup.find('h1')
                text_h1 = consult_tag.get_text()

                print(text_h1)
                
                # captures process number data
                
                text_number_process = soup.find(id="txtNumProcesso")
                
                input_number_process = soup.find('input', {'id': 'txtNumProcesso'})

            
                input_number_process['value'] = self.number_process
                print(input_number_process)
                
                
                # captures process interested party
                text_interested_party = soup.find(id="txtStrParte")
                
                input_interested_party = soup.find('input', {'id': 'txtStrParte'})

            
                input_interested_party['value'] = self.name_part
                print(input_interested_party)
                
                print(self.name_part)
                
                tag_h1_consult = soup.find('div', {'id': 'divInfraBarraComandosSuperior'})
                
                # captures person legal
                
                input_person_legal = soup.find('input', {'id': 'rdoPessoaJuridica'})
                
                print(input_person_legal)
                
                label_person_legal = soup.find('label', {'id': 'lblPessoaJuridica'})
                
                print(label_person_legal)
                
                # captures cnpj
                
                label_cnpj = soup.find('label', {'id': 'lblCpfCnpj'})
                
                print(label_cnpj)
                
                input_cnpj = soup.find('input', {'id': 'txtCpfCnpj'})
                
                print(input_cnpj)
                
                input_cnpj['value'] = self.cnpj
                print(input_cnpj)
                
                print(self.cnpj)
                
                url_number_process = f'https://eproc.trf2.jus.br/eproc/externo_controlador.php?acao=processo_seleciona_publica&acao_origem=processo_consulta_publica&acao_retorno=processo_consulta_publica&num_processo={self.number_process}'
                print(url_number_process)
                
                headers = {"User-Agent": "Mozilla/5.0"}
                resp = requests.get(url_number_process, headers)
                if resp.status_code == 200:
                    print("The request was successful")
                    page_context = resp.content
                    print(page_context)
                    # presents the content of the application
                    soup = BeautifulSoup(page_context, 'html.parser')
                    print(soup)
                    
                    tag_consult_pr = soup.find('h1')
                    text_h1 = tag_consult_pr.get_text()

                    print(text_h1)
                    
                    tag_cover = soup.find('legend')
                    text_cover = tag_cover.get_text()

                    print(text_cover)
                    
                    # extrair name number process
                    
                    label_number_process = soup.find('label', {'id': 'lblNumProcesso'})
                    label_text_number_process = label_number_process.get_text(strip=True)

                    print(label_text_number_process)
                    
                    span_text_number_process = soup.find('span', {'id': 'txtNumProcesso'})
                    span_text_number_process = span_text_number_process.get_text(strip=True)

                    print(span_text_number_process)
                    
                    # extrair situation process
                    
                    label_situation = soup.find('label', {'id': 'lblSituacao'})
                    label_text_situation = label_situation.get_text(strip=True)

                    print(label_text_situation)
                    
                    span_situation = soup.find('span', {'id': 'txtSituacao'})
                    span_text_situation = span_situation.get_text(strip=True)

                    print(span_text_situation)
                    
                    # get in interested party
                    
                    text_legend_interested_party = soup.find('fieldset', {'id': 'fldPartes'})
                    text_legend_interested_parts =  text_legend_interested_party.get_text(strip=True)

                    print(text_legend_interested_parts)
                    
                    # get in event
                    
                    event_parts = soup.find('table', {'class': 'infraTable'})
                    text_event_parts =  event_parts.get_text(strip=True)

                    print(text_event_parts)
                    
                    
                    # saving the captured values and placing them in the dictionary
                    save_file = {
                        'Consulta':text_h1,
                        'Capa do Processo':text_cover,
                        label_text_number_process:span_text_number_process,
                        label_text_situation:span_text_situation,
                        'Partes e Representantes':text_legend_interested_parts
                        
                        
                    }   
                    
                    print(save_file)    
                    
                    
                    file = os.path.join(self.diretory_search_process, 'buscar_processos.json')
                    with open(file, 'w', encoding='utf-8') as f:
                        json.dump(save_file, f, indent=4)

                    print('files of save')
        
                
                                
        except:
            print("Error in requisition")
            
                
    # save files in database
    # def saveDadosBD(self):
    #     pass
             
# realizing the class instance
if __name__ == '__main__':
    consut_processes = ConsultProcess()
    consut_processes.create_diretory_search_process()
    consut_processes.execute_search_process()