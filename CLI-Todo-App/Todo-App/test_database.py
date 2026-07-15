import os
import pytest
import database


@pytest.fixture(autouse=True)
def setup_database():
    """
    Fresh database before every test.
    """
    if os.path.exists("todo.db"):
        os.remove("todo.db")

    database.create_tables()

    yield

    if os.path.exists("todo.db"):
        os.remove("todo.db")


def test_create_user():
    user_id = database.create_user("Raghu")

    assert user_id == 1


def test_duplicate_user():
    database.create_user("Raghu")

    duplicate = database.create_user("Raghu")

    assert duplicate is None


def test_get_existing_user():
    user_id = database.create_user("Raghu")

    user = database.get_user("Raghu")

    assert user == (user_id, "Raghu")


def test_get_missing_user():
    user = database.get_user("Adam")

    assert user is None


def test_add_task():
    user_id = database.create_user("Raghu")

    task_id = database.add_task(user_id, "Learn Python")

    assert task_id == 1


def test_add_task_invalid_user():
    task_id = database.add_task(999, "Impossible Task")

    assert task_id is None


def test_get_tasks():
    user_id = database.create_user("Raghu")

    database.add_task(user_id, "Python")
    database.add_task(user_id, "SQL")

    tasks = database.get_tasks(user_id)

    assert len(tasks) == 2
    assert tasks[0][2] == "Python"
    assert tasks[1][2] == "SQL"


def test_get_tasks_empty():
    user_id = database.create_user("Raghu")

    tasks = database.get_tasks(user_id)

    assert tasks == []


def test_update_existing_task():
    user_id = database.create_user("Raghu")

    task_id = database.add_task(user_id, "Study")

    rows = database.update_task(task_id, 1)

    assert rows == 1

    task = database.get_tasks(user_id)[0]

    assert task[3] == 1


def test_update_missing_task():
    rows = database.update_task(999, 1)

    assert rows == 0


def test_delete_task():
    user_id = database.create_user("Raghu")

    task_id = database.add_task(user_id, "Study")

    rows = database.delete_task(task_id)

    assert rows == 1

    assert database.get_tasks(user_id) == []


def test_delete_missing_task():
    rows = database.delete_task(999)

    assert rows == 0


def test_delete_user():
    user_id = database.create_user("Raghu")

    rows = database.delete_user(user_id)

    assert rows == 1

    assert database.get_user("Raghu") is None


def test_delete_missing_user():
    rows = database.delete_user(999)

    assert rows == 0


def test_foreign_key_cascade():
    user_id = database.create_user("Raghu")

    database.add_task(user_id, "Task 1")
    database.add_task(user_id, "Task 2")

    database.delete_user(user_id)

    tasks = database.get_tasks(user_id)

    assert tasks == []


def test_multiple_users():
    raghu = database.create_user("Raghu")
    aditya = database.create_user("Aditya")

    database.add_task(raghu, "Python")
    database.add_task(aditya, "Gym")

    raghu_tasks = database.get_tasks(raghu)
    aditya_tasks = database.get_tasks(aditya)

    assert len(raghu_tasks) == 1
    assert len(aditya_tasks) == 1

    assert raghu_tasks[0][2] == "Python"
    assert aditya_tasks[0][2] == "Gym"