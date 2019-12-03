# In obedience to the truth

# uva: 10191

import collections


Appointment = collections.namedtuple('Appointment', ['begin', 'end', 'duration'])


def ctime(time):
    """Return number of minutes to time, ellapsed since 00:00."""
    h, m = map(int, time.split(':'))
    return h * 60 + m

def time(ctime):
    h = ctime // 60
    m = ctime % 60
    return '{}:{:0>2}'.format(h,m)

def makeAppointment(begin, end):
    b, e = ctime(begin), ctime(end)
    return Appointment(b, e, e-b)

def duration(ctime):
    h = ctime // 60
    m = ctime % 60
    if h > 0:
        duration = '{} hours and {} minutes'.format(h, m)
    else:
        duration = '{} minutes'.format(m)
    return duration

day = 0

while True:
    try:
        n_lines = int(input())
        day += 1
        appointments = set()
    except EOFError:
        break
    for _ in range(n_lines):
        l = input()
        begin, end, *_ = [s.strip() for s in l.split()]
        appointments.add(makeAppointment(begin, end))

    appointments = list(sorted(appointments, key=lambda a: a.end))

    tenam = ctime('10:00')
    max_nap = (tenam, appointments[0].begin-tenam)

    for i, a in enumerate(appointments[1:], 1):
        naptime = (a.begin-appointments[i-1].end)
        if naptime > max_nap[1]:
            max_nap = (appointments[i-1].end, naptime)

    sixpm = ctime('18:00')
    if sixpm-appointments[-1].end > max_nap[1]:
        max_nap = (appointments[-1].end, sixpm-appointments[-1].end)

    start_time = time(max_nap[0])

    print('Day #{}: the longest nap starts at {} and will last for {}.'.format(
        day, start_time, duration(max_nap[1]))
        )
