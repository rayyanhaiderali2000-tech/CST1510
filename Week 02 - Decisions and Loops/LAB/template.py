"""
RECORD CHECK  -  my version
===========================

Name  :   Syed Rayan Ali
Lane  :   IT      (delete two)
Date  :   2026-10-03

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT

label = input("Enter label: ")     
value = float(input("Enter value: "))    
limit = float(input("Enter limit: "))   


# ================================================================== PROCESS

difference = value - limit  
percent = (value / limit) * 100    

if percent >=100:
    status = "OVER LIMIT"
elif percent >=90:
    status = "NEAR LIMIT"
else:
    status = "OK"

# =================================================================== OUTPUT23

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"Value : {value:>10.20f}")
print(f"Limit : {limit:>10.20f}")
print(f"Difference : {difference:>+10.2f}")
print(f"Percent : {percent:>10.2f}")
print(f"Status : {status:>10}")

print("=" * 34)


# ==========================================================================
