from collections import Counter
def k_char(text, k):
    #use the counter
    freq = Counter(text)

    #order
    ordered = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return ordered[k][0]

def frequency(text):
    all_freq = {}
 
    for i in text:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
 
    # printing result
    print("Count of all characters in GeeksforGeeks is :\n "+ str(all_freq))