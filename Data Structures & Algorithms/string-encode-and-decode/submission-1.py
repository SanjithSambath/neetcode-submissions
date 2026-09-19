class Solution:

    def encode(self, strs: List[str]) -> str:

        for index, word in enumerate(strs): 
            strs[index] = str(len(word)) + "#" + word

        return ("".join(strs))






    def decode(self, s: str) -> List[str]:

        print(s)

        output = []
        i = 0
        length = 0

        while i < len(s):

            n = 1

            while s[i+n] != "#":
                n += 1

            length = int(s[i:i+n])

            first_term = i + n + 1
            second_term = first_term + length

            word_slice = s[first_term:second_term]

            output.append(word_slice)

            i = second_term

        return(output)