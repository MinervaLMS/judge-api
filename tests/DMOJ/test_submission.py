from app.DMOJ.submission import Submission


def test_submission_creation():
    submission = Submission(
        id=1,
        submission_id="ABC123",
        problem_id="TEST",
        source="print('Hello, World!')",
        language="PY3",
        time_limit=2,
        memory_limit=256,
        meta={"key": "value"},
        short_circuit=False,
    )

    assert submission.id == 1
    assert submission.submission_id == "ABC123"
    assert submission.problem_id == "TEST"
    assert submission.source == "print('Hello, World!')"
    assert submission.language == "PY3"
    assert submission.time_limit == 2
    assert submission.memory_limit == 256
    assert submission.meta == {"key": "value"}
    assert not submission.short_circuit


def test_default_values():
    submission = Submission()

    assert submission.id is None
    assert submission.submission_id is None
    assert submission.problem_id is None
    assert submission.source is None
    assert submission.language is None
    assert submission.time_limit is None
    assert submission.memory_limit is None
    assert submission.meta == {}
    assert not submission.short_circuit
