#developer: vk: @chimburdev && tg: @chimburdev
#group tg: @mgmsoftware

from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait

stop = False
client = Client('session', '15179171', 'c8c90d2964a788d4827aac026acf6913')
client.start()
client.stop()
print('\nБот успешно запустился!\Разработчик: vk: @chimburdev && tg: @chimburdev\nНаша телеграмм группа: @mgmsoftware')

@client.on_message(filters.command(['спам', 'spam'], prefixes=['.','!','/', '-']) & filters.me)
def message_handler(client, message):
    global stop
    args = message.text.split(' ')
    #if !args[1]:
        #client.send_message(message.chat.id, 'Используйте: /spam <кол-во сообщений> <сообщение>')
    if args[1] == 'стоп':
        stop = True
        client.edit_message_text(message.chat.id, message.id, 'Вы успешно отключили спам!')
    i = int(args[1])
    args.pop(0)
    args.pop(0)
    while i >= 0:
        try:
            if(stop == True):
                break
                i = 0
                stop = False
            client.send_message(message.chat.id, ' '.join(args))
            sleep(1/15)
        except FloodWait as e:
            sleep(e.x)
        i -= 1

@client.on_message(filters.command(['love', 'hearts'], prefixes=['.','!','/', '-']) & filters.me)
def message_handler(client, message):
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💖💖🤍💖💖🤍🤍\n🤍💖💖💖💖💖💖💖🤍\n🤍💖💖💖💖💖💖💖🤍\n🤍💖💖💖💖💖💖💖🤍\n🤍🤍💖💖💖💖💖🤍🤍\n🤍🤍🤍💖💖💖🤍🤍🤍\n🤍🤍🤍🤍💖🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💌💌🤍💌💌🤍🤍\n🤍💌💌💌💌💌💌💌🤍\n🤍💌💌💌💌💌💌💌🤍\n🤍💌💌💌💌💌💌💌🤍\n🤍🤍💌💌💌💌💌🤍🤍\n🤍🤍🤍💌💌💌🤍🤍🤍\n🤍🤍🤍🤍💌🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    client.edit_message_text(message.chat.id, message.id, '🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️❤️\n❤️❤️❤️❤️\n❤️❤️❤️❤️\n❤️❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️❤️\n❤️❤️❤️\n❤️❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️❤️\n❤️❤️')
    sleep(1/2)
    client.edit_message_text(message.chat.id, message.id, '❤️')

client.run()