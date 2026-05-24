import subprocess
import sys 

def executar_git(comando):
    # função auxiliar para executar os comandos do Git no terminal e retornar o resultado ou o erro encontrado
    try:
        #Executa o comando e captura a saida de texto
        resultado = subprocess.run(comando, shell=True, check=True, text=True, capture_output=True)
        return resultado.stdout
    except subprocess.CalledProcessError as erro:
        #Retorna a mensagem de erro caso o Git falhe
        return f"\n[!] Erro ao executar o comando:\n{erro.stderr}"
def mostrar_estado(escopo):
    #Mostra o estado do repositório local ou do remoto(GitHub)
    if escopo == "local":
        print("\n---ESTADO ATUAL (REP.LOCAL)---")
        print(executar_git("git status"))
    elif escopo == "remoto":
        print("\n---ESTADO ATUAL (REP.REMOTO)---")
        print("[*] Atualizando informações do GitHub (git fetch)...")
        executar_git("git fetch")
        print(executar_git("git status -uno"))#Mostra uma comparação com o remoto
def mostrar_historico(escopo):
    #Mostra o historico do repositório local ou do remoto(GitHub)
    if escopo == "local":
        print("\n--- HISTORICO DE COMMITS (REP.LOCAL)---")
        print(executar_git("git log --oneline -n 10"))#Mostra os ultimos 10 commits
    elif escopo =="remoto":
        print("\n--- HISTORICO DE COMMITS (REP.REMOTO)---")
        print("[*] Buscando histórico do branch remoto...")
        executar_git("git fetch")#Tenta listar os commits do branch remoto padrão 
        print(executar_git("git log origin/main --oneline -n 10"))
def adicionar_arquivo():
    #Adicionar arquivos ao repositório
    print("\n--- ADICIONAR ARQUIVOS---")
    opcao = input("Digite '.'(ponto) para adicionar TODOS os arquivos ou o nome específico do arquivo:")
    print(executar_git(f"git add {opcao}"))
    print("[+] Arquivo(s) adicionado(s) com sucesso!")
def fazer_commit(escopo):
    #Realizando commit, primeiro commita localmente e oferece a opção de enviar para o remoto
    print("\n--- FAZENDO COMMIT---")
    mensagem = input("Digite a mensagem do cmmit:")
    resultado_local = executar_git(f'git commit -m"{mensagem}"')
    print(resultado_local)
    if escopo == "remoto":
        print("\n[*] Enviando alterações para o GitHub (git push)...")
        print(executar_git("git push"))
def menu_principal():
    #loop principal
    while True:
        print("\n==========================================")
        print("         AUTOMAÇÃO GIT & GITHUB            ")
        print("\n==========================================")
        print("1. Adicionar Arquivos (git add)")
        print("2. Fazer Commit (git commit)")
        print("3. Ver Estado do Repositório (git status)")
        print("4.Ver Histórico de Commits (git log)")
        print("5. Sair")
        print("\n==========================================")
        escolha = input("Escolha uma opção (1-5):")
        if escolha == "5":
            print("\n A terminar a automação. Até breve!")
            sys.exit()
        if escolha in ["1","2","3","4",]:
            escopo = input("Deseja executar a ação no repositório [local] ou no [github(remoto)]?").strip().lower()
            github = "remoto"
            if escopo not in ["local", "remoto","github"]:
                print("[!] Opção de escopo inválida. Volte ao menu e tente novamente")
                continue
            if escolha == "1":
                adicionar_arquivo()
            elif escolha == "2":
                fazer_commit(escopo)
            elif escolha == "3":
                mostrar_estado(escopo)
            elif escolha == "4":
                mostrar_historico(escopo)
    else:
        print("[!] Opção iválida! Por favor escolha um número de 1 a 5.")
if __name__== "__main__":
    menu_principal()