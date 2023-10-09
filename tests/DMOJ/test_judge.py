from app.DMOJ.submission import Submission
from app.DMOJ.judge import Judge


def test_judge_submit(app,client,judge_instance):
    with app.app_context():
        client.post(
            "/problem",
            json=(
                {
                    "input": ["1"],
                    "output": ["Hello, World!"],
                    "problem_id": "TEST1",
                    "points": [18]
                }
            ),
        )
    submission = Submission(
        id=1,
        submission_id="ABC123",
        problem_id="TEST1",
        time_limit=1,
        memory_limit=9999,
        source="print('Hello, World!')",
        language="PY3",

    )
    response = Judge.submit(submission, judge_instance)
    assert isinstance(response, list)
    assert len(response) > 0