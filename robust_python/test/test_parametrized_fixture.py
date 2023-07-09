import pytest
from _pytest.fixtures import SubRequest


class JobManager:
    def __init__(self):
        pass

    def created_tasks(self) -> int:
        return 10


@pytest.fixture(scope="function")
def job_manager(mocker, request: SubRequest) -> JobManager:
    obj = JobManager()
    mocker.patch.object(obj, 'created_tasks', return_value=request.param)
    return obj


@pytest.fixture(scope="function")
def other_fixture() -> str:
    return "b"


@pytest.mark.parametrize("job_manager", [(5)], indirect=["job_manager"])
def test_indirect_fixture(job_manager, other_fixture):
    assert job_manager.created_tasks() == 5
    assert other_fixture == "b"

@pytest.mark.parametrize("job_manager", [(2)], indirect=["job_manager"])
def test_indirect_fixture_another_value(job_manager, other_fixture):
    assert job_manager.created_tasks() == 2
    assert other_fixture == "b"
