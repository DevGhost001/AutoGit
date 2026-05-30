# AutoGit

AutoGit é uma ferramenta simples e poderosa escrita em Python para automatizar os comandos mais comuns do Git e GitHub através de uma interface de linha de comando (CLI) intuitiva.

## 🚀 Funcionalidades

- **Gerenciamento de Arquivos**: Adicione arquivos específicos ou todos de uma vez (`git add`).
- **Commits Simplificados**: Realize commits com mensagens personalizadas e envie para o repositório remoto em um único fluxo.
- **Visualização de Estado**: Verifique o `git status` do seu repositório local ou compare com o remoto.
- **Histórico de Commits**: Visualize os últimos commits de forma organizada.
- **Suporte Multi-repositório**: Alterne entre ações locais e remotas (GitHub) facilmente.

## 🛠️ Instalação

Certifique-se de ter o Python 3 e o Git instalados em sua máquina.

1. Clone o repositório:
   ```bash
   git clone https://github.com/DevGhost001/AutoGit.git
   cd AutoGit
   ```

2. Execute o script:
   ```bash
   python3 AutoGit.py
   ```

## 📖 Como Usar

Ao executar o script, você verá um menu interativo:

1. **Adicionar Arquivos**: Escolha entre adicionar tudo (`.`) ou um arquivo específico.
2. **Fazer Commit**: Digite sua mensagem de commit. Se escolher o escopo "github(remoto)", ele fará o push automaticamente.
3. **Ver Estado**: Mostra o status atual dos arquivos.
4. **Ver Histórico**: Lista os últimos 10 commits.
5. **Sair**: Encerra a ferramenta.

## 🏗️ Melhorias Futuras

- Suporte a criação e troca de branches.
- Comando `git pull` integrado.
- Melhor tratamento de erros e interface colorida.
- Inicialização automática de repositórios (`git init`).

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
