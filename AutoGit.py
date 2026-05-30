import subprocess
import sys
import os

class Color:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class GitAutomator:
    def __init__(self):
        self.check_git_repo()

    def check_git_repo(self):
        if not os.path.exists('.git'):
            print(f"{Color.YELLOW}[!] Alerta: Este diretório não é um repositório Git.{Color.END}")
            resp = input("Deseja inicializar um repositório Git aqui? (s/n): ").strip().lower()
            if resp == 's':
                print(self.executar_git("git init"))
                print(f"{Color.GREEN}[+] Repositório inicializado!{Color.END}")

    def executar_git(self, comando):
        try:
            resultado = subprocess.run(comando, shell=True, check=True, text=True, capture_output=True)
            return resultado.stdout
        except subprocess.CalledProcessError as erro:
            return f"\n{Color.RED}[!] Erro ao executar o comando:{Color.END}\n{erro.stderr}"

    def mostrar_estado(self, escopo):
        if escopo == "local":
            print(f"\n{Color.BLUE}{Color.BOLD}--- ESTADO ATUAL (REP. LOCAL) ---{Color.END}")
            print(self.executar_git("git status"))
        elif escopo == "remoto":
            print(f"\n{Color.BLUE}{Color.BOLD}--- ESTADO ATUAL (REP. REMOTO) ---{Color.END}")
            print(f"{Color.YELLOW}[*] Atualizando informações do GitHub (git fetch)...{Color.END}")
            self.executar_git("git fetch")
            print(self.executar_git("git status -uno"))

    def mostrar_historico(self, escopo):
        if escopo == "local":
            print(f"\n{Color.BLUE}{Color.BOLD}--- HISTÓRICO DE COMMITS (REP. LOCAL) ---{Color.END}")
            print(self.executar_git("git log --oneline -n 10"))
        elif escopo == "remoto":
            print(f"\n{Color.BLUE}{Color.BOLD}--- HISTÓRICO DE COMMITS (REP. REMOTO) ---{Color.END}")
            print(f"{Color.YELLOW}[*] Buscando histórico do branch remoto...{Color.END}")
            self.executar_git("git fetch")
            # Tenta pegar o branch atual para comparar
            branch = self.get_current_branch()
            print(self.executar_git(f"git log origin/{branch} --oneline -n 10"))

    def adicionar_arquivo(self):
        print(f"\n{Color.BLUE}{Color.BOLD}--- ADICIONAR ARQUIVOS ---{Color.END}")
        opcao = input("Digite '.'(ponto) para adicionar TODOS ou o nome do arquivo: ")
        print(self.executar_git(f"git add {opcao}"))
        print(f"{Color.GREEN}[+] Arquivo(s) adicionado(s) com sucesso!{Color.END}")

    def fazer_commit(self, escopo):
        print(f"\n{Color.BLUE}{Color.BOLD}--- FAZENDO COMMIT ---{Color.END}")
        mensagem = input("Digite a mensagem do commit: ")
        resultado_local = self.executar_git(f'git commit -m "{mensagem}"')
        print(resultado_local)
        if escopo == "remoto" or escopo == "github":
            print(f"\n{Color.YELLOW}[*] Enviando alterações para o GitHub (git push)...{Color.END}")
            print(self.executar_git("git push"))

    def fazer_pull(self):
        print(f"\n{Color.BLUE}{Color.BOLD}--- PUXANDO ALTERAÇÕES (GIT PULL) ---{Color.END}")
        print(self.executar_git("git pull"))

    def gerenciar_branches(self):
        while True:
            print(f"\n{Color.BLUE}{Color.BOLD}--- GERENCIAR BRANCHES ---{Color.END}")
            print("1. Listar Branches")
            print("2. Criar Nova Branch")
            print("3. Trocar de Branch (Checkout)")
            print("4. Voltar ao Menu Principal")
            
            escolha = input("\nEscolha uma opção: ")
            if escolha == "1":
                print(self.executar_git("git branch"))
            elif escolha == "2":
                nome = input("Digite o nome da nova branch: ")
                print(self.executar_git(f"git branch {nome}"))
            elif escolha == "3":
                nome = input("Digite o nome da branch para trocar: ")
                print(self.executar_git(f"git checkout {nome}"))
            elif escolha == "4":
                break

    def desfazer_alteracoes(self):
        print(f"\n{Color.RED}{Color.BOLD}--- DESFAZER ALTERAÇÕES ---{Color.END}")
        print("1. Desfazer add (git reset)")
        print("2. Descar de alterações no arquivo (git checkout -- arquivo)")
        print("3. Voltar")
        
        escolha = input("\nEscolha uma opção: ")
        if escolha == "1":
            print(self.executar_git("git reset"))
        elif escolha == "2":
            arquivo = input("Digite o nome do arquivo para descartar mudanças: ")
            print(self.executar_git(f"git checkout -- {arquivo}"))

    def get_current_branch(self):
        return self.executar_git("git rev-parse --abbrev-ref HEAD").strip()

    def menu_principal(self):
        while True:
            branch_atual = self.get_current_branch()
            print(f"\n{Color.GREEN}=========================================={Color.END}")
            print(f"         {Color.BOLD}AUTOMAÇÃO GIT & GITHUB{Color.END}            ")
            print(f"         Branch Atual: {Color.YELLOW}{branch_atual}{Color.END}")
            print(f"{Color.GREEN}=========================================={Color.END}")
            print("1. Adicionar Arquivos (git add)")
            print("2. Fazer Commit/Push")
            print("3. Ver Estado do Repositório (git status)")
            print("4. Ver Histórico de Commits (git log)")
            print("5. Puxar Alterações (git pull)")
            print("6. Gerenciar Branches")
            print("7. Desfazer Alterações")
            print("8. Sair")
            print(f"{Color.GREEN}=========================================={Color.END}")
            
            escolha = input("Escolha uma opção (1-8): ").strip()
            
            if escolha == "8":
                print(f"\n{Color.BLUE}Finalizando a automação. Até breve!{Color.END}")
                sys.exit()
            
            if escolha in ["1", "2", "3", "4"]:
                escopo = input("Deseja executar no repositório [local] ou [github]? ").strip().lower()
                if escopo not in ["local", "remoto", "github"]:
                    print(f"{Color.RED}[!] Opção de escopo inválida.{Color.END}")
                    continue
                
                if escolha == "1":
                    self.adicionar_arquivo()
                elif escolha == "2":
                    self.fazer_commit(escopo)
                elif escolha == "3":
                    self.mostrar_estado(escopo)
                elif escolha == "4":
                    self.mostrar_historico(escopo)
            
            elif escolha == "5":
                self.fazer_pull()
            elif escolha == "6":
                self.gerenciar_branches()
            elif escolha == "7":
                self.desfazer_alteracoes()
            elif escolha not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                print(f"{Color.RED}[!] Opção inválida!{Color.END}")

if __name__ == "__main__":
    app = GitAutomator()
    app.menu_principal()