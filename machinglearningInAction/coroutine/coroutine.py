import time

# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         time.sleep(1)
#         r = '200 OK'
#
# def produce(c):
#     c.next()
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()

"""consumer"""
def womanLove():
    love = ''
    while True:
        receive = yield love
        if not receive:
            return
        print 'i %s  you  ,too! handsome gentle  man' %receive
        time.sleep(1)
        r = 200
"""producer"""
def manLove(c):
    c.next()
    n = 0
    while n<10:
        n = n+1
        print ('I love you, beauty girl ')
        r = c.send('love')
        print 'So we can get together to create new life'
    c.close()


if __name__=='__main__':
    c = womanLove()
    manLove(c)