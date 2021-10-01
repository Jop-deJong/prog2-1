print("""
    <svg version="1.1"
    baseProfile="full"
    width="300" height="200"
    xmlns="http://www.w3.org/2000/svg">
    """)
for circle in range(0,100):
    print (f' <circle cx="{circle}" cy="{circle}" r="80" fill="green"/> ')
   
print ("</svg>")