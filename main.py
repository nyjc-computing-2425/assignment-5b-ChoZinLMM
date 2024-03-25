# Part 1
# def read_csv(filename):
#     """
#     Opens the file 'pre-u-enrolment-by-age.csv' and returns the header and the rest of the data as two seperate lists.

#     Parameters 
#     ----------
#     filename: str
#         the file that is to be opened

#     Returns
#     -------
#     list 
#         list 1 - the header
#         list 2 - the data
#     """
#     filename = 'pre-u-enrolment-by-age.csv'
#     with open(filename, 'r') as f:
#       header = list(f.readline().strip().split(','))
  
#       data = []
#       for line in f:
#         record = line.strip().split(',')
#         record[0] = int(record[0])
#         record[3] = int(record[3])
#         data.append(record)
#       return(header, data)
      


# # Part 2
# def filter_gender(enrolment_by_age, sex):
#     """
#     Opens the file 'pre-u-enrolment-by-age.csv' and a string sex

#     Parameters 
#     ----------
#     filename: str
#         the file that is to be opened

#     sex: str
#         MF or F
        
#     Returns
#     -------
#     list 
#         list 1 - data of male enrolment without sex
#         list 2 - data of female enrolment without sex
# #     """
sex_m = "MF"
sex_f = "F"
with open('pre-u-enrolment-by-age.csv', 'r') as f:
  header = list(f.readline().strip().split(','))
  data = []
  sex_mdata = []
  sex_fdata = []
  for line in f:
    record = line.strip().split(',')
    record[0] = int(record[0])
    record[3] = int(record[3])
    data.append(record)

    if sex_m in record[2]:
      sex_mdata.append(record)
      for row in (0, 4):
        sex_mdata.remove(sex_mdata[2])
    print(sex_mdata) 
          
  #   elif sex_f in record[2]:
  #     sex_fdata.append(record)
  #     sex_fdata.remove("F")
  # print(sex_fdata)

        

    
          
    # pass


# Part 3
def sum_by_year(enrolment_data):
    # Type your code below
    pass


# # Part 4
# def write_csv(filename, header, data):
#     # Type your code below
#     pass


# # TESTING
# # You can write code below to call the above functions
# # and test the output
