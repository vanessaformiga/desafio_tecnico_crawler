import requests
import json
from bs4 import BeautifulSoup
import re, os, json, traceback, sys, shutil
from time import sleep
from datetime import date, datetime

# realizando a criação da classe prinipal do projeto
class ConsultarProcessos():
    
    def criando_diretororio_busar_processos(self):
        diretorio_atual= os.getcwdb()
        self.diretorio_buscar_processos = 'diretorio_buscar_processos'

        # criação de uma pasta para guardar as informações obtidas 
        try:
            if not os.path.exists(self.diretorio_buscar_processos):
                os.makedirs(self.diretorio_buscar_processos)
        except:
            print("Erro ao criar o diretório do projeto")
            
    # fazer a alteração no json para fazer consultas
                
            
    def executar_buscar_processos(self):
        # salvar os dados do processo em um arquivo json
        with open('arquivos_de_consulta.json', 'r') as json_file:
            dados = json.load(json_file)
       
        # aessar os valores acerem consultados do arquivo json
        consultas = dados['valores_consulta']
        
        for consulta in consultas:
            lista_processos = consulta['numero_processo']
            for numero_processo in lista_processos:
                self.numero_processo = numero_processo
                print(f"Número do processo: {self.numero_processo}")
            self.cnpj = consulta['cnpj']
            print(f"CNPJ: {self.cnpj}")
            self.nome_da_parte = consulta['nome_da_parte']
            print(f"Número da parte: {self.nome_da_parte}")
            
        
        # executa a requisição 
        url = 'https://eproc.trf2.jus.br/eproc/externo_controlador.php?acao=processo_consulta_publica'

        
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            # realiza a requisão obtida
            response = requests.get(url,headers )
            if response.status_code == 200:
                print("A requisição ocorreu com sucesso")
                page_conteudo = response.content
                # apresenta o conteúdo da aplicação
                soup = BeautifulSoup(page_conteudo, 'html.parser')
                print(soup)
                
                # Inicializando extração da página
                tag_consulta = soup.find('h1')
                text_h1 = tag_consulta.get_text()

                print(text_h1)
                
                #captura os dados de nº processo
                
                texto_num_processo = soup.find(id="txtNumProcesso")
                
                input_num_processo = soup.find('input', {'id': 'txtNumProcesso'})

            
                input_num_processo['value'] = self.numero_processo
                print(input_num_processo)
                
                # captura os dados da parte interessada
                texto_parte_interessada = soup.find(id="txtStrParte")
                
                input_parte_interessada = soup.find('input', {'id': 'txtStrParte'})

            
                input_parte_interessada['value'] = self.nome_da_parte
                print(input_parte_interessada)
                
                print(self.nome_da_parte)
                
                
                tag_h1_consultar = soup.find('div', {'id': 'divInfraBarraComandosSuperior'})
                
                
                input_pessoa_juridica = soup.find('input', {'id': 'rdoPessoaJuridica'})
                
                print(input_pessoa_juridica)
                
                label_pessoa_juridica = soup.find('label', {'id': 'lblPessoaJuridica'})
                
                print(label_pessoa_juridica)
                
                label_cnpj = soup.find('label', {'id': 'lblCpfCnpj'})
                
                print(label_cnpj)
                
                input_cnpj = soup.find('input', {'id': 'txtCpfCnpj'})
                
                print(input_cnpj)
                
                print('aqui')
                
                input_cnpj['value'] = self.cnpj
                print(input_cnpj)
                
                print(self.cnpj)
                
                print('aqui')
                
            
                url_numero_processos = f'https://eproc.trf2.jus.br/eproc/externo_controlador.php?acao=processo_seleciona_publica&acao_origem=processo_consulta_publica&acao_retorno=processo_consulta_publica&num_processo={self.numero_processo}'
                print(url_numero_processos)
                
                headers = {"User-Agent": "Mozilla/5.0"}
                resp = requests.get(url_numero_processos, headers)
                if resp.status_code == 200:
                    print("A requisição ocorreu com sucesso")
                    page_conteudo = resp.content
                    print(page_conteudo)
                    #apresenta o conteúdo da aplicação
                    soup = BeautifulSoup(page_conteudo, 'html.parser')
                    print(soup)
                    
                    tag_consulta_pr = soup.find('h1')
                    text_h1 = tag_consulta_pr.get_text()

                    print(text_h1)
                    
                    tag_capa = soup.find('legend')
                    text_capa = tag_capa.get_text()

                    print(text_capa)
             
            # salvando os valores capturados e    
            save_file = {
                'Consulta do Processo':text_h1,
                'Capa do Processo':text_capa
            }       
            
            arquivo = os.path.join(self.diretorio_buscar_processos, 'buscar_processos.json')
            with open(arquivo, 'w') as f:
                json.dump(save_file, f, indent=4)

            print('salvar os arquivos')
     
             
                              
        except:
            print("Erro ao realizar a requisição")
            
            
    # salvar os arquivos em um banco de dados 
             

            
# realizando a instância da classe
if __name__ == '__main__':
    consulta_de_processos = ConsultarProcessos()
    consulta_de_processos.criando_diretororio_busar_processos()
    consulta_de_processos.executar_buscar_processos()