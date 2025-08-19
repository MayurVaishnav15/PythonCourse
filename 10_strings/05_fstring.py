template = "hey {}, you are awesome take this {}$ bag"
a= "Mayur"
a1=1000
s1=template.format(a,a1)
print(s1)
# or print(template.format(a,a1)) 
# Now use this concept in fstring
print(f"hey {a}, you are awesome take this {a1}$ bag") 