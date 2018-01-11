ciphertext = "aMngfiqieu .oVsul sizep ul saficelemtnq audnt uoet sel seltter sostnd na selb noo drer .eJp neesq euv uo siaemirzea ovriv toerm tod  eapss eamnietantn :chldfhragfeeX."

decoded = ""
i = 0
while (i+1 < len(ciphertext)):
    decoded += ciphertext[i+1] + ciphertext[i]
    i += 2

print (decoded)
