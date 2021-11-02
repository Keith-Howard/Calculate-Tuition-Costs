# input txt file
# processing read tx file data
# processing convert txt file data to float
# output float to be used in main calculations
def get_credit_hour_cost(txt_file):
    with open(txt_file) as opened_file:
        line = opened_file.read()
        credit_hour_cost = float(line)
    opened_file.close()
    return credit_hour_cost


# input table of tuition data by year
# processing save tuition data to a txt file
# output txt file
def create_tuition_report(txt_file, new_content):
    school_report_heading = "Community College of Aurora Tuition Report\n" \
                            "------------------------------------------\n" \
                            " Year     Tuition\n" \
                            "-------  ----------\n"
    opened_file = open(txt_file, "w")
    opened_file.write(school_report_heading)
    for content in new_content:
        opened_file.write(content + "\n")
    opened_file.close()


# input input string for tuition increase %
# convert string to float if int or keep it float if float
# output the tuition increase percentage
def calculate_increase_percentage(increase):
    if increase.isdigit():
        increase_percentage = float(increase) / 100
    else:
        increase_percentage = float(increase)
    return increase_percentage


input_text_file = r"input/CCA_Costs.txt"
output_text_file = r"output/TuitionResults.txt"
credit_hour_cost = get_credit_hour_cost(input_text_file)
print("Please Enter Tuition Increase Percentage")
tuition_increase = input("Please enter whole number or decimal. ")
tuition_increase_percentage = calculate_increase_percentage(tuition_increase)
years_to_implement_increase = int(input("Enter How Many Years to Show Increase "))
credit_hours_per_semester = float(input("Enter Number of Credit Hours Per Semester "))

tuition_each_year = []
for year in range(years_to_implement_increase + 1):
    if year >= 9:
        tuition_year = "Year " + str(year + 1) + "  "
    else:
        tuition_year = "Year " + str(year + 1) + "   "
    tuition_value = ("${:,.2f}".format((credit_hours_per_semester * credit_hour_cost) * 2))
    year_and_tuition = tuition_year + tuition_value.rjust(10)
    tuition_each_year.append(year_and_tuition)
    print(year_and_tuition)
    credit_hour_cost += (tuition_increase_percentage * credit_hour_cost)
create_tuition_report(output_text_file, tuition_each_year)
