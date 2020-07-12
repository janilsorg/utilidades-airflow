# Instalação básica do Airflow usando docker

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
