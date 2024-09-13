hs, ms, ss = map(int, input().split(':'))
hf, mf, sf = map(int, input().split(':'))

gap_second = (3600*(hf-hs) + 60*(mf-ms) + (sf-ss)) % 86400 or 86400
gap_second, s = divmod(gap_second, 60)
h, m = divmod(gap_second, 60)

print(f'{h:02}:{m:02}:{s:02}')