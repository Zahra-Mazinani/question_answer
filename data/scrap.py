# in the name of Allah

## Refrences : https://github.com/ergoncugler/web-scraping-telegram/tree/main
from __init__ import *

# scraping
async with TelegramClient(username, api_id, api_hash) as client:
    async for message in client.iter_messages(channel, search=key_search):
        if message.date < datetime(y_max, m_max, d_max, tzinfo=timezone.utc) and message.date > datetime(y_min, m_min, d_min, tzinfo=timezone.utc):

            # if there is media
            if message.media:
                url = f'https://t.me/{channel}/{message.id}'.replace('@', '')
            else:
                url = 'no media'

            # if there are reactions
            emoji_string=''
            if message.reactions == None:
                pass
            else:
                for reaction_count in message.reactions.results:
                    emoji = reaction_count.reaction.emoticon
                    count = str(reaction_count.count)
                    emoji_string += emoji + " " + count + " "

            # content condensation
            conteudo = [f'#ID{index:05}', channel, message.sender_id, message.text, message.date.strftime('%Y-%m-%d %H:%M:%S'), message.id, message.post_author, message.views, emoji_string, message.forwards, url]

            # if there are comments # important to come after the content list with append following it, so as not to confuse the 'message' and collect only the contents of the comments
            comments = []
            try:
                async for message in client.iter_messages(channel, reply_to=message.id):
                    comments.append(message.text)
            except:
                comments = ['possible adjustment']
            comments = ', '.join(comments).replace(', ', ';\n')

            # append of the content with the comments
            conteudo.append(comments)
            conteudo = tuple(conteudo)
            
            dataset.insertMultipleRecords(con=con,recordList=[conteudo])

            # updates the progress counter
            print(f'Item {index:05} completed!')
            print(f'Id: {message.id:05}.\n')

            # update loop parameters
            index = index + 1
            time.sleep(1)

# end
print(f'----------------------------------------\n#Concluded! #{index-1:05} posts were scraped!\n----------------------------------------\n\n\n\n')