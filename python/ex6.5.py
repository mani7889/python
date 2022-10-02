text = "X-DSPAM-Confidence:    0.8475"
no=text.find('0')
strng=float(text[no: ])
print(strng)