# Simple Calendar API

Criação de API em Python para organização de eventos em um calendário. Projeto criado para estudo da linguagem Python e framework Fast API

## Endpoints

| Method   | Urls               | Description                           |
| :------- | :----------------- | :------------------------------------ |
| `POST`   | /events            | Criar de eventos no calendário        |
| `GET`    | /events            | Buscar todos os eventos no calendário |
| `GET`    | /events/{event_id} | Buscar evento por ID no calendário    |
| `PUT`    | /events/{event_id} | Atualizar dados do evento por ID      |
| `DELETE` | /events/{event_id} | Deletar evento por ID                 |
