# Projeto Final de Graduação

## Para compilar o projeto:

### Servidor

Entre na pasta _server_ em um terminal e digite:

```sh
dnc . -v
```

### Distribuidor

Entre na pasta _distributor_ em um terminal e digite:

```sh
dnc . -v
```


### Cliente

Entre na pasta _client_ em um terminal e digite:

```sh
dnc . -v
```

## Para executar o servidor:

Entre na pasta __server__ em um terminal e digite:

```sh
dana main.o
```


## Para executar o distribuidor (local e remote):

Abra três terminais na pasta _distributor_. No primeiro execute:

```sh
dana -sp "../server;../readn" Distributor.o
```

Em um segundo terminal digite:

```sh
dana -sp ../readn RemoteDist.o
```

Em um terceiro terminal digite:

```sh
dana -sp ../readn RemoteDist.o 8082 2011
```

A primeira composição do servidor que o Distribuidor monta é a versão local. Para distribuí-lo, digite help e escolhar qual opção de distribuir. Para tornar o servidor todo local novamente, digite local.

## Para executar os testes:

A ferramenta utilizada para os testes de performance foi o [Locust](https://locust.io/).

Recomenda-se utilizar Python >= 3.6 e um virtual environment, instalando os requirements com:

```sh
pip install -r locust/requirements.txt
```

Lembrando que para executar os testes é preciso que o _Distribuidor_ esteja executando.

### Testes com interface:

Para executar os testes com a interface do Locust, abra um terminal (com o virtual env ativado) na pasta _locust_ e execute:

```sh
locust <cliente>
```

no qual `<cliente>` deve ser substituído pelo nome da classe de um dos cliente implementados em _locustfile.py_ (`Client_90_10`, `Client_70_30`, `Client_50_50`, `Client_30_70`, `Client_10_90`).

Em seguida, basta acessar http://0.0.0.0:8089 para ter acesso a interface, e configurar os parâmetros para o teste:

- **Number of users:** número máximo de users que o teste irá atingir em pico de carga.
- **Spawn rate:** número de usuários ativados por segundo (até que número máximo seja atingido).
- **Host:** endpoint base no qual os users irão fazer as requisições (configurado por padrão no código).

### Testes sem interface:

Para executar os testes sem a interface do Locust, abra um terminal (com o virtual env ativado) na pasta _locust_ e execute:

```sh
python run_test.py <cliente>
```

O script _run\_test.py_ irá executar o _locustfile.py_ com o cliente passado, e utilizando os parâmetros mencionados anteriormente (pré-definidos no código). Alguns outros parâmetros também são definidos, como o tempo de execução, e a coleta de estatísticas (alguns arquivos _.csv_ serão gerados).
