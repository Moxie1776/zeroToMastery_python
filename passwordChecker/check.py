import hashlib
import sys

import requests

pw = 'password123'


def checkPasswordAgainstApi(password):
  sha1Password = hashlib.sha1(password.encode()).hexdigest().upper()
  first5_char, tail = sha1Password[:5], sha1Password[5:]
  # print(first5_char, tail)
  return requestApiData(first5_char, tail)


def getPasswordLeaksCount(hashes, hashToCheck):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, c in hashes:
    if h == hashToCheck:
      return c
  return 0


def requestApiData(query_chars, hashToCheck):
  url = f'https://api.pwnedpasswords.com/range/{query_chars}'
  res = requests.get(url)
  # if no valid results
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}')

  return getPasswordLeaksCount(res, hashToCheck)


def main(args):
  for password in args:
    used = checkPasswordAgainstApi(password)
    print(f'{password} has been used {used} times')
  return 'done...'


if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
