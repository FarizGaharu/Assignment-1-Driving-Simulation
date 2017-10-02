#print the initial
def word_main():
    word = input('please write the word')
    textb = []
    text = input().split('-')
    for a in text:
        textb.append(a[0])
        print(a[0].upper())
        print(a[0].join())
word_main()
