<img src="docs/assets/logo.png" alt="drawing" height="100"/> 

## 1. GERAL
### 1.1. RESUMO
Fazer o resumo do que o processo automação se refere


### 1.2. DETALHES

#### 1.2.1 Quais são as entradas do processo

#### 1.2.2 Quais são as saídas do processo

#### 1.2.3 Como o processo é realizado


### 1.3. TRATATIVAS
Descrever quais os pontos fracos ou riscos conhecidos


## 2. INFORMAÇÕES
### 2.1. PROCESSO
- **Tipo**: <_demanda-fluid  / agendado / demanda-serviço>
    - <u>Solicitante/Executante</u>: <_área que requisitou a automação_> / <_área que executa processo em caso de problemas_>
- **Tempo de execução**: <_quanto tempo demora para que o processo seja executado. Exemplo: 2min40_>
- **Prioridade de execução**: <_de 0 a 10>
- **Usuário(s) Impessoal Utilizado(s)**: <_nome_usuário_impessoal_>
- **Assinatura:** <Sim / Não>
- **Relatório:**
    - <u>Gera</u>: <Sim / Não>
    - <u>Usa</u>: <Sim / Não>
- **Fluid:**
    - <u>Uso de Processo</u>: <Sim / Não>
        - <u>Nome do processo</u>: <_nome do processo> #TODO - se você for abrir um processo no fluid, qual o nome dele?
    - <u>Afetado por campo:</u> <Sim / Não> <_escrever os CAMPOS que são utilizados>
- **Serviços:**
    - <u>Uso do *Dique*</u>: <Sim / Não>
        - <u>Rotas</u>: </formulario/preencher/...> #TODO - retirar caso não seja utilizado o Dique
    - <u>Uso do *Pilar*</u>: <Sim / Não>
        - <u>Rotas</u>: </processo/armazenar/...> #TODO - retirar caso não seja utilizado o Pilar
    - <u>Uso do *API CAS*</u>: <Sim / Não>
        - <u>Rotas</u>: </bureau/get/...> #TODO - retirar caso não seja utilizada a API CAS
    - <u>Uso do *ZapZap*</u>: <Sim / Não>
        - <u>Rotas</u>: </zapzap/.../...> #TODO - retirar caso não seja utilizado o ZapZap


### 2.2. INSTALAÇÃO
- **Ambiente virtual**: 
    - <u>Linux</u>: `python3 -m venv .venv`  #TODO - retirar caso não seja executado em Linux
    - <u>Windows</u>: `python -m venv .venv`
- **Código**:
    - Pelo pyproject:
        - <u>Produção</u>: `pip install .`
        - <u>Desenvolvimento</u>: `pip install .["dev"]` ou `pip install .["test,dev"]` se envolver testes
    - Pelo requirements:
        - <u>Produção</u>: `pip install -r requirements.txt`


### 2.3. GERAIS
- **Desenvolvedor inicial**: <_seu nome_> 
    - <u>Desenvolvedor suporte</u>: <_nome_> 
- **Responsável pelo mapeamento do processo**: <_quem da área de processos realizou o mapeamento_>
- **Número do Processo de Solicitação - Fluid**: < 123456> # o número do processo onde tem a solicitação para essa automação
- **Uso de porta**: <Sim / Não> (8080 | 9000)
- **Cód. SeSuite**: < 123456>
- **Cód. Checklist CAS**: < RPA0000>
- **Checklist TODO**: [Checklist TODO](TODO.md)
