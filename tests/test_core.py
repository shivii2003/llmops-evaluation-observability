from app.core import evaluate
def test_metrics():
    assert evaluate([{'sources':['a']},{'sources':[]}])['citation_coverage']==0.5
