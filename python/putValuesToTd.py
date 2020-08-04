

filepath = 'values.txt'
with open(filepath) as file:
    line = file.readline().strip()
    while line:
        split = line.split(" ")
        print("<tr>")
        print(" <td></td>")
        print(" <td>" + split[2] + " g</td>")
        print(" <td>" + split[1] + " g</td>")
        print(" <td>" + split[0] + "</td>")
        print("</tr>")
        line = file.readline().strip()
