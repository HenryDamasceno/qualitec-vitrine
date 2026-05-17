# 📘 Cartilha de Uso, Manutenção e Estrutura Técnica
**Projeto:** Vitrine Digital - Qualitec Montagens e Serviços Industriais LTDA
**Autor:** Henry Padilha Damasceno

---

## 1. Apresentação
Esta cartilha foi desenvolvida para documentar a estrutura técnica e o funcionamento da nova Vitrine Digital da Qualitec. O objetivo deste manual é servir como um guia rápido para que futuros desenvolvedores ou a própria equipe técnica da empresa saibam como instalar, modificar e manter o site no ar de forma independente.

---

## 2. Visão Geral da Arquitetura
Diferente de sites tradicionais (que usam pastas separadas para HTML, CSS e JavaScript), este projeto foi construído utilizando uma abordagem moderna focada em **Python**:
*   **Reflex Framework:** Toda a interface, botões e lógicas foram escritos 100% em Python. O Reflex se encarrega de traduzir (compilar) esse código para uma aplicação web moderna (React) nos bastidores.
*   **Hospedagem (Cloud):** O site é hospedado nos servidores gratuitos da Reflex Cloud.
*   **Domínio Customizado:** O domínio oficial (`qualitec.online`) é gerenciado pela Hostinger, utilizando regras de DNS para apontar para a nuvem do Reflex.

---

## 3. Preparando o Ambiente de Trabalho
Para fazer qualquer alteração no site, é necessário rodá-lo localmente no seu computador primeiro.

### Pré-requisitos:
1. Ter o **Python** (versão 3.10 ou superior) instalado no computador.
2. Ter o **Git** instalado para baixar o código.
3. Um editor de código (recomendamos o **Visual Studio Code**).

### Passo a Passo para Iniciar:
1. Abra o Terminal e baixe o projeto:
   ```bash
   git clone https://github.com/HenryDamasceno/qualitec-vitrine.git
   ```
2. Entre na pasta do projeto:
   ```bash
   cd qualitec-vitrine
   ```
3. Ative o "Ambiente Virtual" (ele isola o projeto do resto do seu PC):
   ```bash
   # No Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   ```
4. Ligue o servidor local:
   ```bash
   reflex run
   ```
   *Pronto! O site abrirá no seu navegador no endereço `http://localhost:3000`.*

---

## 4. Entendendo os Arquivos do Projeto
Ao abrir a pasta `qualitec_vitrine` no seu editor, você verá vários arquivos. Os únicos com os quais você precisa se preocupar são:

*   📂 `assets/` -> **É aqui que ficam as imagens.** Todas as fotos, logos e o ícone da aba (favicon.ico) devem ser jogados dentro desta pasta.
*   📂 `qualitec_vitrine/`
    *   📄 `qualitec_vitrine.py` -> **O coração do site.** É aqui que todo o código escrito em Python vive. Textos, cores e componentes estão todos dentro deste arquivo.
*   📄 `requirements.txt` -> Lista das bibliotecas que o Python precisa baixar para o site funcionar.

---

## 5. Como Alterar Textos e Imagens
O desenvolvimento no Reflex possui "Hot-Reload". Isso significa que qualquer mudança que você salvar no arquivo reflete instantaneamente no navegador.

### Como mudar um texto:
1. Abra o arquivo `qualitec_vitrine/qualitec_vitrine.py`.
2. Procure pela seção desejada (exemplo: `def about_section():`).
3. Encontre o texto atual entre aspas duplas `"..."` e reescreva o que desejar.
4. Salve o arquivo (`Ctrl + S`).

### Como trocar uma imagem:
1. Coloque a nova imagem dentro da pasta `assets/` (exemplo: `nova_foto.jpg`).
2. Abra o arquivo `qualitec_vitrine.py` e procure onde a imagem antiga está sendo usada (procure por `rx.image(src="/...")`).
3. Altere o nome do arquivo no código: `src="/nova_foto.jpg"`.
4. Salve o arquivo.

---

## 6. Publicando Alterações na Internet (Deploy)
Sempre que você fizer mudanças nos textos ou imagens e quiser que seus clientes vejam a nova versão, você precisa enviar isso para a nuvem.

1. No terminal do VS Code, certifique-se de que o ambiente virtual está ativo `(venv)`.
2. Pare o servidor local apertando `Ctrl + C`.
3. Digite o comando de publicação:
   ```bash
   reflex deploy
   ```
4. Se for a primeira vez, ele pedirá para você fazer login no navegador. Caso o terminal pergunte se você deseja prosseguir (mesmo com avisos de *requirements*), basta digitar `y` e apertar Enter.
5. Aguarde o processo terminar. A nuvem do Reflex atualizará o site automaticamente!

---

## 7. Gerenciamento do Domínio
O endereço `qualitec.online` é propriedade da Qualitec e foi registrado na **Hostinger**.
*   **Onde renovar:** O pagamento anual do domínio deve ser feito no painel da Hostinger.
*   **Como funciona:** Na aba "Gerenciar DNS" da Hostinger, foram criados apontamentos específicos (registros `CNAME` e `A`) que redirecionam quem digita `qualitec.online` diretamente para os servidores do Reflex onde o código está hospedado.
*   **Atenção:** Nunca apague os registros `_acme-challenge` ou `_cf-custom-hostname` da Hostinger, pois eles são os responsáveis por manter o "cadeado verde" (SSL / Site Seguro) ativado.

---
> *Documentação elaborada como parte de atividade prática de Extensão Universitária em Desenvolvimento de Software.*
