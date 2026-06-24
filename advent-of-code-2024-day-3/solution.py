import re


# read the text input and find sequence of mul(123,4)
# but not like mul ( 2 , 4 ) or mul(4*, so no space between elements and two paranthesis + comma




class Solution:
    # so length of text is approx 20k we dont need to store or create another substring
    # just do the math is enough

    def start_end_finder(self, text):
        start_pos = []
        for m in re.finditer(r"mul\(", text):
            start_pos.append(m.start() + 4)
        return start_pos

    def enable_label(self, text):
        labelled_text = []
        start_pos_do = []
        for m in re.finditer(r"do\(\)", text):
            start_pos_do.append(m.start())

        start_pos_dont = []
        for m in re.finditer(r"don't\(\)", text):
            start_pos_dont.append(m.start())

        counter = 0
        label = 1
        while counter < len(text):
            if len(start_pos_do) == 0 and len(start_pos_dont) > 0:
                if counter < start_pos_dont[0]:
                    labelled_text.append(label)
                elif counter == start_pos_dont[0]:
                    start_pos_dont.pop(0)
                    label = 0
            if len(start_pos_do) > 0 and len(start_pos_dont) == 0:
                if counter < start_pos_do[0]:
                    labelled_text.append(label)
                elif counter == start_pos_do[0]:
                    start_pos_do.pop(0)
                    label = 1

            if len(start_pos_do) == 0 and len(start_pos_dont) == 0:
                labelled_text.append(label)

            if len(start_pos_do) > 0 and len(start_pos_dont) > 0:
                if counter < min(start_pos_do[0], start_pos_dont[0]):
                    labelled_text.append(label)
                elif counter == min(start_pos_do[0], start_pos_dont[0]):
                    if start_pos_do[0] < start_pos_dont[0]:
                        start_pos_do.pop(0)
                        label = 1
                    else:
                        start_pos_dont.pop(0)
                        label = 0
                    labelled_text.append(label)

            counter += 1

        return labelled_text

    def solve(self, text):
        # check what comes after r"mul\("
        # it has to be a number, if not skip
        # and keep adding , until if we see not a number but a comma, add comma
        # and if we see two comma again skip to the next r"mul\("
        # if not number and not comma and if we have already one comma and we see ) next
        # then legit collection and calculate
        # better idea: restricting from righthand side
        
        enable = self.enable_label(text)
        start_pos = self.start_end_finder(text)

        num_comma = 0
        slider = 0
        counter = 0
        x = []
        y = []
        condition = True
        multiplication_1 = 0
        multiplication_2 = 0

        while condition:
            if counter > len(start_pos) - 1:
                break
            if start_pos[counter] + slider > len(text) - 1:
                break

            if text[start_pos[counter] + slider].isdigit():
                x.append(int(text[start_pos[counter] + slider]))
                slider += 1
            elif text[start_pos[counter] + slider] == ",":
                if num_comma > 0:
                    num_comma = 0
                    slider = 0
                    counter += 1
                    x = []
                    y = []
                else:
                    num_comma += 1
                    slider += 1
                    y = x
                    x = []
            elif text[start_pos[counter] + slider] == ")":
                # save the multiplication, x as number and y as number
                num1 = int("".join(str(n) for n in y))
                num2 = int("".join(str(n) for n in x))
                multiplication_1 += num1 * num2
                # if do is enabled assign every element in the array a 1 or 0
                # after a dont appear that array has a 0 in it
                if enable[start_pos[counter] + slider] == 1:
                    multiplication_2 += num1 * num2
                slider = 0
                counter += 1
                num_comma = 0
                x = []
                y = []
                #print(num1, num2)
            else:
                slider = 0
                counter += 1
                num_comma = 0
                x = []
                y = []

        return multiplication_1, multiplication_2


with open("input.txt") as f:
    text = f.read().replace("\n", "")


# my own small test instances 
text1 = "mul(mul(asjasj)fdon't()gjmul(12,1212,)ashdo()asmul(123,133),mul(12,32)don't()mul(0,1267)mul(2,23)do()mul(12,11)323232"
text2 = "123456don't()123do()12don't()do()12345"

multiplication = Solution().solve(text)
