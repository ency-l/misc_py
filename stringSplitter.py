string=input ("String to split:")
div=input("Divider character to split the string with (Will not be in output):")
split_input=str.split(string,div)
print(f"\nSplitting \"{string}\" by \"{div}\".")
if len(split_input)==1:
    print("\nWARNING:The string doesn't contain the designated divider character. No splitting was done.")
print("\n----------------------------------")
for item in split_input:
    print(f'[{split_input.index(item)}] {item}')
print("----------------------------------")
