"""
Created by HenryMa on 2020/9/3
"""

__author__ = 'HenryMa'


from builtins import *


def get_dict_from_singal():

    singal_dict = {'A': (0, 0.1), 'B': (0.1, 0.5), 'C': (0.5, 0.7), 'D': (0.7, 1)}
    return singal_dict


def encoder(singal, singal_dict):
    Low = 0
    High = 1
    for s in singal:
        CodeRange = High - Low
        High = Low + CodeRange * singal_dict[s][1]
        Low = Low + CodeRange * singal_dict[s][0]

    return Low


def decoder(encoded_number, singal_dict, singal_length):
    singal = []
    while singal_length:
        for k, v in singal_dict.items():
            if v[0] <= encoded_number < v[1]:
                singal.append(k)
                ranges = v[1] - v[0]
                encoded_number -= v[0]
                encoded_number /= ranges
                break
        singal_length -= 1
    return singal


def main():
    singal_dict = get_dict_from_singal()
    singal = 'CADACDBABDA'
    ans = encoder(singal, singal_dict)
    print(ans)
    singal_rec = decoder(ans, singal_dict, len(singal))
    print(singal_rec)


if __name__ == '__main__':
    main()
