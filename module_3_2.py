def send_gmail(message, recipient, *, sender='university.help@gmail.com'):
    if '@' not in recipient or not recipient.endswith(
            ('.com', '.ru', '.net')) or '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
        print('Невозможно отправить письмо с адреса', recipient, 'на адрес', sender)
    elif sender == recipient:
        print('нельзя отправить письмо самому себе')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправленно с адреса', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправленно с', sender, 'на адрес', recipient)


send_gmail('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_gmail('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_gmail('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_gmail('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
