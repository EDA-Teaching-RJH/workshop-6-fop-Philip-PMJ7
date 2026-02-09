sample_bay = ["Basalt", "Silica", "Iron", "Dust"]

print(sample_bay[0])
print(sample_bay[len(sample_bay)-1])
print(len(sample_bay))

for item in range(len(sample_bay)):
    print("Transmitting data for: ", sample_bay[item])

new_findings = []
i = 0
for x in range(0,3):
    new_rock = input("New Rock Detcted - Enter name: ")
    new_findings.append(new_rock)
    print(new_findings)

if "Dust" in sample_bay:
    sample_bay.remove("Dust")
    print(sample_bay)
else:
    print("No dust detected.")