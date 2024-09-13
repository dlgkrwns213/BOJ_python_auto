hs, ms, ss = map(int, input().split(':'))
hf, mf, sf = map(int, input().split(':'))

gap_second = (3600*(hf-hs) + 60*(mf-ms) + (sf-ss)) % 86400 or 86400
gap_second, s = divmod(gap_second, 60)
h, m = divmod(gap_second, 60)

print(':'.join(map(lambda x: f'0{x}'[-2:], (h, m, s))))