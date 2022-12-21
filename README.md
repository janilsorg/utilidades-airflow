# Instalação básica do Airflow usando docker

## Abra um terminal ou Prompt de comando e clone o repositório
```
git clone https://github.com/janilsorg/utilidades-airflow

<p>Ou faça o download do repositório via interface</p>

## Execute o comando
```
docker-compose up
```

<p>Verifique se já existe a pasta dags na pasta raíz. Essa pasta é necessária para o mapeamento das dags do airflow</p>

## Utilidades docker

### Para lista os containers execute
```
docker ps
```

### Para executar comando bash no modo interativo execute
```
docker exec -it - airflow-tut_webserver_1 bash
```
<p>Esse comando fará você logar no ambiente docker onde está instalado o AirFlow e assim listar os arquivos de configurações ou até modifica-los.</p>

### Para acessar a interface, basta navegar até o endereço
```
http://localhost:8080
```
