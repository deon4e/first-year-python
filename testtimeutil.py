# test time utiil script
# by Deon Fourie
# 29 March

"""
>>> import timeutil
>>> timeutil.validate("1151 p.m.")
False
>>> timeutil.validate("111:51 p.m.")
False
>>> timeutil.validate("01:51 p.m.")
False
>>> timeutil.validate("11:58 r.m.")
False
>>> timeutil.validate("11:511 p.m.")
False
>>> timeutil.validate("11:51 p.m.")
True

"""