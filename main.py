import easy
import medium
import difficult

def do_easy():
    # "easy" problems
    easy.one()
    easy.two()
    easy.three()
    easy.four()
    easy.five(10)
    easy.six(8)
    easy.seven('circumlocution')
    easy.eight(24)
    easy.nine()
    easy.ten('circumlocution')

def do_medium():
    # "medium" problems
    medium.one([1, 32, 9, 98, 45])
    medium.two([1, 2, 3, 4, 5])
    medium.three('level')
    medium.four(10, 2, 2)
    medium.five([1, 32, 9, 98, 45])
    medium.six(5)
    medium.seven(49)
    medium.eight()
    medium.nine('Hello, everyone! This is a test sentence.')
    medium.ten([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])

def do_difficult():
    # "difficult" problems
    difficult.one(12)
    difficult.two(10)
    difficult.three('listen', 'silent')
    difficult.four(10, 2, 2)
    difficult.five([9, 2, 7, 4, 5])
    difficult.six(28)
    difficult.seven(12345)
    difficult.eight('Which is the longest word in this sentence?')
    difficult.nine('The quick brown fox jumps over the lazy dog')
    difficult.ten()

def main():
    do_easy()
    do_medium()
    do_difficult()

main()
