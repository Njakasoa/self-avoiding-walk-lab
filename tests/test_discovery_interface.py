from fractions import Fraction
import pytest
from src.discovery_engine import run_case
from src.discovery_memory import verify_bound
from src.transfer_matrix import transfer_counts

def test_transfer_width_dispatch_matches_occupation_baseline():
    for width in [2,3,4]:
        result=run_case({'kind':'rectangle','width':width,'height':3,'max_n':7})
        assert result['counts']==transfer_counts(width,3,7)
        assert result['status']=='EXACT_FINITE_COUNTS'
        assert result['bound'] is None and result['certificate'] is None
        assert result['state_count']>0
    with pytest.raises(ValueError):run_case({'kind':'rectangle','width':100,'height':100,'max_n':7})
    with pytest.raises(ValueError):run_case({'kind':'bridges','max_n':8,'weights':[1]*4})

def test_certificate_vector_cannot_be_silently_truncated():
    for vector in [[1.9],[True],['3/2']]:
        assert not verify_bound([{0:1}],{'vector':vector,'upper':'1'})
    assert verify_bound([{0:Fraction(1,2)}],{'vector':['2'],'upper':'1/2'})
