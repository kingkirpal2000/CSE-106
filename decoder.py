def Decoder(s):
    i = 0
    answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while(i < len(s)):
        if(i+2 < len(s)):
            if(s[i+2] == "#"):
                digit = s[i]
                digit += s[i+1]
                i = i + 3

            else:
                digit = s[i]
                i = i + 1 # pointer ends
        if(s[i] != "("):
            answer[int(digit)-1] += 1
        else:
            print(s[i])
            i = i + 1
            occur = int(s[i])
            i = i + 2
            answer[int(digit)-1] += occur
    return answer
if __name__ == "__main__":
    s = "12#(2)231(2)"
    decode = Decoder(s)
    print(decode)