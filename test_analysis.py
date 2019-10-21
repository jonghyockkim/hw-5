import analysis

def test_average():
    avg = analysis.average_inflammations(0)
    assert(avg == 5.45)

def test_max():
    #raise Exception("Remove this line and implement your test instead")
    avg = analysis.max_inflammations(0)
    assert(avg == 18)

def test_acute_patient():
    #raise Exception("Remove this line and implement your test instead")
    avg = analysis.acute_patient()
    assert(avg == 0)
