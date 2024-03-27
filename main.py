# Part 1
def read_csv(filename):
    """
    Opens the file 'pre-u-enrolment-by-age.csv' and returns the header and the rest of the data as two seperate lists.

    Parameters 
    ----------
    filename: str
        the file that is to be opened

    Returns
    -------
    list 
        list 1 - the header
        list 2 - the data
    """
    filename = 'pre-u-enrolment-by-age.csv'
    with open(filename, 'r') as f:
      header = list(f.readline().strip().split(','))
  
      data = []
      for line in f:
        record = line.strip().split(',')
        record[0] = int(record[0])
        record[3] = int(record[3])
        data.append(record)
      return(header, data)
      


# # Part 2
def filter_gender(enrolment_by_age, sex):
    """
    Opens the file 'pre-u-enrolment-by-age.csv' and a string sex

    Parameters 
    ----------
    filename: str
        the file that is to be opened

    sex: str
        MF or F
        
    Returns
    -------
    list 
        list 1 - data of male enrolment without sex
        list 2 - data of female enrolment without sex
#     """
    sex_m = "MF"
    sex_f = "F"
    
    MF_sexrecord = []
    F_sexrecord = []
    for row in enrolment_by_age:
      if sex_m in row[2]:
        MF_sexrecord.append([row[0], row[1], row[3]])
        return MF_sexrecord
    
      elif sex_f in row[2]:
        F_sexrecord.append([row[0], row[1], row[3]])
        return F_sexrecord


# Part 3
def sum_by_year(enrolment_data):
    """
    """
    enrolment_by_year_list = []
    count = 0
    for line in enrolment_data:
      for x in range(1984, 2018):
        if int(x) in line[0]:
          count = count + 1
      enrolment_by_year_list.append(x, count)
      return enrolment_by_year_list
      
# # Part 4
def write_csv(filename, header, data):
    """
    """
    filename = 'total-enrolment-by-year.csv'
    with open(filename, 'w') as f:
      f.writelines(header)
      count = 0
      for rows in data:
        for y in range(len(rows)):
          rows[y] = str(rows[y])
        f.writelines(','.join(rows))
        count += 1
      
    return count
    
#     pass


# # TESTING
# # You can write code below to call the above functions
# # and test the output

