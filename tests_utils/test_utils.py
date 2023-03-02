from funktions import utils


def test_load_json():
    assert type(utils.load_json()) == list
    assert len((utils.load_json())) > 0


def test_state_executed():
    assert isinstance(utils.state_executed(), list)
    assert utils.state_executed() is not None


def test_sort_by_date():
    assert isinstance(utils.sort_by_date(), list)
    assert utils.state_executed() != utils.sort_by_date()


def test_last_five():
    assert isinstance(utils.last_five()[:5], list)
    assert len(utils.last_five()[:5]) == 5


def test_disguise_card():
    for i in utils.last_five()[:5]:
        assert isinstance(i, dict)

    last_five_transactions = utils.last_five()[:5]
    assert isinstance(utils.disguise_card(last_five_transactions), list)


def test_date_format_change():
    """тест формата даты"""
    last_five_transaction = utils.last_five()[:5]
    assert isinstance(utils.date_format_change(last_five_transaction), list)


def test_output():
    last_five_transaction = utils.last_five()[:5]
    assert utils.output(last_five_transaction) != utils.load_json()
