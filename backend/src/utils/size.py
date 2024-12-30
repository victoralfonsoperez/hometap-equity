acre_size_in_feets = 43560

def square_feet_to_acres(square_feet):
  # 1 acre = 43,560 square feet
  acres = square_feet / acre_size_in_feets
  return acres

def acres_to_square_feet(acres):
  # 1 acre = 43,560 square feet
  square_feet = acres * acre_size_in_feets
  return round(square_feet)