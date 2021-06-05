words = input().split(", ")
output = [f"{word} -> {len(word)}" for word in words]

print(', '.join(output))
