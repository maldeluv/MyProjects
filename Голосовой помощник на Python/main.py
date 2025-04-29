import speech_recognition as sp
import sys
import webbrowser
import pyttsx3 as pyt

#def talk(words):
    #print(words)
    #engine = pyt.init()
    #engine.say(words)
    #engine.runAndWait()

#talk('скажи что-то')

commands_Dict = { 'commands':{
    'opensite': ['открыть сайт',"включи сайт","запусти сайт","сайт","на домашнюю страницу"],
    'hello': ['привет','здравствуй','здрасте','приветствую','добрый день','доброе утро','добрый вечер',"доброго дня"],
    'stop': ['стоп','хватит','завершить','завершить программу','завершить работу','остановить программу']
}

}

def command():
    r = sp.Recognizer()

    with sp.Microphone() as sourse:
        print('Говорите')
        engine = pyt.init()
        engine.say('Говорите')
        engine.runAndWait()
        r.pause_threshold = 0,5
        r.adjust_for_ambient_noise(sourse, duration=0.5)
        audio = r.listen(sourse)

    try:
        task = r.recognize_google(audio, language='ru-RU').lower()
        #print('Вы сказали ' + task)
        #a = 'Вы сказали '+ task
        #engine = pyt.init()
        #engine.say(a)
        #engine.runAndWait()
    except sp.UnknownValueError:
        print('Повторите')
        engine = pyt.init()
        engine.say('Повторите пожалуйста')
        engine.runAndWait()
        task = command()
    return task

def opensite():
    print('Будет сделано')
    engine = pyt.init()
    engine.say('Будет сделано')
    engine.runAndWait()
    url = 'https://www.mozilla.org/ru/firefox/central/'
    webbrowser.open(url)

def hello():
    print('Здравствуйте')
    engine = pyt.init()
    engine.say('Здравствуйте')
    engine.runAndWait()

def stop():
    print('До свидания')
    engine = pyt.init()
    engine.say('До свидания')
    engine.runAndWait()
    sys.exit()

def main():
    task = command()
    for k, v in commands_Dict['commands'].items():
        if task in v:
            print(k)

#while True:
    #something(command())





