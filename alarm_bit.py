# -*- coding: utf-8 -*-
# wrote on 2018/1/29


def hex2dec(string_num):
    return int(string_num.upper(), 16)


def check_alarm_state(alarm_state):
    """
    车辆是否报警
    :param alarm_state: 报警字段,长度为8字符串，例如00010001
    :return: 是否紧急报警（是True否False），是否超速报警，是否疲劳报警
    """
    jj_mask, cs_mask, pl_mask = 1, 1 << 16, 1 << 17  # 紧急报警, 超速报警, 疲劳报警
    i_state = hex2dec(alarm_state)
    is_jj, is_cs, is_pl = i_state & jj_mask, i_state & cs_mask, i_state & pl_mask
    return is_jj is not 0, is_cs is not 0, is_pl is not 0


t0, t1, t2 = check_alarm_state("00010001")
print t0, t1, t2
