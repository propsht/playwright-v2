import utils

def test_root():
    utils.root()
    print("testing for 25...")
    root_25num = utils.root(25)
    print(".... got ", root_25num)
    assert root_25num == 5