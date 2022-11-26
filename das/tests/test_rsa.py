from ..algorithms.RSA import RSA

def test_rsa():
    r = RSA(79, 89)

    assert r.k==5, f"k={r.k} (should be 5)"
    assert r.d==1373, f"d = {r.d} (should be 1373)"
    assert r.n==7031, f"d = {r.n} (should be 7031)"

    assert (
        r.encrypt(44) == 4119
    ), "Does not match example (p=79, q=89, ciphertext=4119). NOT {r.encrypt(44)}"
    assert r.d * r.k % r.phi_n == 1, "d and k are not inverses!"
    assert r.decrypt(r.encrypt(100)) == 100, r.decrypt(r.encrypt(100))


def test_2_users():
    generator = RSA()
    _d = generator.__dict__

    
    rsa2 = RSA(3,7)
    rsa2.n = _d["n"]
    rsa2.d = _d["d"]

    rsa3 = RSA(3,7)
    rsa3.n = _d["n"]
    rsa3.k = _d["k"]

    pt = 2**63
    ct = rsa3.encrypt(pt)
    assert rsa2.decrypt(ct) == pt