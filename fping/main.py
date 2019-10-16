# -*- coding: utf-8 -*-

import os
import multiprocessing
import subprocess


class FPing(object):
    """
    use run() method
    """


    def __ping(self, host, mp_queue): # TODO: set types of vars and result -> tuple ??
        """
        :param host: Host for ping
        :param mp_queue: Thread # TODO: realy??
        :return: Tuple (result, host's ip)
        """
        with open(os.devnull, 'w') as DNULL:
            response = subprocess.call(["ping", "-c", "2", "-w", '2', host], stdout=DNULL)
            if response == 0:
                result = True
            else:
                result = False
            mp_queue.put((result, host))

    def run(self, devices):
        """
        :param devices: list of ip address
        :return: two list with online and offline hosts
        """
        mp_queue = multiprocessing.Queue()
        processes = []
        for device in devices:
            p = multiprocessing.Process(target=self.__ping, args=(device, mp_queue))
            processes.append(p)
            p.start()
        for p in processes:
            p.join()
        results = {True: [], False: []}
        for p in processes:
            key, value = mp_queue.get()
            results[key] += [value]
        return results[True], results[False]


#if __name__ == "__main__":
#    fp = FPing()
#    hosts = input("Input list of ip: ['127.0.0.1', '127.0.0.2', '11.0.0.1'] # ")
#    result = fp.run(hosts)
#    print('Online: {}, Offline: {}'.format(result[0], result[1]))
