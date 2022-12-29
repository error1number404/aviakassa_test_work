from main import main


def test_result():
    result = main()

    with open("result.json", 'r') as f:
        assert f.readline() == result.json()
