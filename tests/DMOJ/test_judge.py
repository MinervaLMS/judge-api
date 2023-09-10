from app.DMOJ.submission import Submission
from app.DMOJ.judge import Judge


def test_judge_submit(judge_instance):
    submission = Submission(
        id=1,
        submission_id="ABC123",
        problem_id="TEST",
        source="print('Hello, World!')",
        language="PY3",
        time_limit=2,
        memory_limit=25996,
        meta={"key": "value"},
    )
    response = Judge.submit(submission, judge_instance)

    assert isinstance(response, list)
    assert len(response) > 0
