def word_count(n):
    #this is only for giving onethousand
    if n == 1000:
        return "onethousand"
    # yeh 0-9 wale case handle krne ke lia
    ones = ["","one","two","three","four","five","six","seven","eight","nine"]
    # yeh teens wale case handle krne ke lia
    teen = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    # yeh tenth place wale handle krne ke lia
    tenth = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # empty string pure word ko handle krne ke lia
    word = ""
    if (n >= 100):
        word += ones[n // 100] + "hundred"
        if n % 100 != 0:
            word += "and"
    n %= 100
    if (10 < n < 20): word += teen[n - 10]

    else:
        word += tenth[n // 10]
        word += ones[n % 10]
    
    return word

sample_input = sum(len(word_count(i)) for i in range(1, 1001))

print(sample_input)

#TIME COMPLEXITY O(1)