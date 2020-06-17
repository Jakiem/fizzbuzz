# BEGIN (write your solution here)
def fizz_buzz(begin, end):
    result = []
    if begin and end and begin < end:
        for i in range(begin, end + 1):
            if i % 5 == 0 and i % 3 == 0:
                result.append('fizz_buzz')
            elif i % 5 == 0:
                result.append('buzz')
            elif i % 3 == 0:
               result.append('fizz')
            else:
                result.append(str(i))
        print(' '.join(result))
        return ' '.join(result)
    elif begin == end:
        print(begin)
        return str(begin)
    else:
        print('')
        return ''
     
# END
fizz_buzz(7, 7)