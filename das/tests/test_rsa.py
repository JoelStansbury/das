from ..algorithms.RSA import RSA

def test_rsa():
    r = RSA(79, 89)

    print(f"k = {r.k} (should be 5)")
    print(f"d = {r.d} (should be 1373)")
    print(f"d = {r.n} (should be 7031)")

    assert (
        r.encrypt(44) == 4119
    ), "Does not match example (p=79, q=89, ciphertext=4119). NOT {r.encrypt(44)}"
    assert r.d * r.k % r.phi_n == 1, "d and k are not inverses!"
    assert r.decrypt(r.encrypt(100)) == 100, r.decrypt(r.encrypt(100))