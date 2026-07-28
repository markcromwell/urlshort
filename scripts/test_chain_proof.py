from app.chain_proof import chain_proof_marker


def test_chain_proof_marker():
    assert chain_proof_marker() == 'chain-proof-ok'
