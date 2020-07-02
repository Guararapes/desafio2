# Desafio Guararapes
Bem vindos ao desafio guararapes, nessa fase precisamos validar seus conhecimentos em nossa Stack, leia toda a documentação abaixo para realizar.

### Esqueletos
O candidato podem criar os serviços utilizando os esqueletos fornecidos, mas caso queiram criar projetos do zero podem ficar a vontade, todas as ferramentas citadas abaixo estão inclusas nos esqueletos. Não é preciso fazer um fork desse projeto, porém favor entregar um projeto fechado na [gitlab](http://gitlab.com) (para que outros candidatos não vizualizem a sua solução).

### Linguagens
* Java 11
* Javascript / NodeJS ECMA 6+
* [Typescript 3+](https://www.typescriptlang.org/)
* Python 3.8

### Frameworks
* [Spring boot](https://spring.io/projects/spring-boot)
* [Angular](https://angular.io/)
* [Django](https://www.djangoproject.com/)

### Libs 
* [Spring JPA](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#reference)
* [Spring Batch](https://docs.spring.io/spring-batch/docs/current-SNAPSHOT/reference/html/index.html)
* [Spring Web](https://spring.io/guides/gs/serving-web-content/)
* [Spring Fox](http://springfox.github.io/springfox/docs/current/)
* [Lombok](https://projectlombok.org/)
* [Liquid Base](https://www.liquibase.org/)
* [JPA H2 Database](https://www.h2database.com/html/main.html)
* [JPA Postgres Database](https://www.postgresql.org/)
* [drf-yasg](https://github.com/axnsan12/drf-yasg) - Swagger para Django
* [Angular Material](https://material.angular.io/) - Lib de estilização de interfaces

### Tools
* [Maven](https://maven.apache.org/)
* [Pipenv](https://github.com/pypa/pipenv) - Package manager para python

## Passo 1
Escolha a sua tecnologia, Java + Spring Boot ou Python + Django

## Passo 2
* Crie uma api restful que contenha um crud de materiais, cada material pode se relacionar com outros materiais, formando uma arvore, porém é importante de observar que os materiais da raiz (aqueles que não tem pais) são considerados produtos finais (camisas, calças, vestidos, etc) e os materiais "filhos" são sempre materias primas (tecido, linha, tinta, etc)
* Crie tambem um crud de criação de ordems de produção, que podem ser criadas a partir de um produto final caso todas as suas matérias primas possuam estoque

## Passo 3
Crie um frontend em SPA para listar os materiais considerados produtos finais (camisas, calças, vestidos, etc), nessa listagem deve haver um botão de liberar ordem de produção, porém esse botão só deve funcionar no caso em que o produto possua todas as suas matérias primas em estoque.

### Contexto
![deployment](out/uml/deployment/context.png)

### Componentes
![component](out/uml/component/components.png)

### Domínio
![classes](out/uml/code/code.png)

## Critérios de aceite
* Pode ser usado H2, Sqlite ou postgres
* Siga o modelo de hiperlink da api original
* Documente suas API's (pode ser OpenApi + Swagger)

## Bonus
Esses criterios não são obrigatorios porém são considerados bonus:
* Use swagger com spring fox (a documentação das apis podem ser via swagger)
* Use postgres
* Crie migrations com liquidbase
* Crie testes unitários ou de integração (sabe dizer a diferença?)
* Dockerize as aplicações
