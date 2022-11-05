## Micropython & ESP 32

Este repositório registra os códigos desenvolvidos pela turma de **Sistemas Embarcados (SE) e Sistemas Ciber Físicos e Ubíquos (SCFU)** do [MEEC](https://pos.ucpel.edu.br/ppgeec/) da UCPel.

  * **[ajusta-relogio.py](https://github.com/adenauery/micropython/blob/main/ajusta-relogio.py)**: ajusta o relógio da ESP32 utilizando o NTP (Network Time Protocol)
  * **[publica-sensores-sleep.py](https://github.com/adenauery/micropython/blob/main/publica-sensores-sleep.py)**: publica leituras feitas por sensores (DHT 22, no caso) utilizando o protocolo MQTT (biblioteca sem suporte a senha) e intervalo de publicação por sleep (sem agendamento). O programa tem impressões em vários pontos, as quais quando em regime de produção, podem ser suprimidas.
