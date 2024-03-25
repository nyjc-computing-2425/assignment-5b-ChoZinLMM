# Part 1
# def read_csv(filename):
    # filename = 'pre-u-enrolment-by-age.csv'
with open('pre-u-enrolment-by-age.csv', 'r') as f:
  # header = list(f.readline().strip().split(','))
  # print(header)



  data = []
  for line in f:
    record = list(line.strip().split(','))
    record[0] = int(record[0])
    record[]
    
    data.append(record)
  print(data)
        
    # pass


# # Part 2
# def filter_gender(enrolment_by_age, sex):
#     # Type your code below
#     pass


# # Part 3
# def sum_by_year(enrolment):
#     # Type your code below
#     pass


# # Part 4
# def write_csv(filename, header, data):
#     # Type your code below
#     pass


# # TESTING
# # You can write code below to call the above functions
# # and test the output
