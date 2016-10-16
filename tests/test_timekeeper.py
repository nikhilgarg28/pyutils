import time
from pyutils import timekeeper


def test():
    tk = timekeeper.TimeKeeper()

    @tk.time('f1')
    def f1():
        time.sleep(1)
        return

    @tk.time('f2')
    def f2():
        time.sleep(2)
        return

    f1()
    f2()
    f2()

    profile = tk.profile()

    # first verify that profile has data for both f1/f2 and nothing else
    assert 'f1' in profile
    assert 'f2' in profile
    assert 2 == len(profile)

    assert profile['f1'] >= 1
    assert profile['f2'] >= 2 * 2

