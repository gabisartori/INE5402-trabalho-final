# INE5402-trabalho-final
 Atividade final de matéria de Introdução à Programação Orientada a Objetos

 A atividade consiste em implementar diversas classes aplicando os conceitos vistos eu aula

 Modelo implementado: Uma plataforma que mantem controle de publicações e usuários
 As publicações podem ser uma das 2 formas a seguir:
 - Publicação de texto
 - Publicação de imagem

 Todos os tipos de publicação herdam as propriedades de uma publicação genérica

 Os usuários serão um classe simples, contendo informações de perfil como nome de usuário além de uma lista relacionando seus posts por ordem de publicação.

 O programa inicia numa tela de boas-vindas, perguntando se o usuário deseja realizar login, cadastrar uma nova conta ou encerrar o programa

 No menu de cadastro, são requisitadas as informações do novo perfil e é instanciado um novo objeto da classe User.

 No menu de login, são requisitados o nome e a senha de um possível usuário. Caso esse usuário exista e a senha esteja correta, é exibida a tela de do usuário, caso contrário, o programa retorna para a tela de boas-vindas.

 Uma vez que existem usuários cadastrados, também é possível realizar login como usuário de admin, que possui funcionalidades específicas como remoção de usuários.

 Após logado, o usuário será apresentado com funcionalidades padrões de uma rede social, como criar e visualizar publicações, além de visitar perfis existentes e comentar em outras publicações.