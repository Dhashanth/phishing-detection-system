from src.service import analyze

def test_analyze_returns_score():
    result = analyze({})
    assert isinstance(result, dict)
    assert "score" in result
