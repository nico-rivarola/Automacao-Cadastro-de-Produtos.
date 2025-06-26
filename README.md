 ### Automação de Cadastro de Produtos Web
Este projeto demonstra a automação do processo de cadastro de produtos em um sistema web fictício, utilizando Python. O principal objetivo é otimizar tarefas repetitivas, inserindo dados de um arquivo CSV diretamente na interface do usuário de forma programática.

  # Objetivo
O objetivo central deste projeto é desenvolver uma solução de automação que seja capaz de:

Abrir um navegador web e navegar para uma URL específica de login.

Realizar o login no sistema com credenciais pré-definidas.

Ler e processar dados de produtos a partir de um arquivo CSV.

Inserir esses dados nos campos correspondentes de um formulário de cadastro de produtos na página web.

Simular interações do usuário (cliques, digitação, pressionar teclas) para navegar e submeter os formulários.

  # Funcionamento
O script Python opera de forma sequencial, simulando as ações de um usuário humano:

Abertura e Navegação: Inicia o navegador Google Chrome, digita a URL do sistema de cadastro e navega até a página de login.

Login Automatizado: Preenche os campos de e-mail e senha e clica no botão de login para acessar o sistema.

Leitura de Dados: Carrega os dados dos produtos de um arquivo produtos.csv para uma estrutura de dados (DataFrame).

Cadastro Iterativo: Para cada linha (produto) no arquivo CSV, o script executa os seguintes passos:

Clica no campo inicial do formulário de cadastro.

Preenche cada campo do formulário (código, marca, tipo, categoria, preço unitário, custo e observações) com os dados da linha atual do CSV.

Utiliza a tecla TAB para navegar entre os campos.

Pressiona ENTER para submeter o formulário de cadastro do produto.

Rola a página para garantir que os próximos campos de cadastro estejam visíveis, preparando para o próximo item.

  # Resultado
Ao final da execução, o script terá cadastrado todos os produtos listados no arquivo produtos.csv no sistema web, de forma rápida e autônoma, eliminando a necessidade de inserção manual e reduzindo erros. Isso demonstra o potencial da automação para agilizar processos e liberar o tempo do usuário para tarefas mais estratégicas.

 # Ferramentas Utilizadas
Python: Linguagem de programação principal.

pyautogui: Biblioteca Python utilizada para automação da interface gráfica (simulação de cliques do mouse, digitação de texto e pressionamento de teclas).

pandas: Biblioteca Python utilizada para manipulação e leitura de dados de arquivos CSV.

time: Módulo padrão do Python para introduzir pausas (esperas) no fluxo da automação, garantindo que os elementos da página web sejam carregados antes das interações.

Google Chrome: Navegador web utilizado como ambiente para a automação.
