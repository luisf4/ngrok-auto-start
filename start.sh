#!/bin/bash

# Substitua <SEU_TOKEN> pelo token do seu bot no Discord
# Substitua <ID_DO_USUARIO> pelo ID do usuário que receberá a mensagem privada

# Iniciar ngrok na porta 8006
ngrok http 8006 &

# Esperar alguns segundos para a URL ser gerada
sleep 5


userid=''
tokenid=''

# Capturar a URL gerada pelo ngrok
ngrok_url=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')

# Enviar a URL via mensagem privada no Discord
curl -X POST -H "Authorization: Bot $tokenid" \
-H "User-Agent: BotDiscord (https://github.com/Gilbert7, 0.1)" \
-H "Content-Type: application/json" \
-d "{\"content\":\"ngrok URL: $ngrok_url\",\"tts\":false,\"embed\":[]}" \
https://discordapp.com/api/v6/users/$userid/channels

# Imprimir a URL para verificação
echo "ngrok URL: $ngrok_url"
