def concatenate(s1: str, s2: str) -> str:
    # result = s1 + s2
    # if len(result) > 10:
    #     return "Too long!"
    # else:
    #     return result

    return (s1 + s2) if len(s1 + s2) <= 10 else "Too long!"


# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
