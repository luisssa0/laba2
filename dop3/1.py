
with open('input.txt', 'r') as input_file:

    with open('output1.txt', 'w') as output1_file:

        for line in input_file:

            if line.startswith("#"):
                continue

            elif line.startswith(("DB", "DW", "DD")):

                parts = line.strip().split(",")

                data_type, number = parts[0], int(parts[1])

                if data_type == "DB" and number == 100:
                    new_number = number
                else:

                    if 8 <= number <= 15:
                        new_number = (number - 8) * 2
                    elif 0 <= number <= 8:
                        new_number = (number * 2) + 1
                    else:
                        new_number = number * 2

                if data_type == "DB":
                    new_data_type = "DB"
                elif data_type == "DW":
                    new_data_type = "DBW"
                elif data_type == "DD":
                    new_data_type = "DBD"

                output_line = f"{new_data_type}{new_number},{parts[2]}\n"
                output2_file.write(output_line)

            else:
                output1_file.write(line)
