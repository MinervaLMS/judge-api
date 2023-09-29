from app.DMOJ.submission import Submission


def test_submission_creation():
    submission = Submission(
        id=1,
        submission_id="ABC123",
        problem_id="TEST",
        time_limit=1,
        memory_limit=9999,
        source="print('Hello, World!')",
        language="py3",
    )

    assert submission.id == 1
    assert submission.submission_id == "ABC123"
    assert submission.problem_id == "TEST"
    assert submission.source == "print('Hello, World!')"
    assert submission.language == "py3"
    assert submission.time_limit == 1
    assert submission.memory_limit == 9999


def test_default_values():
    submission = Submission()

    assert submission.id is None
    assert submission.submission_id is None
    assert submission.problem_id is None
    assert submission.source is None
    assert submission.language is None
    assert submission.time_limit is None
    assert submission.memory_limit is None