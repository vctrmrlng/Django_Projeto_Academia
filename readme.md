Nomes dos Integrantes:
Caio Correa, João Cabrera, Lucas Miranda, Marlon Rosa, Ruimar Silvano, Victor Merling

Descrição do Projeto:
Inspirados pelo nosso Projeto Integrador, no qual desenvolvemos um site para a Academia Nova Corpore, e utilizando o modelo sugerido de Cursos e Alunos, decidimos ampliar o conceito original do projeto e incluir novas classes de objetos no sistema.
No Projeto Integrador, usando Javascript, criamos um formulário capaz de cadastrar um Aluno, mas, para atender os requisitos deste projeto aumentamos o numero de Classes para cinco. Dessa forma, o sistema passa a contar com as cinco classes finais: Aluno, Professor, Aula, Sala e Matricula.

Models Criados:
Aluno -> nome, cpf, altura, peso, data_nascimento, email
Professor -> nome, cpf, cref, data_nascimento, email
Sala -> nome
Aula -> nome, professor, sala
Matrícula -> aluno, aula

Explicando os Modelos:
- Aluno tem nome, cpf (único), altura (em centimetros, logo um decimal de 2 casas), peso (em quilos), data de nascimento, email (único)
- Professor tem nome, cpf (único), cref (é a identificação do profissional de educação física. é único), data de nascimento e email (único)
- Sala tem somente nome. Foi criado para que pudessem ser selecionado o local de uma aula usando um menu dropdown
- Aula tem nome, professor (chave estrangeira que representa quem dá a aula) e sala (chave estrangeira que representa o local em que a aula ocorre)
- Matricula - Segundo o que aprendemos na aula de Banco de Dados, quando há uma relação Many-to-many entre duas tabelas, é necessario criar uma tabela relacional. Sendo assim, essa tabela tem duas chaves estrangeiras associando um aluno e a aula em que ele está matriculado 

Todos os modelos tem um método __str__ que retorna o nome da instancia, com exceção de Matricula que retorna o nome do aluno e o nome da aula. Ex: Marcelo - Alongamento

Tecnologias Criadas:
O projeto foi feito usando Django

Instruções para rodar:
O projeto ainda é incompleto, mas para rodar é simples:
1 - Certifique-se que tem Python e Django instalados 
2 - Crie uma pasta e clone o repositorio dentro dessa pasta com o comando 
    git clone https://github.com/vctrmrlng/Django_Projeto_Academia
3 - Dentro desta pasta há uma pasta chamada _______________________. Entre na pasta
4 - Use o comando
    python manage.py runserver
5 - Clique no link que aparece ou abra seu browser e vá até o endereço http://127.0.0.1:8000/admin
6 - Use o login e senha root : root


Algumas dúvidas a sanar antes do entregar o projeto:
1 - A descrição da avaliação tem o seguinte texto:

3.3 Relacionamento entre Models
Exemplo:

Um autor pode ter vários livros
Um professor pode ter vários cursos
Um cliente pode ter vários pedidos
Isso deve aparecer na listagem.

Mas eu não sei o que ele quer dizer com listagem. Precisa explicar qual é a relação entre as classes ou só precisa ter relação. Vale a pena incluir uma modelagem daquela que o Bob ensinou a fazer? Aquela que fazia no site.

2 - Os prints das telas do Portal ADM tem que ser incluidas no readme? Não sei como por fotos no readme.
Será que pode enviar os prints pelo moodle separadamente?
