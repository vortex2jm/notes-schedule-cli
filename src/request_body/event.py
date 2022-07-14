event_body = {
          'summary': 'Evento teste',
          'location': 'Jardim da Penha, Vitória',
          'description': 'Evento para testar a API',
          'start': {
            'dateTime': '2022-07-15T03:00:00-03:00',
            'timeZone': 'America/Sao_Paulo',
          },
          'end': {
            'dateTime': '2022-07-15T04:00:00-03:00',
            'timeZone': 'America/Sao_Paulo',
          },
          'attendees': [
            {'email': 'joao.clevelares@edu.ufes.br'}
          ],
          'reminders': {
            'useDefault': False,
            'overrides': [
              {'method': 'email', 'minutes': 24 * 60},
              {'method': 'popup', 'minutes': 10},
            ],
          },
        }