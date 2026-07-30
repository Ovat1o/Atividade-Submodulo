# Gerenciador de Tarefas - CLI 📝

Um aplicativo de linha de comando (CLI) desenvolvido em Python para o registro, priorização e ofuscação de tarefas. Este projeto foi criado como requisito prático de desenvolvimento, demonstrando a integração e o consumo de dependências externas através da arquitetura de submódulos do Git.

## 🚀 Funcionalidades

O sistema consome a biblioteca `Texto Magico Pro` como submódulo para realizar o processamento das strings fornecidas pelo usuário:

*   **Sistema de Alerta de Prioridade:** Utiliza o processamento de texto em caixa alta (*Uppercase Protocol*) nativo da biblioteca para destacar tarefas críticas, gerando alertas visuais no terminal.
*   **Ofuscação de Dados:** Implementa a reversão de caracteres (*Reverse String Technology*) para criar uma camada de ofuscação de dados, ocultando o conteúdo original da tarefa na interface para fins de privacidade.

## ⚙️ Pré-requisitos

*   Python 3.x
*   Git 

## 🔧 Instalação e Execução

**1. Clonagem do repositório** 

Para garantir que a biblioteca dependente seja baixada corretamente, é obrigatório clonar o repositório utilizando a flag de recursividade para os submódulos:

```bash
git clone --recurse-submodules <LINK_DESTE_REPOSITORIO>
```

*(Nota: Caso o repositório já tenha sido clonado sem a flag, execute `git submodule update --init` na raiz do projeto).*

**2. Acesso ao diretório**

```bash
cd app-tarefas-caoticas
```

**3. Execução do sistema**

```bash
python main.py
```

## 📖 Exemplo de Uso

```text
==================================================
   Gerenciador de Tarefas - CLI          
==================================================
Informe a tarefa pendente: Atualizar documentação da API

Processando entrada...

[PRIORIDADE ALTA] ATUALIZAR DOCUMENTAÇÃO DA API!!!
[DADO OFUSCADO] IPA ad oãçatnemucod razilautA

Operação concluída com sucesso.
```