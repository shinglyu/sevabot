#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys

def main(args):
    # rage magic word - 10% possibility
    if random.randint(1, 100) >= 90:
       print "不要像「小孩子要糖果」似的，什麼都喊要，而且越多越好。一下子得不到想要的也不要疑神疑鬼。"
       return 0

    # magic word
    if args.__len__() != 0:
       magic_word = args[random.randint(0, args.__len__() - 1)]   
    else:
       magic_word = ""

    if magic_word == "sf" or magic_word == "paris":
        print "巴 黎 有 華 貴 的 內 飾 ， 舊 金 山 有 海 景 ， 是 一 種 比 法；"
    elif magic_word == "tp" or magic_word == "bj":
        print "於 北 京 辦 公 室 比 ， 那 邊 既 沒 有 臺 北 辦 公 室 現 有 的 咖 啡 機 ， 也 沒 有 附 近 的 美 食 ， 更 沒 有 同 樣 質 量 的 空 氣 ， 又 是 另 一 種 比 法。"
    elif magic_word == "yearend":
        print "可 是 那 邊 沒 有 尾 牙 ， 沒 有 郊 遊 ， 是 另 一 種 比 法 。"
    elif magic_word == "news":
        print "總 是 有 「 這 類 」 記 者 。"
    elif magic_word == "court":
        print "是 否 最 好 請 最 高 法 院 到 場 見 證 ？"
    else:
        rand_list = ["公司不是盲流組織，不是mob rule。若是只有在mob rule環境下才能生存，若是認為上班就是搞民主運動，不僅政治上幼稚，工作上也幼稚。",
                     "同一家公司，不同地域，可比性不強。",
                     "誰也不會吃飽了撐的跑到信義計劃區辦「血汗工廠」。",
                     "好漢不提當年勇。",
                     "美 国 有 「 言 論 自 由 」 的 憲 法 ， 但 這 一 條 只 適 用 於 約 束 政 府 ， 不 可 以 拿 來 約 束 公 司 和 團 體 。",
                     "I think it is a wise decision to avoid a known controversial name for a conference room. It is simply not worth the hassle."]
        print rand_list[random.randint(0, rand_list.__len__() - 1)]

if __name__ == '__main__':
    main(sys.argv[1:])
