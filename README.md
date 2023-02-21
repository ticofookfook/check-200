# check-200

<h1>Checando Dominios</h1>
</br>

O programa acima faz um check nos dominios validando se estão up , a diferença é que ele aceita dominios sem https ou http incluindo para validar.
A saida dos hosts validos por padrao pega o nome do dominio e cria um arquivo na pasta se preferir pode passar -o para o nome que quiser, e -t é quantidade de threds, por padrão ele roda em 100 threds.
</br>
</br>
<h2>Exemplo de uso</h2>
200 lista-hosts.txt
</br>
Padrão = python3 validate-200.py  <(subfinder -d exemplo.com)
</br>
Com Threds setados = python3 validate-200.py -t 50 <(subfinder -d exemplo.com)
