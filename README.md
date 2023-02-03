# check-200

<h1>Checando Dominios</h1>
</br>

O programa acima faz um check nos dominios validando se estão up , a diferença é que ele aceita dominios sem https ou http incluindo para validar.
A saida dos hosts validos por padrao pega o nome do dominio e cria um arquivo na pasta se preferir pode passar -o para o nome que quiser, e -t e quantidade de threds, por padrao ele roda em 100 threds.
</br>
</br>
<h2>Exemplo de uso<h2>
200 lista-hosts.txt
</br>
Padrão = 200 <(subfinder -d exemplo.com)
Com Threds setados = 200 -t 50 <(subfinder -d exemplo.com)
