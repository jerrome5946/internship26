def right_angle_pattern(rows):
    for i in range(1, rows + 1):
        print("*" * i)
        
        
right_angle_pattern(5)  
   
def pyramid_pattern(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))
      
pyramid_pattern(6)        