def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])


input_string = "hello"
reversed_output = reverse_string(input_string)
print(reversed_output)  