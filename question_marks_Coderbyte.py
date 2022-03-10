'''
CODERBYTE - Question marks
===============================================================================
Have the function QuestionsMarks(str) take the str string parameter, which will 
contain single digit numbers, letters, and question marks, and check if there 
are exactly 3 question marks between every pair of two numbers that add up to 
10. If so, then your program should return the string true, otherwise it should 
return the string false. If there aren't any two numbers that add up to 10 in 
the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return 
true because there are exactly 3 question marks between 6 and 4, and 3 question 
marks between 5 and 5 at the end of the string.

'''

def QuestionsMarks(strParam):
  q_count = 0
  a = 0
  b = 0
  for char in strParam:
    if char.isdigit():
      b = int(char) + int(a)
      if q_count == 3 and b == 10: 
        return "true"
      a = int(char)
      q_count = 0 
    elif char == '?':
      q_count += 1

  return "false"
if __name__ == '__main__':
    
    ar = ["arrb6???4xxbl5???eee5","acc?7??sss?3rr1??????5", 
            "?5?5?5?", "9?8??d?2", "1?1?1?1","1??2?", "1??2?2","1??ba?9", 
            "arrb6???4xxbl5???eee5"]
            
    print(QuestionsMarks("acc?7??sss?3rr1??????5"))
    for item in ar:
        print(QuestionsMarks(item))