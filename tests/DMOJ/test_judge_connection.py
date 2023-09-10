from app.DMOJ.judge_connection import SingletonJudge, LocalPacketManager, LocalJudge


def test_local_packet_manager():
    judge = LocalJudge()
    LocalPacketManager(judge)


def test_local_judge():
    judge = LocalJudge()

    assert isinstance(judge, LocalJudge)
    assert isinstance(judge.graded_submissions, list)


def test_singleton_judge():
    judge1 = SingletonJudge()
    judge2 = SingletonJudge()

    assert isinstance(judge1.response, list)
    assert isinstance(judge1.judge, LocalJudge)
    assert judge1 is judge2
