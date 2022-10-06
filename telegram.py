from email import message
from inspect import Parameter
from telethon.sync import TelegramClient, events;
import playsound, gtts;
from os import system;

apiId = 11150491;
apiHash = 'fd3eae5e278b2acd32d08c6c290b7a69';

sessionName = '/home/victormuller/PYTHON - Telegram/sessionName.session';
client = TelegramClient(sessionName, apiId, apiHash);
chat = 'me';

client.start();

@client.on(events.NewMessage(chats = chat))
async def event_handler(event):
    message = event.raw_text;

    print(message)

    parametros = message.split();
    parametrosNoCommand = message.replace(f'{parametros[0]} ', '');

    if(parametros[0] == 'tts'):

        tts = gtts.gTTS(parametrosNoCommand, lang = 'pt', tld = 'com.br')
        tts.save('/tmp/audioMensagem.mp3');
        playsound.playsound('/tmp/audioMensagem.mp3');
        system('rm /tmp/audioMensagem.mp3');


        #  tts = gtts.gTTS(parametrosNoCommand, lang = 'en', tld = 'com')

client.run_until_disconnected();