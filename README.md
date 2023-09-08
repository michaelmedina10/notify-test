# notify-test

o objetivo desse repositorio é construir uma API na qual me permita ser noificado quando alguma alteração for realizada em um repositório do github

Para configurar o WebHook do github ou do Gitlab, preciso configurar um endpoint, caso esteja desenvolvendo o projeto localmente, podemos usar o
servidor ngrok, no qual funciona como um proxy reverso, um servidor web que gerencia outros servidores web.

Para instalar no macbook o ngrok, basta executar o comando: <br>
`brew install ngrok`

Uma vez instalado, execute sua aplicação, por exemplo fastapi executa na porta 8000 com uvicorn.<br>
Agora execute o ngrok na porta 8000, com o seguinte comando:<br>
`ngrok http 8000`
