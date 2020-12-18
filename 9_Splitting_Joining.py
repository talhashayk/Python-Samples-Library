problems = "Broke, Fat, Shoulder, Hair"
print(problems)

split_problems = problems.split(", ")
print(split_problems)

join_problems = " and ".join(split_problems)
print(join_problems)

join_csv = ",".join(split_problems)
print(join_csv)
