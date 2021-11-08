import os
import sys
import time

os.system("clear")


print("""
█████╗ ██╗   ██╗████████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
███████║██║   ██║   ██║   ██║   ██║██╔████╔██║███████║   ██║   ██║██║   ██║██╔██╗ ██║
██╔══██║██║   ██║   ██║   ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║ ╚═╝ ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                     
                                                            ##################################################
                                                            #   - Feito Por Destroyer                        #
                                                            #   - Fiz só pra ficar bonito e dar meus crédito #
                                                            ##################################################
""")

time.sleep(3)

def build_Dockerfile():
    opr=input("Fez a build do Dockerfile? (Y/N): ")
    if opr == "Y":
        print("Okay!")
        caminho=input("Aonde está o Arquivo Dockerfile? (Digite a pasta ex: /home/home): ")
        tag=input("Digite o nome que você quer colocar (Ex: Webserver:1.0): ")
        os.system("docker build -t {} -f {} ".format(tag, caminho))
        print("Imagem Construida")
        time.sleep(2)
        os.system("docker images")
    else:
        print("Criando dockerfile...")
        time.sleep(3)
        os.system("touch Dockerfile")
        os.system("vi Dockerfile")
        tag=input("Digite o nome que você quer colocar e a versão: ")
        os.system("docker build -t {} .".format(tag))
        print("Imagem Construida!")
build_Dockerfile()

while True:
    cnt=input("Deseja criar mais Dockerfile? (Y/N): ")
    if cnt == "Y, y":
        name=input("Digite o nome para o arquivo: ")
        os.system("touch {}.Dockerfile".format(name))
        continued=input("Deseja Editar o {}.Dockerfile? (Y/N)".format(name))
        if continued == "Y, y":
            nome_arquivo=input("Qual é o nome do arquivo?: ")
            os.system("vi {}.Dockerfile")
        else:
            break
    else:
        break
