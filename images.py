import openai
import os
import requests
import json
import urllib.request
from PIL import Image

continuar = 1

openai.organization = "YOUR TOKEN HERE"
openai.api_key = "YOUR TOKEN HERE"


while continuar == 1:
    gerar = input('Insira a imagem cujo será gerada: \n')

    try:
        resposta_bruta = openai.Image.create(
          prompt=gerar, # o que vai ser gerado
          n=1, # imagens geradas
          size="1024x1024" # tamanho da imagem
        )

        #print(resposta_bruta)
        resposta = (resposta_bruta['data'][0])
        print(resposta['url'])

        url_img = resposta['url']

        with open("bancoContandor", encoding='utf-8') as meu_json:  #vai ler a contagem atual das imagens
            dados = json.load(meu_json)
        contagem = (dados['contador'])

        urllib.request.urlretrieve(url_img, f"C:/Users/Vinicius/Pictures/AI/imagem_gerada_{contagem}.png")
        img = Image.open(f"C:/Users/Vinicius/Pictures/AI/imagem_gerada_{contagem}.png")
        img.show()

        contagem = int(contagem) + 1  #vai aumentar a contagem das imagens

        atualizar_banco = {
            "contador": f"{contagem}",
        }
        json_object = json.dumps(atualizar_banco, indent=4)
        with open("bancoContandor", "w") as outfile:            #vai salvar a contagem das imagens
            outfile.write(json_object)

        continuar = 2
        print('Imagem gerada e arquivada com sucesso!')

    except:
        print('Um erro aconteceu.')
        print('Reiniciando o programa....')
        print('')
        continuar = 1






