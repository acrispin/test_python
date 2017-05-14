"""
https://dev.to/mistermocha/python-unit-testing-with-mock---part-one
https://mail.python.org/pipermail/tutor/2014-January/099629.html
"""

from subprocess import Popen, PIPE

class Proc2(object):
    def ping_host(self, host_to_ping):
        cmd_string = 'ping %s' % (host_to_ping)
        cmd_args = cmd_string.split()
        proc = Popen(cmd_args, shell=True)
        proc.wait()
        if proc.returncode != 0:
            raise Exception('Error code was: %d' % (proc.returncode))
            # print('Error code was: %d' % (proc.returncode))
        else:
            print('OK....')

    def ping_host2(self, host_to_ping):
        cmd_string = 'ping %s' % (host_to_ping)
        cmd_args = cmd_string.split()
        proc = Popen(cmd_args, shell=False)
        proc.wait()
        for line in proc.stdout.readlines():
            print(line)
        if proc.returncode != 0:
            raise Exception('Error code was: %d' % (proc.returncode))
            # print('Error code was: %d' % (proc.returncode))
        else:
            print('OK....')

    def count_the_shells(self):
        p = Popen(['ps', '-ax'], stdout=PIPE, stderr=PIPE)
        if p.wait():
            raise Exception('We had a fail')
        count = 0
        for proc in p.stdout.readlines():
            # http://stackoverflow.com/questions/33054527/python-3-5-typeerror-a-bytes-like-object-is-required-not-str-when-writing-t
            # http://stackoverflow.com/questions/17615414/how-to-convert-binary-string-to-normal-string-in-python3
            if b"bash" in proc: # en python3.5 y python2.7 se tenie que usar binary string: b"bash"
            # if "bash" in proc: # solo funciona en python2.7
                print(type(proc))
                print(type(proc) is bytes, type(proc) is str)
                print(proc)
                count += 1
        return count

if __name__ == '__main__':
    proc = Proc2()
    print(proc.count_the_shells())
    proc.ping_host('localhost')
