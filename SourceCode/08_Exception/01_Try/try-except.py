# try-except

# [POINT 1]
try:
    1 / 0
except Exception as e:
    print('Alarm:  ' + str(e))
else:
    print('Safe')
finally:
    print('Finish')
